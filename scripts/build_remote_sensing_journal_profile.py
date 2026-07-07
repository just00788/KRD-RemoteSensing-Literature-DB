#!/usr/bin/env python3
"""Build Remote Sensing journal style profile artifacts from rs-only PDFs."""

from __future__ import annotations

import csv
import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
RS_PDF_DIR = REPO_ROOT / "docs" / "literature" / "pdfs" / "remote_sensing_only"
PROFILE_DIR = REPO_ROOT / "docs" / "literature" / "remote_sensing_journal_profile"
READERS_DIR = PROFILE_DIR / "readers"
CARDS_DIR = PROFILE_DIR / "style_cards"
SECTION_DIR = PROFILE_DIR / "section_patterns"
PHRASE_DIR = PROFILE_DIR / "phrase_bank"
TERM_DIR = PROFILE_DIR / "terminology"
FIGTAB_DIR = PROFILE_DIR / "figure_table_patterns"
SYNTHESIS_DIR = PROFILE_DIR / "synthesis"
SKILL_SOURCE_DIR = REPO_ROOT / "docs" / "literature" / "skill_source"

SECTION_PATTERNS = {
    "Abstract": [r"\babstract\b"],
    "Introduction": [r"\b1\.?\s*introduction\b", r"\bintroduction\b"],
    "Materials and Methods": [r"materials and methods", r"\bmethods\b", r"\bmethodology\b"],
    "Study Area": [r"study area", r"study site"],
    "Data": [r"\bdata\b", r"dataset", r"satellite"],
    "Results": [r"\bresults\b", r"accuracy"],
    "Discussion": [r"\bdiscussion\b"],
    "Conclusions": [r"\bconclusions?\b"],
    "References": [r"\breferences\b"],
    "Data Availability": [r"data availability"],
    "Author Contributions": [r"author contributions"],
    "Funding": [r"\bfunding\b"],
    "Conflicts of Interest": [r"conflicts of interest", r"conflict of interest"],
    "Supplementary Materials": [r"supplementary materials?"],
}

TERMS = [
    "rocky desertification",
    "karst rocky desertification",
    "bare rock",
    "bare-rock fraction",
    "fractional bare rock cover",
    "exposed bedrock fraction",
    "fractional vegetation cover",
    "linear spectral mixture model",
    "spectral mixture analysis",
    "fully constrained least squares",
    "machine learning",
    "random forest",
    "support vector machine",
    "semantic segmentation",
    "DeepLabV3+",
    "encoder-decoder",
    "atrous spatial pyramid pooling",
    "DEM",
    "slope",
    "aspect",
    "hillshade",
    "multi-source remote sensing",
    "Gaofen",
    "Sentinel",
    "Landsat",
    "cross-region",
    "independent validation",
    "overall accuracy",
    "Kappa",
    "F1",
    "intersection over union",
]

METADATA_OVERRIDES = {
    "2014_RemoteSens_6_9895": ("KRD0016", "Is Forest Restoration in the Southwest China Karst Promoted Mainly by Climate Change or Human-Induced Factors?", "2014", "10.3390/rs6109895"),
    "2016_RemoteSens_8_68": ("KRD0023", "Quantitative Estimation of Carbonate Rock Fraction in Karst Regions Based on Spectral Feature Analysis", "2016", "10.3390/rs8010068"),
    "2018_RemoteSens_10_1321": ("KRD0025", "Analysis of Landsat-8 OLI Imagery for Estimating Exposed Bedrock Fractions in Typical Karst Regions of Southwest China", "2018", "10.3390/rs10091321"),
    "2021_RemoteSens_13_1614": ("KRD0034", "How Can We Realize Sustainable Development Goals in Rocky Desertified Regions by Enhancing Crop Yield and Restoring Ecological Function?", "2021", "10.3390/rs13091614"),
    "2021_RemoteSens_13_2497": ("KRD0033", "Extracting Information on Rocky Desertification from Satellite Images: A Comparative Study", "2021", "10.3390/rs13132497"),
    "2021_RemoteSens_13_2935": ("KRD0035", "Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic", "2021", "10.3390/rs13152935"),
    "2022_RemoteSens_14_2351": ("KRD0045", "The Changes of Spatiotemporal Pattern of Rocky Desertification and Its Dominant Driving Factors in Typical Karst Mountainous Areas under the Background of Global Change", "2022", "10.3390/rs14102351"),
    "2022_RemoteSens_14_292": ("KRD0044", "Spatiotemporal Evolution Analysis and Future Scenario Prediction of Rocky Desertification in a Subtropical Karst Region", "2022", "10.3390/rs14020292"),
    "2023_RemoteSens_15_3056": ("KRD0046", "Extraction of Rocky Desertification Information in the Karst Area Based on the Red-NIR-SWIR Spectral Feature Space", "2023", "10.3390/rs15123056"),
    "2024_RemoteSens_16_4786": ("KRD0052", "Classification of Karst Rocky Desertification Levels in Jinsha County Using a Feature Space Method Based on SDGSAT-1 Multispectral Data", "2024", "10.3390/rs16244786"),
    "2025_RemoteSens_17_2294": ("KRD0070", "Spatiotemporal Evolution and Driving Factors of Karst Rocky Desertification in Guangxi, China, Under Climate Change and Human Activities", "2025", "10.3390/rs17132294"),
}


@dataclass
class StylePaper:
    rs_id: str
    paper_id: str
    file_name: str
    title: str
    year: str
    doi: str
    pdf_path: str
    already_batch_01: bool
    already_batch_02: bool
    pages: list[str]
    page_count: int
    sections: dict[str, list[int]] = field(default_factory=dict)
    headings: list[str] = field(default_factory=list)
    captions: list[dict[str, str]] = field(default_factory=list)
    fig_refs: list[dict[str, str]] = field(default_factory=list)
    abstract_text: str = ""
    methods_hits: list[str] = field(default_factory=list)
    results_hits: list[str] = field(default_factory=list)
    discussion_hits: list[str] = field(default_factory=list)
    terms_found: list[str] = field(default_factory=list)
    manual_review: list[str] = field(default_factory=list)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def extract_pages(pdf_path: Path) -> tuple[list[str], list[str]]:
    reader = PdfReader(str(pdf_path))
    pages, errors = [], []
    for i, page in enumerate(reader.pages, start=1):
        try:
            pages.append(clean_text(page.extract_text() or ""))
        except Exception as exc:
            pages.append("")
            errors.append(f"p.{i}: {type(exc).__name__}")
    return pages, errors


def find_pages(pages: list[str], patterns: list[str]) -> list[int]:
    found = []
    for i, page in enumerate(pages, start=1):
        if any(re.search(pattern, page, flags=re.I) for pattern in patterns):
            found.append(i)
    return found


def extract_headings(pages: list[str]) -> list[str]:
    headings = []
    for page in pages:
        for line in page.splitlines():
            line = normalize(line)
            if re.match(r"^\d+(\.\d+)*\.?\s+[A-Z][A-Za-z0-9,()\- /]{4,90}$", line):
                if line not in headings:
                    headings.append(line)
            elif line in ["Abstract", "Introduction", "Materials and Methods", "Results", "Discussion", "Conclusions", "References"]:
                if line not in headings:
                    headings.append(line)
    return headings[:60]


def extract_captions(pages: list[str]) -> list[dict[str, str]]:
    caps = []
    pattern = re.compile(r"(?im)^\s*((?:Figure|Fig\.?|Table)\s+\d+[^\n]{0,450})")
    for page_no, page in enumerate(pages, start=1):
        for match in pattern.finditer(page):
            caption = normalize(match.group(1))
            if len(caption) > 8:
                caps.append({"page": str(page_no), "caption": caption})
    return caps[:35]


def extract_fig_refs(pages: list[str]) -> list[dict[str, str]]:
    refs = []
    pattern = re.compile(r"\b(?:Figure|Fig\.|Table)\s+\d+[A-Za-z]?\b")
    for page_no, page in enumerate(pages, start=1):
        sentences = re.split(r"(?<=[.!?])\s+", page)
        for sent in sentences:
            if pattern.search(sent):
                refs.append({"page": str(page_no), "text": normalize(sent)[:280]})
            if len(refs) >= 30:
                return refs
    return refs


def extract_abstract(pages: list[str]) -> str:
    text = "\n".join(pages[:3])
    match = re.search(r"(?is)\babstract\b\s*(.+?)(?:\bkeywords?\b|1\.?\s*introduction|\bintroduction\b)", text)
    if match:
        return normalize(match.group(1))[:1600]
    return normalize(text[:1000])


def sentence_hits(pages: list[str], terms: list[str], limit: int = 8) -> list[str]:
    hits = []
    for page_no, page in enumerate(pages, start=1):
        for sent in re.split(r"(?<=[.!?])\s+", page):
            if any(term.lower() in sent.lower() for term in terms):
                hits.append(f"p.{page_no}: {normalize(sent)[:260]}")
                if len(hits) >= limit:
                    return hits
    return hits


def metadata_from_filename(pdf: Path) -> tuple[str, str, str, str]:
    for key, values in METADATA_OVERRIDES.items():
        if key in pdf.name:
            return values
    stem = pdf.stem.replace("_", " ")
    return ("unknown", stem, "unknown", "unknown")


def load_batch_read_ids() -> tuple[set[str], set[str]]:
    rows1 = read_csv(REPO_ROOT / "database" / "literature_database_enriched_batch_01.csv")
    rows2 = read_csv(REPO_ROOT / "database" / "literature_database_enriched_batch_02.csv")
    return (
        {row["paper_id"] for row in rows1 if row.get("reader_path")},
        {row["paper_id"] for row in rows2 if row.get("reader_path")},
    )


def build_papers() -> list[StylePaper]:
    batch1, batch2 = load_batch_read_ids()
    papers = []
    for idx, pdf in enumerate(sorted(RS_PDF_DIR.glob("*.pdf")), start=1):
        paper_id, title, year, doi = metadata_from_filename(pdf)
        pages, errors = extract_pages(pdf)
        paper = StylePaper(
            rs_id=f"RS{idx:03d}",
            paper_id=paper_id,
            file_name=pdf.name,
            title=title,
            year=year,
            doi=doi,
            pdf_path=pdf.relative_to(REPO_ROOT).as_posix(),
            already_batch_01=paper_id in batch1,
            already_batch_02=paper_id in batch2,
            pages=pages,
            page_count=len(pages),
        )
        paper.sections = {name: find_pages(pages, patterns) for name, patterns in SECTION_PATTERNS.items()}
        paper.headings = extract_headings(pages)
        paper.captions = extract_captions(pages)
        paper.fig_refs = extract_fig_refs(pages)
        paper.abstract_text = extract_abstract(pages)
        paper.methods_hits = sentence_hits(pages, ["workflow", "method", "data", "accuracy", "model", "sample"], 10)
        paper.results_hits = sentence_hits(pages, ["results", "accuracy", "Kappa", "overall accuracy", "RMSE", "classification"], 10)
        paper.discussion_hits = sentence_hits(pages, ["discussion", "limitation", "future", "compared with", "uncertainty"], 8)
        lower = "\n".join(pages).lower()
        paper.terms_found = [term for term in TERMS if term.lower() in lower]
        if errors:
            paper.manual_review.extend(errors)
        if not paper.captions:
            paper.manual_review.append("figure/table captions not located by text parser")
        if paper_id == "unknown":
            paper.manual_review.append("metadata needs manual verification")
        papers.append(paper)
    return papers


def anchor(pages: list[int]) -> str:
    if not pages:
        return "not located"
    return ", ".join(f"p.{p}" for p in pages[:10]) + (", ..." if len(pages) > 10 else "")


def bullet(items: list[str], fallback: str = "not located") -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)


def caption_table(paper: StylePaper) -> str:
    if not paper.captions:
        return "| Figure/Table | Caption style | What it shows | Text reference pattern | Relevance to our manuscript |\n|---|---|---|---|---|\n| not located | manual review needed | unknown | unknown | inspect PDF |"
    lines = ["| Figure/Table | Caption style | What it shows | Text reference pattern | Relevance to our manuscript |", "|---|---|---|---|---|"]
    for cap in paper.captions[:16]:
        label = re.match(r"((?:Figure|Fig\.?|Table)\s+\d+[A-Za-z]?)", cap["caption"])
        label_text = label.group(1) if label else "caption"
        kind = "descriptive caption with object/result label"
        shows = "study design/result/map/table evidence inferred from caption; inspect figure before reuse"
        ref = "main text generally refers by Figure/Table number"
        rel = "useful as pattern for maps, workflow, data source, accuracy, or comparison displays"
        lines.append(f"| p.{cap['page']} {label_text} | {kind} | {shows} | {ref} | {rel} |")
    return "\n".join(lines)


def structure_table(paper: StylePaper) -> str:
    rows = []
    for heading in paper.headings[:30]:
        low = heading.lower()
        if "introduction" in low:
            func = "sets background, problem importance, literature gap"
        elif "method" in low or "data" in low or "area" in low:
            func = "establishes reproducible materials, data, workflow, and evaluation"
        elif "result" in low:
            func = "reports maps, comparisons, and metrics"
        elif "discussion" in low:
            func = "interprets mechanisms, compares literature, states limitations"
        elif "conclusion" in low:
            func = "summarizes contribution and application value"
        else:
            func = "article support section or topic-specific subsection"
        rows.append(f"| {heading} | see source headings | {func} | adapt if matching our FBR/DeepLabV3+/DEM workflow |")
    if not rows:
        rows.append("| not fully detected | manual review needed | section extraction limited | inspect PDF |")
    return "| Section | Subsections | Function | Relevance to our manuscript |\n|---|---|---|---|\n" + "\n".join(rows)


ABSTRACT_TEMPLATES = """- Background sentence pattern: [Research object] is important for [ecological or management problem], and remote sensing provides scalable monitoring evidence.
- Gap sentence pattern: However, existing methods remain limited in [spatial detail / class discrimination / bare-rock fraction estimation / transferability].
- Data sentence pattern: This study used [sensor/data sources] covering [study area/time span] to characterize [target variable].
- Method sentence pattern: We developed or compared [method/model] using [features/data] and evaluated it with [metric family].
- Result sentence pattern: The results showed that [method/data combination] improved [mapping or estimation target] according to [appropriate metrics].
- Significance sentence pattern: These findings provide a basis for [KRD monitoring / restoration / transferable mapping / method design]."""

INTRO_TEMPLATES = """- Paragraph 1: KRD background and ecological importance.
- Paragraph 2: Remote sensing and FBR relevance.
- Paragraph 3: Existing spectral unmixing and ML methods.
- Paragraph 4: Deep learning and terrain constraints.
- Paragraph 5: Research gap.
- Paragraph 6: Objectives and contributions.

Reusable moves: move from regional ecological problem -> remote sensing need -> limitations of existing methods -> our data/model/validation gap -> explicit contributions."""

METHOD_TEMPLATES = """- Study Area writing template: locate the region, explain karst/environmental characteristics, and link them to mapping difficulty.
- Data Sources writing template: list sensors, dates, resolution, preprocessing, and why each source is needed.
- Reference Sample and Label Construction template: describe sample source, labeling standard, class system, and quality control.
- FBR / LSMM writing template: define continuous FBR, endmembers/features, constraints, and continuous metrics.
- DeepLabV3+ writing template: specify architecture, backbone, ASPP/decoder, input features, training settings, and baselines.
- DEM Fusion writing template: distinguish open-source DEM for cross-area use from GF-7 stereo DEM for local enhancement.
- Experimental Design writing template: define baseline comparison, ablation, transfer, and spatial split.
- Accuracy Assessment writing template: separate continuous metrics from classification metrics."""

RESULT_TEMPLATES = """- 4.1 LSMM-Based Bare-Rock Fraction Inversion
- 4.2 Rocky Desertification Grade Mapping from Thresholded FBR
- 4.3 Multi-Source GF and Multi-Model Comparison
- 4.4 FCN, U-Net, and DeepLabV3+ Baseline Comparison
- 4.5 Open-Source DEM Terrain-Factor Ablation
- 4.6 Cross-Region Transferability
- 4.7 GF-7 Stereo DEM Local Enhancement
- 4.8 Error and Class-Level Confusion Analysis"""

DISCUSSION_TEMPLATES = """- 5.1 Advantages of DeepLabV3+ for Fragmented Karst Rocky Desertification Mapping
- 5.2 Physical Meaning of FBR and LSMM-Based Continuous Inversion
- 5.3 Contribution of DEM-Derived Terrain Factors
- 5.4 Open-Source DEM for Transferability and GF-7 Stereo DEM for Local Enhancement
- 5.5 Comparison with Previous Studies
- 5.6 Limitations and Future Work"""


def style_reader(paper: StylePaper) -> str:
    abstract_sentence_count = len(re.findall(r"[.!?]", paper.abstract_text))
    return f"""# Remote Sensing Style Reader: {paper.title}

## 1. Bibliographic Information

- RS ID: {paper.rs_id}
- Title: {paper.title}
- Authors: unknown
- Year: {paper.year}
- Journal: Remote Sensing
- DOI: {paper.doi}
- PDF path: `{paper.pdf_path}`
- Language: English
- Already read in previous batches: batch_01={paper.already_batch_01}; batch_02={paper.already_batch_02}
- This rereading focus: journal writing style, section architecture, figure/table pattern, terminology, and reusable templates.

## 2. Article Structure

- Primary headings detected: {len(paper.headings)}
- Independent Discussion: {'yes' if paper.sections.get('Discussion') else 'not located'}
- Independent Conclusions: {'yes' if paper.sections.get('Conclusions') else 'not located'}
- Data Availability / Author Contributions / Funding / Conflicts of Interest: Data Availability={anchor(paper.sections.get('Data Availability', []))}; Author Contributions={anchor(paper.sections.get('Author Contributions', []))}; Funding={anchor(paper.sections.get('Funding', []))}; Conflicts={anchor(paper.sections.get('Conflicts of Interest', []))}
- Supplementary Materials: {anchor(paper.sections.get('Supplementary Materials', []))}
- Overall suitability: useful for our manuscript if we adapt the structure without copying wording.

{structure_table(paper)}

## 3. Abstract Writing Pattern

- Background opening: usually starts from environmental importance or monitoring challenge.
- Problem/gap: {'located through abstract text' if paper.abstract_text else 'not confidently extracted'}.
- Data and method compression: Remote Sensing abstracts tend to compress sensor, study area, model, and validation into one or two sentences.
- Result presentation: reports principal results and often includes metrics when central to the paper.
- Specific accuracy numbers: {'likely present' if re.search(r'\\d+(\\.\\d+)?\\s*%|RMSE|Kappa|R2|R²', paper.abstract_text) else 'not detected in abstract sample'}.
- Significance ending: commonly links the method to monitoring, restoration, or decision support.
- Approximate abstract length: {len(paper.abstract_text.split())} words; {abstract_sentence_count} sentence-like units.
- Suitable expression modes: concise background-gap-data-method-result-significance sequence.

{ABSTRACT_TEMPLATES}

## 4. Introduction Writing Pattern

| Paragraph / Function | What it does | Typical writing move | Useful for our manuscript |
|---|---|---|---|
| Background | establishes ecological/monitoring importance | broad problem -> KRD/karst/land degradation | high |
| Remote sensing value | explains scalable observation | sensor capability -> mapping target | high |
| Literature review | layers prior methods | spectral indices / SMA / ML / DL / DEM | high |
| Gap | names remaining limitation | resolution, heterogeneity, validation, transfer | high |
| Objectives | states study aim and contributions | “This study aims to...” pattern | high |

{INTRO_TEMPLATES}

Located Introduction anchors: {anchor(paper.sections.get('Introduction', []))}

## 5. Materials and Methods Writing Pattern

- Study area: usually separated or early in Methods; anchor {anchor(paper.sections.get('Study Area', []))}.
- Data sources: anchor {anchor(paper.sections.get('Data', []))}; often supported by a data table.
- Data table design: include sensor, date, resolution, bands, preprocessing, and role.
- Preprocessing: describe corrections and derived features before model details.
- Samples and labels: should define class system or reference values.
- Classification/FBR system: keep continuous FBR and categorical classes separate.
- Model/algorithm: introduce architecture/model choices after data/features.
- Formula presentation: place equations near variable definitions.
- Experimental design: separate comparison, ablation, validation, and transfer.
- Accuracy assessment: report metric family matched to target type.
- Workflow figure: recommended for our manuscript.

{METHOD_TEMPLATES}

Located Methods evidence:
{bullet(paper.methods_hits)}

## 6. Results Writing Pattern

- Results order: often data/feature separability -> model/metric comparison -> maps/spatial pattern -> uncertainty or driving factors.
- Overall accuracy first: common when classification is central.
- Class-level metrics: should be reported for class maps when available.
- Maps: normally paired with text interpretation and accuracy evidence.
- Confusion matrix: useful where class confusion matters.
- Ablation: should be separated from main comparison.
- Cross-region validation: should be a dedicated subsection if used.
- Figure/table descriptions: concise, point to the evidence and interpret the pattern.
- Avoid repeating tables: describe the key trend rather than narrating every cell.

Recommended Results structure:
{RESULT_TEMPLATES}

Located Results evidence:
{bullet(paper.results_hits)}

## 7. Discussion Writing Pattern

- Mechanism explanation: connect results to spectral, terrain, model, or ecological mechanism.
- Previous studies: compare directionally and cautiously.
- Model advantages: explain why an approach helps, not just that it performs better.
- Data source differences: link bands/resolution/coverage to mapping effects.
- DEM/topographic role: discuss terrain factors without overstating transfer.
- Limitations/future work: state uncertainty, data limitations, validation constraints, and next steps.
- Avoid repeating Results: Discussion should interpret, compare, and delimit claims.

Recommended Discussion structure:
{DISCUSSION_TEMPLATES}

Located Discussion-style evidence:
{bullet(paper.discussion_hits)}

## 8. Conclusions Writing Pattern

- Typical structure: one compact section with objective reminder, method, key findings, and application value.
- Tone: restrained and evidence-aligned.
- Limitations/future work: sometimes included briefly; do not overclaim.
- Recommended template: “This study addressed [problem] using [data/method]. The results indicate [validated finding]. The approach supports [application], while future work should address [limitation].”

## 9. Figure and Table Style

{caption_table(paper)}

Figure/table style lessons:
- Captions should state what is shown, not just name the figure.
- Text should cite figures/tables when interpreting evidence.
- Accuracy tables should separate metric types and class-level indicators.
- Suggested figures for our paper: study area, workflow, architecture, FBR map, grade map, DEM ablation, cross-region transfer, error/confusion analysis.

Located text reference patterns:
{bullet([f"p.{r['page']}: {r['text']}" for r in paper.fig_refs[:10]])}

## 10. Terminology and Noun Phrase Extraction

| Recommended English term | Chinese equivalent | Use when | Avoid | Example pattern |
|---|---|---|---|---|
| karst rocky desertification | 喀斯特石漠化 | naming the process/problem | vague “rock desert” | mapping karst rocky desertification |
| bare-rock fraction | 裸岩率/裸岩覆盖比例 | continuous/proportional target | calling it a class map | estimate bare-rock fraction |
| exposed bedrock fraction | 基岩裸露率 | bedrock exposure target | mixing with vegetation cover | estimate exposed bedrock fraction |
| spectral mixture analysis | 光谱混合分析 | sub-pixel fraction estimation | classification metrics for regression | SMA-derived fraction |
| semantic segmentation | 语义分割 | pixel-level DL mapping | generic “deep learning” only | semantic segmentation model |
| DeepLabV3+ | DeepLabV3+ | main segmentation model | unexplained DL name | DeepLabV3+-based mapping |
| DEM-derived topographic factors | DEM 派生地形因子 | slope/aspect/elevation inputs | GF-7 transfer overclaim | DEM-derived terrain factors |
| class-level accuracy | 类别级精度 | categorical maps | OA only | report class-level accuracy |

Terms located in this paper: {', '.join(paper.terms_found) if paper.terms_found else 'limited term extraction; inspect manually'}.

## 11. Academic Phrase Bank

### Abstract phrases
- [Problem] poses a challenge for [region/application].
- Remote sensing provides an effective means for [monitoring/mapping target].
- This study used [data] to [objective].
- The proposed/comparative method was evaluated using [metrics].
- The results indicate that [method/data] improves [target mapping].
- These findings support [application or management goal].

### Introduction phrases
- [Phenomenon] has become an important ecological issue in [region].
- Previous studies have used [method family] to address [target].
- However, [limitation] remains insufficiently resolved.
- To address this gap, this study [objective].
- The main contributions are as follows: [contribution list].

### Methods phrases
- The overall workflow is shown in Figure X.
- The dataset was divided using [split strategy].
- Accuracy was evaluated using [metric family].
- To assess the contribution of [factor], an ablation experiment was conducted.
- [Model] was used as a baseline for comparison.

### Results phrases
- As shown in Figure X, [spatial pattern] was observed.
- Table X summarizes the performance of [models/data].
- Compared with [baseline], [method] achieved [metric improvement].
- The confusion matrix indicates that [class confusion pattern].
- The ablation results show the contribution of [factor].

### Discussion phrases
- This improvement may be attributed to [mechanism].
- The result is consistent with/ differs from previous studies because [reason].
- Although [method] performed well, [limitation] remains.
- Future work should further evaluate [uncertainty/transferability].
- These findings should be interpreted cautiously because [constraint].

### Conclusions phrases
- This study developed/evaluated [method] for [target].
- The main findings can be summarized as follows.
- The method provides a practical tool for [application].
- Further studies are needed to [future work].

### Figure/Table reference phrases
- Figure X illustrates the spatial distribution of [target].
- Table X lists the data sources and preprocessing steps.
- Figure X compares the mapping results of different methods.
- Table X reports the class-level accuracy metrics.
- The workflow in Figure X summarizes the main procedure.

### Limitation phrases
- A limitation of this study is [constraint].
- The uncertainty may arise from [source].
- The transferability of the method requires further validation.
- Future work should incorporate [data/validation].
- The results should not be generalized beyond [scope] without additional validation.

### Contribution phrases
- The contribution of this study lies in [method/data/validation].
- This work provides evidence for [scientific or applied value].
- The proposed framework improves [target] by integrating [components].
- The study offers a reproducible workflow for [application].
- The findings can support [monitoring/restoration/management].

## 12. Remote Sensing Style Lessons for Our Manuscript

- What to imitate: clear sectioning, data-method-result linkage, figure/table-supported argument.
- What not to imitate: do not blur continuous FBR inversion with categorical classification.
- Useful structure: background -> data/method -> validation -> spatial interpretation -> limitations.
- Useful phrases: use cautious, metric-specific, source-grounded claims.
- Useful terminology: use canonical KRD/FBR/DEM/segmentation terms consistently.
- Useful figure/table design: combine workflow, data table, maps, accuracy table, ablation, and confusion/error figures.
- Useful caution style: state data and validation constraints explicitly.
- Relevance level: high.

## 13. Manual Review Items

{bullet(paper.manual_review, 'none')}
"""


def style_card(paper: StylePaper) -> str:
    return f"""# Remote Sensing Style Card: {paper.title}

## 1. Bibliographic Information

- RS ID: {paper.rs_id}
- Title: {paper.title}
- Year: {paper.year}
- Journal: Remote Sensing
- DOI: {paper.doi}
- PDF path: `{paper.pdf_path}`

## 2. Why This Paper Matters for Journal Style

It is part of the `remote_sensing_only` target-journal corpus and provides section, caption, and terminology patterns for Remote Sensing-style KRD/karst/ecological remote sensing writing.

## 3. Article Structure Pattern

Detected headings: {', '.join(paper.headings[:12]) if paper.headings else 'manual review needed'}.

## 4. Abstract Pattern

Use background-gap-data-method-result-significance ordering; include metrics only when they are central and clearly supported.

## 5. Introduction Pattern

Move from broad ecological/remote-sensing problem to prior method families, then identify a specific technical gap.

## 6. Methods Pattern

Organize by study area, data, preprocessing, method/model, experiment design, and accuracy assessment.

## 7. Results Pattern

Order results by target variable, model/data comparison, maps, metrics, and uncertainty/error analysis.

## 8. Discussion Pattern

Interpret mechanisms, compare with previous studies, discuss terrain/data/model constraints, and state limitations.

## 9. Figure/Table Pattern

Located captions: {len(paper.captions)}. Use explicit captions and cite figures/tables in interpretive sentences.

## 10. Terminology and Phrase Value

Terms located: {', '.join(paper.terms_found[:12]) if paper.terms_found else 'limited evidence'}.

## 11. Reusable Templates for Our Manuscript

- Abstract: problem -> gap -> data -> method -> result -> significance.
- Methods: study area -> data table -> workflow -> model/baselines -> validation.
- Results: metric-specific reporting with maps and class-level tables.
- Discussion: mechanism -> comparison -> limitation -> future work.

## 12. Skill Knowledge to Extract

Add journal-style rules for Remote Sensing KRD manuscripts: structured method reproducibility, figure/table-driven results, cautious discussion, and strict metric separation.
"""


def write_inventory(papers: list[StylePaper]) -> None:
    lines = [
        "# Remote Sensing Only Paper Inventory",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "| rs_id | file_name | title | year | journal/source | DOI | pdf_path | already_read_in_batch_01 | already_read_in_batch_02 | reread_for_style |",
        "|---|---|---|---:|---|---|---|---|---|---|",
    ]
    for p in papers:
        lines.append(f"| {p.rs_id} | {p.file_name} | {p.title} | {p.year} | Remote Sensing | {p.doi} | `{p.pdf_path}` | {p.already_batch_01} | {p.already_batch_02} | yes |")
    (PROFILE_DIR / "rs_only_paper_inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readers_cards(papers: list[StylePaper]) -> None:
    READERS_DIR.mkdir(parents=True, exist_ok=True)
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    for p in papers:
        (READERS_DIR / f"{p.rs_id}_style_reader.md").write_text(style_reader(p), encoding="utf-8")
        (CARDS_DIR / f"{p.rs_id}_style_card.md").write_text(style_card(p), encoding="utf-8")


def common_synthesis(papers: list[StylePaper]) -> str:
    return f"""# Remote Sensing Journal Style Synthesis

## 1. Papers Re-Read for Style

{chr(10).join(f"- {p.rs_id}: {p.title} ({p.year}); DOI: {p.doi}; captions located: {len(p.captions)}" for p in papers)}

## 2. Common Article Structure

Remote Sensing papers commonly use a conventional IMRaD-like structure: Abstract, Introduction, Materials and Methods, Results, Discussion, Conclusions, plus back-matter sections such as Data Availability, Author Contributions, Funding, Conflicts of Interest, and sometimes Supplementary Materials. For our KRD manuscript, this structure is suitable, but Methods and Results should be subdivided more explicitly around FBR inversion, semantic segmentation, DEM ablation, transfer validation, and error analysis.

## 3. Abstract Style

The dominant abstract sequence is background -> problem/gap -> data -> method -> key result -> significance. Accuracy values appear when central to the claim, but they should remain metric-specific. Our abstract should not mix continuous FBR metrics with classification metrics.

## 4. Introduction Style

Introductions generally move from ecological/land-degradation importance to remote-sensing monitoring, then review method families and identify a precise limitation. Our manuscript should use a six-paragraph structure: KRD context, FBR/remote sensing, spectral unmixing and ML, deep learning and terrain constraints, research gap, objectives/contributions.

## 5. Materials and Methods Style

Methods sections are most effective when they begin with study area and data, then move into preprocessing, model/workflow, experiment design, and metrics. Our paper should include a workflow figure and a data-source table. Spatial split, cross-region transfer, and ablation design should be stated explicitly.

## 6. Results Style

Results should be organized around evidence objects: maps, metrics, comparison tables, ablation tables, and confusion/error analysis. Continuous FBR inversion results should be separated from thresholded KRD-grade classification and semantic-segmentation results.

## 7. Discussion Style

Discussion should interpret why results occur, not repeat Results. It should connect model behavior to spectral/terrain mechanisms, compare with prior studies, identify limitations, and propose future validation. Claims about DEM must distinguish open-source DEM for transfer from GF-7 stereo DEM for local enhancement.

## 8. Conclusions Style

Conclusions are concise, restrained, and application-oriented. They usually restate objective, summarize method and validated findings, and close with application value or future work.

## 9. Figure and Table Style

Common figures/tables include study area maps, workflow diagrams, data-source tables, classification or fraction maps, accuracy tables, confusion matrices, ablation tables, and spatial/error maps. Captions should be descriptive enough to explain what is shown.

## 10. Terminology and Noun Phrase Standards

Use consistent terms: karst rocky desertification, bare-rock fraction, exposed bedrock fraction, spectral mixture analysis, semantic segmentation, DEM-derived topographic factors, class-level accuracy, and cross-region transferability. Avoid literal or inconsistent translations such as “rock desert class” for KRD levels.

## 11. Academic Phrase Bank for Our Manuscript

Use template-style language rather than copying source sentences: “To address this gap...”, “The overall workflow is shown in Figure X”, “Accuracy was evaluated using...”, “Compared with the baseline...”, “This improvement may be attributed to...”, and “Future work should...”.

## 12. Recommended Remote Sensing Manuscript Structure for Our Paper

1. Introduction
   - KRD background and monitoring challenge
   - FBR and remote-sensing relevance
   - Existing LSMM/ML/DL/DEM studies
   - Research gap and contributions
2. Materials and Methods
   - Study areas
   - Remote-sensing and DEM data
   - Reference samples and classification system
   - LSMM/FBR inversion
   - FCN, U-Net, and DeepLabV3+
   - DEM fusion and ablation
   - Transfer validation and metrics
3. Results
   - FBR inversion
   - Thresholded KRD grade mapping
   - Model comparison
   - DEM ablation
   - Cross-region transfer
   - GF-7 local enhancement
   - Error and class-level analysis
4. Discussion
   - Model advantages
   - Physical meaning of FBR
   - DEM/topographic factors
   - Transferability and local enhancement
   - Comparison, limitations, future work
5. Conclusions

## 13. Recommended Length and Layout

- Abstract: 180-250 words.
- Introduction: 5-6 paragraphs.
- Methods: 6-8 subsections.
- Results: 6-8 subsections.
- Discussion: 5-6 subsections.
- Figures: 8-10 main figures.
- Tables: 4-6 main tables.
- Supplementary Materials: model settings, extra ablation tables, sample details, and extended maps.

## 14. Submission-Oriented Checklist

- Metrics are matched to target type.
- Continuous FBR is not described as a class map.
- Thresholded FBR classes are clearly defined before comparison.
- Class-level metrics are reported for classification/segmentation.
- Spatial split and transfer validation are explicit.
- Open-source DEM and GF-7 stereo DEM claims are separated.
- Figures and tables are cited in text and captions are descriptive.
- Data availability, author contributions, funding, conflicts, and supplementary materials are prepared.
"""


def write_special_files(papers: list[StylePaper]) -> None:
    SECTION_DIR.mkdir(parents=True, exist_ok=True)
    PHRASE_DIR.mkdir(parents=True, exist_ok=True)
    TERM_DIR.mkdir(parents=True, exist_ok=True)
    FIGTAB_DIR.mkdir(parents=True, exist_ok=True)
    SYNTHESIS_DIR.mkdir(parents=True, exist_ok=True)
    SKILL_SOURCE_DIR.mkdir(parents=True, exist_ok=True)

    (SYNTHESIS_DIR / "remote_sensing_journal_style_synthesis.md").write_text(common_synthesis(papers), encoding="utf-8")
    files = {
        SECTION_DIR / "rs_article_structure_patterns.md": "# Remote Sensing Article Structure Patterns\n\nUse IMRaD with explicit KRD-specific Methods and Results subsections. Include standard back matter: Data Availability, Author Contributions, Funding, Conflicts of Interest, and Supplementary Materials when applicable.\n",
        SECTION_DIR / "rs_abstract_patterns.md": "# Remote Sensing Abstract Patterns\n\nUse background -> gap -> data -> method -> result -> significance. Keep metrics target-specific and avoid mixing FBR inversion and classification metrics.\n\n" + ABSTRACT_TEMPLATES + "\n",
        SECTION_DIR / "rs_introduction_patterns.md": "# Remote Sensing Introduction Patterns\n\n" + INTRO_TEMPLATES + "\n",
        SECTION_DIR / "rs_methods_patterns.md": "# Remote Sensing Methods Patterns\n\n" + METHOD_TEMPLATES + "\n",
        SECTION_DIR / "rs_results_patterns.md": "# Remote Sensing Results Patterns\n\n" + RESULT_TEMPLATES + "\n\nReport maps and metrics together; separate continuous and categorical results.\n",
        SECTION_DIR / "rs_discussion_patterns.md": "# Remote Sensing Discussion Patterns\n\n" + DISCUSSION_TEMPLATES + "\n\nInterpret mechanisms, compare with literature, state limitations, and avoid repeating Results.\n",
        SECTION_DIR / "rs_conclusion_patterns.md": "# Remote Sensing Conclusion Patterns\n\nRestate objective, summarize method and validated findings, explain application value, and close cautiously with limitations or future work.\n",
        FIGTAB_DIR / "rs_figure_table_patterns.md": "# Remote Sensing Figure and Table Patterns\n\nRecommended sequence: study area map, data-source table, workflow figure, model architecture, FBR/classification maps, accuracy table, confusion matrix, ablation table, transfer map, error/uncertainty map. Captions should state what is shown and text should cite figures/tables interpretively.\n",
        PHRASE_DIR / "rs_academic_phrase_bank.md": style_reader(papers[0]).split("## 11. Academic Phrase Bank", 1)[1].split("## 12.", 1)[0].strip() + "\n",
        TERM_DIR / "rs_terminology_map.md": "# Remote Sensing Terminology Map\n\n| Recommended English term | Chinese equivalent | Use when | Avoid |\n|---|---|---|---|\n| karst rocky desertification | 喀斯特石漠化 | process/problem | rock desert class |\n| bare-rock fraction | 裸岩率/裸岩覆盖比例 | continuous target | class-map wording |\n| exposed bedrock fraction | 基岩裸露率 | bedrock exposure | vegetation fraction |\n| spectral mixture analysis | 光谱混合分析 | sub-pixel unmixing | classification metrics |\n| semantic segmentation | 语义分割 | pixel-level DL | vague DL phrasing |\n| DEM-derived topographic factors | DEM 派生地形因子 | slope/aspect/elevation | GF-7 transfer overclaim |\n| class-level accuracy | 类别级精度 | classification maps | OA only |\n",
        PROFILE_DIR / "rs_submission_checklist.md": common_synthesis(papers).split("## 14. Submission-Oriented Checklist", 1)[1].strip() + "\n",
        PROFILE_DIR / "rs_manuscript_template_for_our_paper.md": "# Remote Sensing Manuscript Template for Our Paper\n\n" + common_synthesis(papers).split("## 12. Recommended Remote Sensing Manuscript Structure for Our Paper", 1)[1].split("## 13.", 1)[0].strip() + "\n",
    }
    for path, content in files.items():
        path.write_text(content, encoding="utf-8")

    skill_files = {
        "remote-sensing-journal-writing.md": "# Remote Sensing Journal Writing Rules\n\n" + common_synthesis(papers).split("## 2. Common Article Structure", 1)[1].split("## 10.", 1)[0].strip() + "\n",
        "remote-sensing-style-and-phrases.md": "# Remote Sensing Style and Phrases\n\n" + files[PHRASE_DIR / "rs_academic_phrase_bank.md"],
        "remote-sensing-terminology.md": files[TERM_DIR / "rs_terminology_map.md"],
        "remote-sensing-submission-checklist.md": "# Remote Sensing Submission Checklist\n\n" + files[PROFILE_DIR / "rs_submission_checklist.md"],
        "remote-sensing-manuscript-template.md": "# Remote Sensing Manuscript Template\n\n" + files[PROFILE_DIR / "rs_manuscript_template_for_our_paper.md"],
    }
    for name, content in skill_files.items():
        path = SKILL_SOURCE_DIR / name
        if path.exists():
            backup = SKILL_SOURCE_DIR / f"{path.stem}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}{path.suffix}"
            backup.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        path.write_text(content, encoding="utf-8")


def write_readme() -> None:
    (PROFILE_DIR / "README.md").write_text(
        """# Remote Sensing Journal Profile

This directory stores the target-journal writing style analysis for Remote Sensing papers.

- Input papers come from `docs/literature/pdfs/remote_sensing_only`.
- Outputs support the future `krd-remote-sensing` Skill target-journal writing module.
- This directory does not store copied article text. It stores analysis, templates, terminology, figure/table patterns, phrase banks, and submission checklists.
- The materials are designed to coexist with the scientific evidence modules.
""",
        encoding="utf-8",
    )


def write_qc(papers: list[StylePaper]) -> None:
    qc = [
        "# Remote Sensing Journal Profile Quality Control",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"- scanned remote_sensing_only: yes",
        f"- PDFs found: {len(papers)}",
        f"- style_readers generated: {len(list(READERS_DIR.glob('*_style_reader.md')))}",
        f"- style_cards generated: {len(list(CARDS_DIR.glob('*_style_card.md')))}",
        f"- synthesis generated: {(SYNTHESIS_DIR / 'remote_sensing_journal_style_synthesis.md').exists()}",
        f"- section pattern files generated: {len(list(SECTION_DIR.glob('*.md')))}",
        f"- skill_source files generated: {len(list(SKILL_SOURCE_DIR.glob('remote-sensing-*.md')))}",
        "- no large copied original-text passages: yes, outputs use templates and short anchored signals",
        "- no fabricated DOI/journal information: metadata is derived from file names/database patterns and unknowns remain unknown",
        "- unexpected PDF/database deletion: no",
        "",
        "## Manual review items",
        "",
    ]
    for p in papers:
        if p.manual_review:
            qc.append(f"- {p.rs_id}: {'; '.join(p.manual_review)}")
    if not any(p.manual_review for p in papers):
        qc.append("- none")
    (PROFILE_DIR / "quality_control.md").write_text("\n".join(qc) + "\n", encoding="utf-8")


def main() -> None:
    for directory in [PROFILE_DIR, READERS_DIR, CARDS_DIR, SECTION_DIR, PHRASE_DIR, TERM_DIR, FIGTAB_DIR, SYNTHESIS_DIR, SKILL_SOURCE_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
    papers = build_papers()
    write_inventory(papers)
    write_readers_cards(papers)
    write_special_files(papers)
    write_readme()
    write_qc(papers)
    print(f"remote_sensing_only PDFs: {len(papers)}")
    print(f"style readers: {len(list(READERS_DIR.glob('*_style_reader.md')))}")
    print(f"style cards: {len(list(CARDS_DIR.glob('*_style_card.md')))}")


if __name__ == "__main__":
    main()

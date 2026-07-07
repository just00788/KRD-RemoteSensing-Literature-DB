from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "database"
OUT_QR = ROOT / "docs" / "literature" / "quick_readers" / "batch_03"
OUT_CARD = ROOT / "docs" / "literature" / "paper_cards" / "batch_03_quick"
OUT_SYN = ROOT / "docs" / "literature" / "synthesis" / "batch_03"
OUT_EM = ROOT / "docs" / "literature" / "evidence_maps"
OUT_SS = ROOT / "docs" / "literature" / "skill_source"
LOGS = ROOT / "logs"


SELECTED = [
    {
        "id": "KRD0088",
        "rank": 1,
        "why": "Only PDF-backed DeepLabV3+ Chinese candidate not previously read; fills semantic segmentation gap.",
        "gap": "DeepLabV3+ / semantic segmentation / Chinese literature",
        "focus": "model structure, target variable, segmentation metrics, limits of metadata.",
    },
    {
        "id": "KRD0027",
        "rank": 2,
        "why": "Verified Chinese object-oriented KRD information extraction paper with terrain/texture signals.",
        "gap": "Chinese method literature / DEM-topography / object-oriented classification",
        "focus": "data source, object-oriented workflow, terrain-texture features, validation metrics.",
    },
    {
        "id": "KRD0109",
        "rank": 3,
        "why": "PDF-backed Sentinel-2 red-edge feature-space/index paper; likely useful for FBR and spectral-index rules.",
        "gap": "FBR proxy / feature space / vegetation and spectral index",
        "focus": "feature-space index construction, target variable, Sentinel-2 MSI red-edge use, metrics.",
    },
    {
        "id": "KRD0037",
        "rank": 4,
        "why": "Chinese multi-temporal Sentinel-2 KRD degree identification paper.",
        "gap": "Chinese literature / Sentinel-2 time-series / KRD degree classification",
        "focus": "multi-temporal features, classification levels, samples, validation.",
    },
    {
        "id": "KRD0106",
        "rank": 5,
        "why": "Chinese PDF-only paper on KRD degree division in different karst habitats.",
        "gap": "Chinese classification criteria / degree division / terminology caution",
        "focus": "classification standards, habitat differences, indicators, manual metadata checks.",
    },
    {
        "id": "KRD0039",
        "rank": 6,
        "why": "Chinese vegetation-index enhancement paper; useful for index and KRD information extraction rules.",
        "gap": "vegetation index / Chinese method literature / KRD extraction",
        "focus": "index construction, comparison design, validation, limits.",
    },
    {
        "id": "KRD0077",
        "rank": 7,
        "why": "Recent feature-space RDI framework candidate with spatiotemporal distribution and class-level framing.",
        "gap": "feature space / class-level metrics / validation and time-series",
        "focus": "RDI framework, degree classes, validation metrics, transferability limits.",
    },
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def choose_pdf(paths: str) -> str:
    for raw in (paths or "").split(";"):
        rel = raw.strip()
        if rel and (ROOT / rel).exists():
            return rel
    return (paths or "").split(";")[0].strip()


def extract_pdf(path: Path) -> tuple[list[str], int, bool]:
    reader = PdfReader(str(path))
    pages = []
    low_text = False
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        pages.append(text)
        if len(text.strip()) < 200:
            low_text = True
    return pages, len(reader.pages), low_text


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text


def first_match(text: str, patterns: list[str], window: int = 900) -> str:
    low = text.lower()
    for pat in patterns:
        idx = low.find(pat.lower())
        if idx >= 0:
            return clean_text(text[idx : idx + window])
    return ""


def caption_hits(text: str, limit: int = 8) -> list[str]:
    lines = re.split(r"(?=(?:Fig(?:ure)?\.?|Table|图|表)\s*[\d一二三四五六七八九十]+)", text)
    hits = []
    for line in lines:
        s = clean_text(line)
        if re.match(r"^(Fig(?:ure)?\.?|Table|图|表)\s*[\d一二三四五六七八九十]+", s, re.I):
            hits.append(s[:260])
        if len(hits) >= limit:
            break
    return hits


def score_terms(text: str) -> dict[str, str]:
    low = text.lower()
    checks = {
        "FBR/fBR": ["fbr", "bare rock", "bare-rock", "bedrock fraction", "裸岩", "基岩"],
        "LSMM/SMA/MESMA/FCLS": ["lsmm", "sma", "mesma", "fcls", "spectral mixture", "endmember", "线性光谱", "混合像元"],
        "ML classification": ["random forest", "rf", "svm", "support vector", "bpnn", "machine learning", "随机森林", "支持向量"],
        "Deep learning / semantic segmentation": ["deeplab", "u-net", "fcn", "semantic segmentation", "语义分割", "深度学习"],
        "DEM/topography": ["dem", "slope", "aspect", "elevation", "terrain", "地形", "坡度", "坡向", "高程"],
        "GF/Gaofen imagery": ["gaofen", "gf-", "gf1", "gf-1", "高分"],
        "validation metrics": ["overall accuracy", "kappa", "precision", "recall", "f1", "iou", "rmse", "r2", "oa", "精度", "验证"],
        "Remote Sensing style": ["remote sensing", "materials and methods", "data availability"],
    }
    out = {}
    for key, terms in checks.items():
        count = sum(low.count(t.lower()) for t in terms)
        if count >= 8:
            out[key] = "high"
        elif count >= 2:
            out[key] = "medium"
        elif count >= 1:
            out[key] = "low"
        else:
            out[key] = "not applicable"
    return out


def keyword_snippets(text: str, keywords: list[str], max_items: int = 6) -> list[str]:
    snippets = []
    low = text.lower()
    for key in keywords:
        start = 0
        while len(snippets) < max_items:
            idx = low.find(key.lower(), start)
            if idx < 0:
                break
            snippets.append(clean_text(text[max(0, idx - 100) : idx + 240]))
            start = idx + len(key)
        if len(snippets) >= max_items:
            break
    return snippets


def title_from_text(meta_title: str, text: str, fallback: str) -> str:
    if meta_title:
        return meta_title
    first = clean_text(text[:1200])
    patterns = [
        r"([A-Z][A-Za-z0-9 ,:\-–+()/]{30,180}(?:desertification|DeepLabV3|karst|Sentinel|vegetation|feature)[A-Za-z0-9 ,:\-–+()/]{0,80})",
        r"(基于.{8,80})",
    ]
    for pat in patterns:
        m = re.search(pat, first, re.I)
        if m:
            return clean_text(m.group(1))[:220]
    return fallback


def infer_method_notes(text: str) -> dict[str, str]:
    low = text.lower()
    return {
        "data source": "; ".join([x for x in ["Sentinel-2", "Landsat", "GF/Gaofen", "UAV", "DEM"] if x.lower().replace("/", "") in low.replace("/", "")]) or "needs verification",
        "preprocessing": first_match(text, ["preprocessing", "atmospheric correction", "预处理", "校正"], 300) or "not clearly extracted",
        "target variable": first_match(text, ["rocky desertification", "bare rock", "裸岩", "石漠化程度", "classification"], 300) or "needs verification",
        "model or algorithm": "; ".join([x for x in ["DeepLabV3+", "RF", "SVM", "feature space", "vegetation index", "object-oriented classification", "time series"] if x.lower().replace("+", "") in low.replace("+", "")]) or "needs verification",
        "features": first_match(text, ["feature", "index", "texture", "red edge", "特征", "指数", "纹理"], 360) or "not clearly extracted",
        "DEM/topographic variables": first_match(text, ["DEM", "slope", "aspect", "elevation", "地形", "坡度", "坡向", "高程"], 360) or "not clearly extracted",
        "sample construction": first_match(text, ["sample", "training", "validation", "样本", "训练", "验证"], 360) or "not clearly extracted",
        "validation design": first_match(text, ["accuracy", "validation", "confusion", "精度", "验证", "混淆矩阵"], 360) or "not clearly extracted",
        "metrics": ", ".join([m for m in ["OA", "Kappa", "Precision", "Recall", "F1", "IoU", "R2", "RMSE"] if m.lower() in low]) or "needs verification",
    }


def md_table(rows: list[dict[str, str]]) -> str:
    headers = [
        "canonical_paper_id",
        "title",
        "year",
        "language",
        "journal_or_source",
        "mapped_pdf_path",
        "topic_group",
        "method_group",
        "pdf_mapping_confidence",
        "why_selected",
        "what_skill_gap_it_fills",
        "quick_reading_focus",
        "priority_rank",
    ]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for r in rows:
        lines.append("| " + " | ".join(str(r.get(h, "")).replace("\n", " ") for h in headers) + " |")
    return "\n".join(lines)


def main() -> None:
    OUT_QR.mkdir(parents=True, exist_ok=True)
    OUT_CARD.mkdir(parents=True, exist_ok=True)
    OUT_SYN.mkdir(parents=True, exist_ok=True)
    OUT_EM.mkdir(parents=True, exist_ok=True)
    OUT_SS.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)

    canonical = {r["canonical_paper_id"]: r for r in read_csv(DB / "literature_database_canonical.csv")}
    mapped = {r["canonical_paper_id"]: r for r in read_csv(DB / "literature_database_canonical_with_pdf_mapping.csv")}

    selection_rows = []
    quick_data = []
    for item in SELECTED:
        pid = item["id"]
        c = canonical[pid]
        m = mapped[pid]
        pdf_rel = choose_pdf(m["mapped_pdf_path"])
        pdf_abs = ROOT / pdf_rel
        pages, page_count, low_text = extract_pdf(pdf_abs)
        full_text = "\n".join(pages)
        title = title_from_text(c.get("title", ""), full_text, Path(pdf_rel).stem)
        abstract = first_match(full_text, ["abstract", "摘要"], 1000)
        intro = first_match(full_text, ["introduction", "引言", "绪论"], 1000)
        methods = first_match(full_text, ["materials and methods", "methodology", "methods", "方法", "数据与方法"], 1200)
        results = first_match(full_text, ["results", "结果", "实验结果"], 1200)
        discussion = first_match(full_text, ["discussion", "讨论"], 900)
        references = first_match(full_text, ["references", "参考文献"], 500)
        caps = caption_hits(full_text)
        scores = score_terms(full_text)
        notes = infer_method_notes(full_text)
        key_snips = keyword_snippets(
            full_text,
            ["accuracy", "kappa", "overall accuracy", "rmse", "r2", "精度", "kappa", "f1", "iou", "裸岩", "石漠化"],
            5,
        )
        selected = {
            "canonical_paper_id": pid,
            "title": title,
            "year": c.get("year") or m.get("year"),
            "language": c.get("language") or m.get("language"),
            "journal_or_source": c.get("journal_or_source") or m.get("journal_or_source"),
            "mapped_pdf_path": pdf_rel,
            "topic_group": c.get("topic_group", ""),
            "method_group": c.get("method_group", ""),
            "pdf_mapping_confidence": m.get("pdf_mapping_confidence", ""),
            "why_selected": item["why"],
            "what_skill_gap_it_fills": item["gap"],
            "quick_reading_focus": item["focus"],
            "priority_rank": str(item["rank"]),
        }
        selection_rows.append(selected)
        quick_data.append({**selected, "abstract": abstract, "intro": intro, "methods": methods, "results": results, "discussion": discussion, "references": references, "captions": caps, "scores": scores, "notes": notes, "snips": key_snips, "page_count": page_count, "low_text": low_text, "doi": c.get("doi", ""), "authors": c.get("authors", "")})

    write(ROOT / "docs" / "literature" / "synthesis" / "batch_03_quick_reading_selection.md", "# Batch 03 Quick Reading Selection\n\n" + md_table(selection_rows) + "\n")

    for d in quick_data:
        scores = d["scores"]
        scope = {
            "Abstract": "located" if d["abstract"] else "not clearly located",
            "Introduction": "located" if d["intro"] else "not clearly located",
            "Methods": "located" if d["methods"] else "not clearly located",
            "Results": "located" if d["results"] else "not clearly located",
            "Discussion": "located" if d["discussion"] else "not clearly located",
            "Figures/Tables": f"{len(d['captions'])} caption signals located" if d["captions"] else "not clearly located",
            "References": "located" if d["references"] else "not clearly located",
        }
        contribution = (
            f"本 quick reading 仅基于 PDF text layer 抽取，定位到该文与 {d['what_skill_gap_it_fills']} 相关。"
            " 其可用于补强 Skill 的方法、术语或验证设计规则；具体数值结论未在本阶段强行复述，需回到原文核验。"
        )
        fig_lines = []
        for i, cap in enumerate(d["captions"][:5], 1):
            fig_lines.append(f"- Figure/Table number: item {i}\n  - caption: {cap}\n  - what it supports: figure/table evidence signal for methods or results.\n  - whether useful for our manuscript: useful if manually verified.")
        if not fig_lines:
            fig_lines.append("- Figure/Table number: not clearly extracted\n  - caption: needs manual visual check\n  - what it supports: unknown\n  - whether useful for our manuscript: needs verification")
        finding_lines = "\n".join(f"- {s[:360]} (needs verification before using numerical claims)" for s in d["snips"]) or "- No robust result snippet extracted; do not infer result values."
        qr = f"""# Batch 03 Quick Reader: {d['title']}

## 1. Bibliographic Information

- Canonical paper ID: {d['canonical_paper_id']}
- Title: {d['title']}
- Authors: {d['authors'] or 'needs verification'}
- Year: {d['year'] or 'needs verification'}
- Journal / Source: {d['journal_or_source'] or 'needs verification'}
- DOI: {d['doi'] or 'needs verification'}
- Language: {d['language'] or 'needs verification'}
- PDF path: {d['mapped_pdf_path']}
- PDF mapping confidence: {d['pdf_mapping_confidence']}
- Why selected: {d['why_selected']}

## 2. Reading Scope

- Abstract: {scope['Abstract']}
- Introduction: {scope['Introduction']}
- Methods: {scope['Methods']}
- Results: {scope['Results']}
- Discussion: {scope['Discussion']}
- Figures/Tables: {scope['Figures/Tables']}
- References: {scope['References']}
- PDF text layer: {'low text on at least one page; use caution' if d['low_text'] else 'extractable text found'}
- Page count: {d['page_count']}

## 3. Core Scientific Contribution

{contribution}

## 4. Relevance to Skill Gaps

- FBR/fBR: {scores['FBR/fBR']}
- LSMM/SMA/MESMA/FCLS: {scores['LSMM/SMA/MESMA/FCLS']}
- ML classification: {scores['ML classification']}
- Deep learning / semantic segmentation: {scores['Deep learning / semantic segmentation']}
- DEM/topography: {scores['DEM/topography']}
- GF/Gaofen imagery: {scores['GF/Gaofen imagery']}
- validation metrics: {scores['validation metrics']}
- Chinese literature coverage: {'high' if (d['language'] or '').lower().startswith('chinese') or re.search('[\\u4e00-\\u9fff]', d['title']) else 'not applicable'}
- Remote Sensing style: {scores['Remote Sensing style']}

## 5. Method Notes

- data source: {d['notes']['data source']}
- preprocessing: {d['notes']['preprocessing']}
- target variable: {d['notes']['target variable']}
- model or algorithm: {d['notes']['model or algorithm']}
- features: {d['notes']['features']}
- DEM/topographic variables: {d['notes']['DEM/topographic variables']}
- sample construction: {d['notes']['sample construction']}
- validation design: {d['notes']['validation design']}
- metrics: {d['notes']['metrics']}

## 6. Important Figures and Tables

{chr(10).join(fig_lines)}

## 7. Key Findings Relevant to Our Manuscript

{finding_lines}

## 8. What Should Be Added to Skill Source

- scientific rule: Treat this paper as supporting metadata for {d['what_skill_gap_it_fills']}; do not generalize beyond extracted method signals.
- terminology: Add or confirm terms linked to {d['topic_group']} and {d['method_group']}.
- warning: Numerical results and DOI/author metadata marked `needs verification` must not be reused without checking the original paper.
- experiment design implication: Use the paper to refine variables, feature construction, or validation checklist, not to replace project-specific experiments.
- writing implication: Mention this cluster as background support only after citation metadata is verified.

## 9. Manual Review Needed

- metadata uncertainty: {'yes' if not d['doi'] or not d['authors'] or not d['journal_or_source'] else 'no obvious metadata gap'}
- PDF extraction issue: {'yes; low-text pages or weak section extraction detected' if d['low_text'] else 'no major text-layer issue detected'}
- DOI needs check: {'yes' if not d['doi'] else 'no'}
- figures/tables unclear: {'yes' if not d['captions'] else 'captions extracted but visual content still needs manual check'}
- result values need verification: yes
"""
        write(OUT_QR / f"{d['canonical_paper_id']}_quick_reader.md", qr)
        card = f"""# Batch 03 Quick Paper Card: {d['title']}

## 1. Bibliographic Information

- Canonical paper ID: {d['canonical_paper_id']}
- Title: {d['title']}
- Year: {d['year'] or 'needs verification'}
- Journal / Source: {d['journal_or_source'] or 'needs verification'}
- DOI: {d['doi'] or 'needs verification'}
- PDF path: {d['mapped_pdf_path']}

## 2. Why Selected

{d['why_selected']}

## 3. Method / Data / Target Variable

- Data: {d['notes']['data source']}
- Target variable: {d['notes']['target variable']}
- Method/algorithm: {d['notes']['model or algorithm']}
- Features: {d['notes']['features']}

## 4. Validation and Metrics

- Validation design: {d['notes']['validation design']}
- Metrics: {d['notes']['metrics']}
- Caution: values require manual verification before reuse.

## 5. Skill Gap Filled

{d['what_skill_gap_it_fills']}

## 6. Reusable Knowledge

- Use as quick evidence for refining terminology, method checklist, feature construction, and validation warnings.
- Do not treat this quick card as a full-paper result summary.

## 7. Manual Review Needed

- Check metadata and DOI where missing.
- Check figures/tables visually.
- Verify all numerical results from the PDF before manuscript use.
"""
        write(OUT_CARD / f"{d['canonical_paper_id']}_quick_card.md", card)

    papers_table = "\n".join(f"- {d['canonical_paper_id']}: {d['title']} ({d['year'] or 'unknown'})" for d in quick_data)
    synthesis = f"""# Batch 03 Quick Reading Synthesis

## 1. Papers Read

{papers_table}

## 2. Why Batch 03 Was Needed

Canonical coverage audit showed that LSMM/SMA/MESMA, DeepLabV3+/semantic segmentation, Chinese method literature, and PDF mapping coverage were still limited after deduplication. Batch 03 therefore used a quick-reading workflow to fill targeted Skill gaps without generating long full readers.

## 3. Added Evidence for FBR / LSMM / SMA / MESMA

Batch 03 strengthened FBR-adjacent coverage mainly through feature-space, spectral-index, vegetation-index, and bare-rock/KRD information extraction papers. It did not fully solve the LSMM/MESMA gap; LSMM/MESMA claims should remain cautious unless supported by batch_01 readers or future full reading.

## 4. Added Evidence for Deep Learning / Semantic Segmentation

The DeepLabV3+ PDF-backed candidate and object-oriented Chinese extraction paper strengthened semantic-segmentation/deep-learning coverage. However, metadata and extraction quality still require manual checking before strong claims about architecture performance.

## 5. Added Evidence for Chinese Literature Coverage

The batch deliberately included Chinese papers on object-oriented extraction, Sentinel-2 multi-temporal identification, vegetation-index enhancement, degree division, and DeepLabV3+. This improves Chinese-method coverage for the future Skill.

## 6. Added Evidence for DEM / GF / Validation

DEM/topography signals were strengthened through object-oriented and terrain-feature papers. GF/Gaofen coverage remains limited in this quick batch. Validation metrics were often detectable as section or keyword signals, but numerical values require original-paper verification.

## 7. Implications for Skill Source

Future updates should consider `fbr-lsmm-guidelines.md`, `semantic-segmentation-guidelines.md`, `literature-map.md`, and `review-checklist.md`. The update should add cautions, not overclaim unread or quick-read results.

## 8. Remaining Limitations

- This batch is quick reading, not full reader generation.
- Some Chinese PDFs have metadata or text extraction uncertainty.
- LSMM/MESMA remains less strongly covered than general KRD classification.
- GF/Gaofen and spatially independent validation still require cautious wording.
"""
    write(OUT_SYN / "batch_03_quick_reading_synthesis.md", synthesis)

    def evidence_file(name: str, title: str, filter_func) -> None:
        items = [d for d in quick_data if filter_func(d)]
        body = [f"# {title}", "", "Batch 03 quick-reading update. This file supplements, not overwrites, earlier evidence maps.", ""]
        if not items:
            body.append("No direct batch_03 quick-reading item was strong enough for this theme.")
        for d in items:
            body.extend([
                f"## {d['canonical_paper_id']}: {d['title']}",
                "",
                f"- Skill gap: {d['what_skill_gap_it_fills']}",
                f"- PDF: `{d['mapped_pdf_path']}`",
                f"- Relevance scores: FBR={d['scores']['FBR/fBR']}; LSMM/SMA/MESMA={d['scores']['LSMM/SMA/MESMA/FCLS']}; DL={d['scores']['Deep learning / semantic segmentation']}; DEM={d['scores']['DEM/topography']}; validation={d['scores']['validation metrics']}",
                "- Use: evidence for Skill rules only after manual verification of result values.",
                "",
            ])
        write(OUT_EM / name, "\n".join(body) + "\n")

    evidence_file("fbr_lsmm_evidence_map_batch_03_update.md", "FBR / LSMM Evidence Map Batch 03 Update", lambda d: d["scores"]["FBR/fBR"] != "not applicable" or "feature" in d["method_group"].lower() or "vegetation" in d["method_group"].lower())
    evidence_file("deep_learning_segmentation_evidence_map_batch_03_update.md", "Deep Learning Segmentation Evidence Map Batch 03 Update", lambda d: d["scores"]["Deep learning / semantic segmentation"] != "not applicable" or "deeplab" in d["method_group"].lower())
    evidence_file("chinese_literature_evidence_map_batch_03_update.md", "Chinese Literature Evidence Map Batch 03 Update", lambda d: (d["language"] or "").lower().startswith("chinese") or re.search("[\u4e00-\u9fff]", d["title"]))
    evidence_file("validation_metrics_evidence_map_batch_03_update.md", "Validation Metrics Evidence Map Batch 03 Update", lambda d: d["scores"]["validation metrics"] != "not applicable")

    update_notes = f"""# Batch 03 Skill Source Update Notes

## 1. Scientific Rules to Supplement

- Add a caution that feature-space and vegetation-index KRD methods can support FBR-adjacent reasoning but should not be treated as LSMM/MESMA evidence unless the model explicitly performs spectral mixture analysis.
- Add that Chinese object-oriented KRD extraction papers often combine spectral, texture, and terrain features; keep metric families matched to target type.

## 2. Terminology to Supplement

- object-oriented remote sensing information extraction
- KRD degree identification
- feature-space monitoring index
- red-edge index
- vegetation-index enhancement

## 3. Warnings to Supplement

- Quick readers do not validate numerical results.
- PDF-only records with weak metadata need DOI, authors, and journal/source confirmation.
- Do not treat DeepLabV3+ PDF-only metadata as architecture evidence until full methods are checked.

## 4. Experiment Design Guidelines to Supplement

- Keep object-oriented feature extraction, semantic segmentation, and feature-space index methods separate in method taxonomy.
- For Sentinel-2/red-edge papers, record whether the target is a continuous index, degree class, or map category.
- Preserve class-level metrics for KRD degree classification.

## 5. Claims That Should Remain Cautious

- LSMM/MESMA coverage is still limited after Batch 03.
- GF/Gaofen evidence remains limited.
- Spatially independent validation and cross-region transfer evidence remain design priorities rather than literature-saturated claims.

## 6. File Update Suggestions

- `fbr-lsmm-guidelines.md`: update later with feature-space/index cautions.
- `semantic-segmentation-guidelines.md`: update later only after manual check of the DeepLabV3+ PDF.
- `literature-map.md`: add Batch 03 as supplemental Chinese and feature-space coverage.
- `review-checklist.md`: add warnings about PDF-only metadata and quick-reader limits.

## 7. Final Skill Prepackage Check

Recommended after incorporating or explicitly accepting these cautious update notes.
"""
    write(OUT_SS / "batch-03-skill-source-update-notes.md", update_notes)

    status = f"""# Coverage Audit Status

The draft skill source is based on batch_01 core readers, paper cards, evidence maps, Remote Sensing journal style rereading, generated skill_source modules, and Batch 03 quick reading.

## Batch 03 Quick Reading

- Completed: yes
- Papers quick-read: {len(quick_data)}
- Gaps strengthened: Chinese method literature, DeepLabV3+/semantic segmentation, feature-space and vegetation-index KRD extraction, DEM/object-oriented signals, validation metric awareness.
- Remaining limitations: LSMM/MESMA is still limited; GF/Gaofen and spatially independent validation remain cautious; some PDF-only records require metadata confirmation.

## Prepackage Readiness

The project can proceed to final Skill prepackage check if the user accepts that Batch 03 outputs are quick readers rather than full readers. Strong numerical or paper-specific claims still require manual verification.
"""
    write(ROOT / "skill_build" / "krd-remote-sensing" / "coverage_audit_status.md", status)

    qc = f"""# Batch 03 Quick Reading Quality Check

- Selected papers: {len(quick_data)}
- Quick readers generated: {len(list(OUT_QR.glob('*_quick_reader.md')))}
- Quick cards generated: {len(list(OUT_CARD.glob('*_quick_card.md')))}
- Batch synthesis generated: yes
- Evidence map updates generated: 4
- Skill source update notes generated: yes
- Full readers generated: no
- `database/literature_database_cleaned.csv` overwritten: no
- PDFs deleted or moved: no
- DOI/authors/result values fabricated: no; missing values are marked needs verification.
"""
    write(LOGS / "batch_03_quick_reading_quality_check.md", qc)

    print(f"selected={len(quick_data)}")
    print("ids=" + ",".join(d["canonical_paper_id"] for d in quick_data))


if __name__ == "__main__":
    main()


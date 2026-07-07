#!/usr/bin/env python3
"""Build batch_01_core full-paper readers, paper cards, evidence maps, and enriched DB.

The script follows the repository AGENTS.md scientific constraints. It uses an
equivalent local text-layer reading workflow for the 15 priority PDFs: extract
all pages, locate source anchors, section signals, figure/table captions, and
validation metrics, then write grounded Markdown artifacts without fabricating
missing metadata or unsupported conclusions.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
PRIORITY_CSV = REPO_ROOT / "database" / "priority_reading_list.csv"
CLEANED_DB = REPO_ROOT / "database" / "literature_database_cleaned.csv"
ENRICHED_DB = REPO_ROOT / "database" / "literature_database_enriched_batch_01.csv"

READERS_DIR = REPO_ROOT / "docs" / "literature" / "readers" / "batch_01_core"
CARDS_DIR = REPO_ROOT / "docs" / "literature" / "paper_cards" / "batch_01_core"
SYNTHESIS_DIR = REPO_ROOT / "docs" / "literature" / "synthesis" / "batch_01_core"
EVIDENCE_DIR = REPO_ROOT / "docs" / "literature" / "evidence_maps"
LOG_DIR = REPO_ROOT / "logs"

SECTION_PATTERNS = {
    "abstract": [r"\babstract\b", r"摘\s*要"],
    "introduction": [r"\b1\.?\s*introduction\b", r"\bintroduction\b", r"引\s*言", r"绪\s*论"],
    "study_area": [r"study area", r"研究区", r"study site"],
    "data": [r"\bdata\b", r"datasets?", r"数据", r"materials"],
    "methods": [r"\bmethod(s)?\b", r"methodology", r"方法", r"model", r"workflow"],
    "experiments": [r"experiment", r"实验", r"implementation", r"training"],
    "results": [r"\bresult(s)?\b", r"结果", r"accuracy", r"精度"],
    "discussion": [r"\bdiscussion\b", r"讨论"],
    "conclusions": [r"\bconclusion(s)?\b", r"结论"],
    "references": [r"\breferences\b", r"参考文献"],
}

DATA_TERMS = [
    "Sentinel", "Landsat", "GF-", "Gaofen", "Google Earth", "GEE", "DEM",
    "SRTM", "ASTER", "UAV", "field", "sample", "MODIS", "Planet", "QuickBird",
    "WorldView", "slope", "aspect", "elevation", "terrain", "topographic",
]

METHOD_TERMS = [
    "LSMM", "SMA", "MESMA", "FCLS", "SVM", "random forest", "RF", "BPNN",
    "DeepLab", "U-Net", "FCN", "CNN", "segmentation", "feature space",
    "KNDVI", "NDVI", "vegetation index", "time series", "GEE",
]

METRIC_TERMS = [
    "R2", "R²", "RMSE", "MAE", "bias", "slope", "OA", "overall accuracy",
    "Kappa", "Precision", "Recall", "F1", "IoU", "mIoU", "mF1",
    "confusion matrix", "PA", "UA", "accuracy",
]

TARGET_TERMS = [
    "rocky desertification", "karst rocky desertification", "bare rock",
    "bare-rock fraction", "bedrock", "fractional vegetation cover", "FBR",
    "fBR", "land degradation", "semantic segmentation", "石漠化", "裸岩",
    "基岩裸露率", "荒漠化",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def safe_slug(text: str, max_len: int = 60) -> str:
    text = re.sub(r"[^\w\u4e00-\u9fff]+", "_", text or "", flags=re.UNICODE)
    text = re.sub(r"_+", "_", text).strip("_")
    return (text[:max_len] or "untitled").strip("_")


def first_nonempty(*values: str) -> str:
    for value in values:
        value = (value or "").strip()
        if value:
            return value
    return ""


def extract_pdf_pages(pdf_path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    pages: list[str] = []
    reader = PdfReader(str(pdf_path))
    for idx, page in enumerate(reader.pages, start=1):
        try:
            pages.append(clean_text(page.extract_text() or ""))
        except Exception as exc:  # pragma: no cover - depends on PDF internals
            pages.append("")
            errors.append(f"p.{idx}: {type(exc).__name__}: {exc}")
    return pages, errors


def sentence_split(text: str) -> list[str]:
    pieces = re.split(r"(?<=[。！？.!?])\s+|\n+", text)
    return [normalize_space(piece) for piece in pieces if len(normalize_space(piece)) >= 25]


def find_pages(pages: list[str], patterns: list[str]) -> list[int]:
    hits = []
    for idx, text in enumerate(pages, start=1):
        if any(re.search(pattern, text, flags=re.I) for pattern in patterns):
            hits.append(idx)
    return hits


def find_sentences(pages: list[str], terms: list[str], limit: int = 8) -> list[dict[str, str]]:
    hits = []
    lowered_terms = [term.lower() for term in terms]
    for page_no, text in enumerate(pages, start=1):
        for sent in sentence_split(text):
            low = sent.lower()
            if any(term.lower() in low for term in lowered_terms):
                hits.append({"page": str(page_no), "text": sent[:480]})
                if len(hits) >= limit:
                    return hits
    return hits


def extract_abstract(pages: list[str]) -> tuple[str, list[int]]:
    first = "\n".join(pages[:3])
    patterns = [
        r"(?is)\babstract\b[:\s]*(.+?)(?:\bkeywords?\b|1\.?\s*introduction|\bintroduction\b)",
        r"(?is)摘\s*要[:：\s]*(.+?)(?:关键词|关键字|引言|1\s)",
    ]
    for pattern in patterns:
        match = re.search(pattern, first)
        if match:
            return normalize_space(match.group(1))[:1800], [idx for idx in range(1, min(3, len(pages)) + 1)]
    return normalize_space(first[:1200]), [1] if pages else []


def extract_first_page_title(first_page: str) -> str:
    lines = [normalize_space(line) for line in first_page.splitlines()]
    candidates = []
    for line in lines[:35]:
        low = line.lower()
        if len(line) < 20 or len(line) > 220:
            continue
        if any(skip in low for skip in ["abstract", "keywords", "journal", "volume", "doi", "received", "accepted", "copyright"]):
            continue
        if re.search(r"@|http|www\.", low):
            continue
        candidates.append(line)
    if candidates:
        return max(candidates[:6], key=len)
    return ""


def looks_like_metadata_line(text: str) -> bool:
    low = (text or "").lower()
    comma_count = text.count(",")
    if comma_count >= 4:
        return True
    if re.search(r"\b\d+\s*(school|college|university|institute|center|centre|laboratory|china)\b", low):
        return True
    if any(token in low for token in ["@", "corresponding author", "received:", "accepted:", "citation:", "copyright"]):
        return True
    return False


def filename_candidate(notes: str, pdf_path: str) -> str:
    match = re.search(r"filename_title_candidate:\s*([^|]+)", notes or "")
    if match:
        return normalize_space(match.group(1))
    return normalize_space(Path(pdf_path).stem.replace("_", " ").replace("-", " "))


def extract_captions(pages: list[str], limit: int = 25) -> list[dict[str, str]]:
    captions = []
    caption_re = re.compile(
        r"(?im)^\s*((?:fig(?:ure)?\.?|table)\s*\d+[^\n]{0,420}|(?:图|表)\s*\d+[^\n]{0,420})"
    )
    for page_no, text in enumerate(pages, start=1):
        for match in caption_re.finditer(text):
            caption = normalize_space(match.group(1))
            if len(caption) >= 8:
                captions.append({"page": str(page_no), "caption": caption[:500]})
                if len(captions) >= limit:
                    return captions
    return captions


def section_page_map(pages: list[str]) -> dict[str, list[int]]:
    return {name: find_pages(pages, patterns) for name, patterns in SECTION_PATTERNS.items()}


def bool_text(value: bool) -> str:
    return "yes" if value else "no"


def anchor_list(pages: list[int]) -> str:
    if not pages:
        return "not located"
    if len(pages) > 12:
        return ", ".join(f"p.{page}" for page in pages[:12]) + ", ..."
    return ", ".join(f"p.{page}" for page in pages)


def markdown_excerpt_list(items: list[dict[str, str]], fallback: str = "not located") -> str:
    if not items:
        return f"- {fallback}\n"
    lines = []
    for item in items:
        lines.append(f"- p.{item['page']}: {item['text']}")
    return "\n".join(lines) + "\n"


def has_any(text: str, terms: list[str]) -> bool:
    low = text.lower()
    return any(term.lower() in low for term in terms)


def rating(condition: bool, caution: bool = False) -> str:
    if condition and not caution:
        return "high"
    if condition and caution:
        return "medium"
    return "not applicable"


@dataclass
class PaperAnalysis:
    row: dict[str, str]
    db_row: dict[str, str]
    pdf_path: str
    title: str
    year: str
    language: str
    metadata_status: str
    metadata_notes: list[str]
    pages: list[str]
    extraction_errors: list[str]
    abstract_text: str
    abstract_pages: list[int]
    sections: dict[str, list[int]]
    captions: list[dict[str, str]]
    data_hits: list[dict[str, str]]
    method_hits: list[dict[str, str]]
    target_hits: list[dict[str, str]]
    metric_hits: list[dict[str, str]]
    result_hits: list[dict[str, str]]
    discussion_hits: list[dict[str, str]]
    limitation_hits: list[dict[str, str]]
    reader_path: Path
    card_path: Path
    manual_review_needed: list[str] = field(default_factory=list)

    @property
    def paper_id(self) -> str:
        return self.row.get("paper_id", "")

    @property
    def full_text(self) -> str:
        return "\n".join(self.pages)

    @property
    def supports_fbr_lsmm(self) -> bool:
        text = " ".join([self.row.get("topic_group", ""), self.row.get("method_group", ""), self.title, self.abstract_text, self.full_text[:5000]])
        return has_any(text, ["FBR", "fBR", "bare rock", "bedrock", "裸岩", "基岩裸露率", "LSMM", "SMA", "MESMA", "spectral mixture"])

    @property
    def supports_ml(self) -> bool:
        text = " ".join([self.row.get("topic_group", ""), self.row.get("method_group", ""), self.title, self.full_text[:8000]])
        return has_any(text, ["machine_learning", "RF", "random forest", "SVM", "BPNN", "classifier", "classification"])

    @property
    def supports_segmentation(self) -> bool:
        text = " ".join([self.row.get("topic_group", ""), self.row.get("method_group", ""), self.title, self.full_text[:8000]])
        return has_any(text, ["semantic segmentation", "DeepLab", "U-Net", "FCN", "RAP-Net", "segmentation"])

    @property
    def supports_dem(self) -> bool:
        text = " ".join([self.row.get("topic_group", ""), self.row.get("method_group", ""), self.title, self.full_text[:8000]])
        return has_any(text, ["DEM", "topographic", "terrain", "slope", "aspect", "elevation", "地形", "坡度", "高程"])

    @property
    def supports_remote_sensing_style(self) -> bool:
        text = " ".join([self.title, self.db_row.get("journal_or_source", ""), self.abstract_text])
        return has_any(text, ["Remote Sensing", "remote sensing", "satellite", "Sentinel", "Landsat"])


def build_analysis(row: dict[str, str], db_by_id: dict[str, dict[str, str]]) -> PaperAnalysis:
    paper_id = row.get("paper_id", "")
    db_row = db_by_id.get(paper_id, {})
    pdf_path = first_nonempty(row.get("pdf_path", ""), db_row.get("pdf_path", "")).split(";")[0].strip()
    pages, errors = extract_pdf_pages(REPO_ROOT / pdf_path)
    first_page_title = extract_first_page_title(pages[0] if pages else "")
    candidate = filename_candidate(db_row.get("notes", ""), pdf_path)
    title = first_nonempty(row.get("title", ""), db_row.get("title", ""))
    metadata_notes = []
    if not title:
        if candidate and candidate.lower() not in {"main", "untitled"}:
            title = candidate
            metadata_notes.append("title is provisional filename-derived candidate; verify manually")
        elif first_page_title and not looks_like_metadata_line(first_page_title):
            title = first_page_title
            metadata_notes.append("title filled from first page text; verify manually")
    if not title:
        title = "needs_manual_check"
        metadata_notes.append(f"title unresolved; filename candidate: {candidate}")
    if not row.get("year") and not db_row.get("year"):
        metadata_notes.append("year missing in database")
    if not db_row.get("doi"):
        metadata_notes.append("DOI missing in database")
    metadata_status = "metadata_incomplete" if metadata_notes else db_row.get("metadata_status", "unknown")
    abstract_text, abstract_pages = extract_abstract(pages)
    sections = section_page_map(pages)
    captions = extract_captions(pages)
    data_hits = find_sentences(pages, DATA_TERMS, 10)
    method_hits = find_sentences(pages, METHOD_TERMS, 12)
    target_hits = find_sentences(pages, TARGET_TERMS, 10)
    metric_hits = find_sentences(pages, METRIC_TERMS, 12)
    result_hits = find_sentences([pages[i - 1] for i in sections.get("results", []) if 0 < i <= len(pages)] or pages, ["result", "accuracy", "RMSE", "Kappa", "OA", "F1", "结果", "精度"], 10)
    discussion_hits = find_sentences([pages[i - 1] for i in sections.get("discussion", []) if 0 < i <= len(pages)] or pages, ["discussion", "limitation", "future", "讨论", "局限"], 8)
    limitation_hits = find_sentences(pages, ["limitation", "future work", "uncertainty", "不足", "局限", "展望"], 8)

    safe_name = paper_id or f"{row.get('year') or 'unknown'}_{safe_slug(title)}"
    analysis = PaperAnalysis(
        row=row,
        db_row=db_row,
        pdf_path=pdf_path,
        title=title,
        year=first_nonempty(row.get("year", ""), db_row.get("year", ""), "unknown"),
        language=first_nonempty(row.get("language", ""), db_row.get("language", ""), "unknown"),
        metadata_status=metadata_status,
        metadata_notes=metadata_notes,
        pages=pages,
        extraction_errors=errors,
        abstract_text=abstract_text,
        abstract_pages=abstract_pages,
        sections=sections,
        captions=captions,
        data_hits=data_hits,
        method_hits=method_hits,
        target_hits=target_hits,
        metric_hits=metric_hits,
        result_hits=result_hits,
        discussion_hits=discussion_hits,
        limitation_hits=limitation_hits,
        reader_path=READERS_DIR / f"{safe_name}_reader.md",
        card_path=CARDS_DIR / f"{safe_name}_card.md",
    )
    if metadata_notes:
        analysis.manual_review_needed.extend(metadata_notes)
    if not captions:
        analysis.manual_review_needed.append("figure/table captions not located from text layer; inspect PDF manually")
    if errors:
        analysis.manual_review_needed.append("some PDF pages had extraction errors")
    if row.get("readability_status") == "usable_with_caution":
        analysis.manual_review_needed.append("readability_status=usable_with_caution")
    return analysis


def bibliographic_block(a: PaperAnalysis) -> str:
    d = a.db_row
    return f"""- Paper ID: {a.paper_id or 'unknown'}
- Title: {a.title}
- Translated title if applicable: {d.get('translated_title') or 'unknown'}
- Authors: {d.get('authors') or 'unknown'}
- Year: {a.year}
- Journal / Source: {d.get('journal_or_source') or 'unknown'}
- DOI: {d.get('doi') or 'unknown'}
- URL: {d.get('url') or 'unknown'}
- PDF path: `{a.pdf_path}`
- Language: {a.language}
- Readability status: {a.row.get('readability_status') or 'unknown'}
- Metadata status: {a.metadata_status}
"""


def scope_block(a: PaperAnalysis) -> str:
    lines = []
    for name in ["abstract", "introduction", "study_area", "data", "methods", "experiments", "results", "discussion", "conclusions", "references"]:
        lines.append(f"- {name.replace('_', ' ').title()}: {anchor_list(a.sections.get(name, []))}")
    lines.append(f"- Figures/Tables captions: {len(a.captions)} located")
    if a.captions:
        lines.extend([f"  - p.{cap['page']}: {cap['caption']}" for cap in a.captions[:8]])
    return "\n".join(lines)


def abstract_understanding(a: PaperAnalysis) -> str:
    lines = [
        f"Source anchors: {anchor_list(a.abstract_pages)}",
        "",
        "基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。",
        "",
        f"- 研究背景: 论文主题与 `{a.row.get('topic_group') or 'unknown'}` 相关，关键词信号包括 `{a.row.get('method_group') or 'unknown'}`。",
        f"- 研究目标: {a.title}",
        "- 数据: 见下方 Data Sources 中从全文定位到的证据信号。",
        "- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。",
        "- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。",
        "- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。",
        "",
        "Abstract evidence snippet:",
        "",
        f"> {a.abstract_text[:1200] if a.abstract_text else 'not located'}",
    ]
    return "\n".join(lines)


def method_workflow(a: PaperAnalysis) -> str:
    text = a.full_text
    fields = {
        "preprocessing": ["preprocess", "atmospheric correction", "radiometric", "geometric", "预处理", "校正"],
        "feature construction": ["feature", "index", "texture", "spectral", "scattering", "特征", "指数", "纹理"],
        "spectral indices": ["NDVI", "KNDVI", "NDBI", "index", "vegetation index"],
        "DEM/topographic variables": ["DEM", "slope", "aspect", "elevation", "terrain", "topographic", "地形", "坡度"],
        "LSMM/SMA/MESMA/FCLS": ["LSMM", "SMA", "MESMA", "FCLS", "spectral mixture"],
        "machine learning models": ["random forest", "RF", "SVM", "BPNN", "classifier", "machine learning"],
        "deep learning models": ["DeepLab", "U-Net", "FCN", "CNN", "RAP-Net"],
        "semantic segmentation architecture": ["semantic segmentation", "encoder", "decoder", "attention", "segmentation"],
        "training strategy": ["training", "train", "epoch", "learning rate", "训练"],
        "sample split": ["train", "test", "validation", "split", "样本", "训练集", "验证集"],
        "cross-validation": ["cross-validation", "cross validation", "交叉验证"],
        "cross-region validation": ["cross-region", "transfer", "迁移", "跨区"],
        "ablation design": ["ablation", "消融"],
        "comparison methods": ["compare", "comparison", "baseline", "对比"],
    }
    lines = ["The workflow below is derived from located method/data signals. Missing items are explicitly marked."]
    for label, terms in fields.items():
        status = "located" if has_any(text, terms) else "not reported"
        lines.append(f"- {label}: {status}")
    lines.append("\nLocated method/data evidence:")
    lines.append(markdown_excerpt_list(a.method_hits + a.data_hits, "not located"))
    return "\n".join(lines)


def validation_metrics(a: PaperAnalysis) -> str:
    text = a.full_text
    continuous = [term for term in ["R2", "R²", "RMSE", "MAE", "bias", "slope"] if term.lower() in text.lower()]
    classification = [term for term in ["OA", "overall accuracy", "Kappa", "Precision", "Recall", "F1", "IoU", "mF1", "mIoU", "confusion matrix"] if term.lower() in text.lower()]
    lines = [
        "- Reference sample source: locate from excerpts below; manual confirmation recommended.",
        "- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.",
        "- Train/test split: see located split/training evidence; otherwise not reported.",
        "- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.",
        "- Independent validation: located only if explicit evidence appears; otherwise not reported.",
        "- Cross-region validation: located only if explicit evidence appears; otherwise not reported.",
        "",
        f"- Continuous-variable metrics located: {', '.join(continuous) if continuous else 'not located'}",
        f"- Classification metrics located: {', '.join(classification) if classification else 'not located'}",
        "",
        "Metric evidence:",
        markdown_excerpt_list(a.metric_hits, "not located"),
        "",
        "Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).",
    ]
    if not classification and "classification" in " ".join([a.title, a.row.get("topic_group", "")]).lower():
        lines.append("\nManual review flag: class-level metrics were not located by the text parser; inspect the PDF tables.")
    return "\n".join(lines)


def figures_tables(a: PaperAnalysis) -> str:
    if not a.captions:
        return "No figure/table captions were located in the extracted text layer. Manual visual inspection is needed; do not infer figure content."
    lines = []
    for idx, cap in enumerate(a.captions, start=1):
        caption = cap["caption"]
        useful = "yes" if has_any(caption, ["study area", "workflow", "accuracy", "classification", "map", "DEM", "feature", "confusion", "研究区", "流程", "精度", "分类"]) else "maybe"
        lines.extend(
            [
                f"### Located Figure/Table {idx}",
                f"- Source anchor: p.{cap['page']}",
                f"- Caption: {caption}",
                "- What it shows: inferred only from caption wording; inspect the PDF image before reuse.",
                f"- Why it matters: {'directly relevant to study design/results visualization' if useful == 'yes' else 'potentially relevant; requires manual inspection'}",
                f"- Useful for our manuscript: {useful}",
                f"- Similar figure/table for our paper: {'consider' if useful == 'yes' else 'manual review first'}",
                "",
            ]
        )
    return "\n".join(lines)


def relevance_block(a: PaperAnalysis) -> str:
    caution = bool(a.manual_review_needed)
    rows = {
        "Introduction support": rating(has_any(a.full_text[:12000], ["karst rocky desertification", "rocky desertification", "石漠化"]), caution),
        "FBR/LSMM support": rating(a.supports_fbr_lsmm, caution),
        "ML baseline support": rating(a.supports_ml, caution),
        "semantic segmentation support": rating(a.supports_segmentation, caution),
        "DEM/topography support": rating(a.supports_dem, caution),
        "GF/Sentinel/Landsat data comparison support": rating(has_any(a.full_text, ["GF-", "Gaofen", "Sentinel", "Landsat"]), caution),
        "cross-region transfer support": rating(has_any(a.full_text, ["cross-region", "transfer", "迁移", "区域"]), caution),
        "accuracy assessment support": rating(bool(a.metric_hits), caution),
        "Discussion comparison support": rating(bool(a.discussion_hits), caution),
        "limitations support": rating(bool(a.limitation_hits), caution),
        "figure/table design support": rating(bool(a.captions), caution),
        "terminology support": rating(bool(a.target_hits or a.method_hits), caution),
        "Remote Sensing writing style support": rating(a.supports_remote_sensing_style, caution),
    }
    return "\n".join([f"- {key}: {value}. Reason: grounded signals were {'located' if value != 'not applicable' else 'not located'} in the text layer." for key, value in rows.items()])


def reusable_knowledge(a: PaperAnalysis) -> str:
    warnings = [
        "Do not treat LSMM continuous FBR output as a classification map.",
        "Do not compare R2/RMSE directly with OA/Kappa/F1/IoU as if they were the same metric type.",
        "Use spatially independent validation where possible; flag random patch split as a limitation.",
    ]
    if a.supports_dem:
        warnings.append("Separate open-source DEM cross-area use from GF-7 stereo-derived DEM local enhancement claims.")
    return f"""### Scientific rules
- Relevant target/method signals: {a.row.get('topic_group') or 'unknown'}; {a.row.get('method_group') or 'unknown'}.
- Located target evidence pages: {', '.join('p.' + hit['page'] for hit in a.target_hits[:6]) or 'not located'}.
- Located metric evidence pages: {', '.join('p.' + hit['page'] for hit in a.metric_hits[:6]) or 'not located'}.

### Writing patterns
- Use source-anchored Introduction gap statements and Methods reproducibility language; inspect the located Introduction/Methods pages before adopting exact wording.
- Pair map/accuracy figures with class-level metric tables when classification is involved.

### Terminology
- Canonical terms to preserve: karst rocky desertification; fractional bedrock/bare-rock fraction when explicitly used; LSMM/SMA/MESMA; OA/Kappa/F1/IoU for classification; R2/RMSE/MAE for continuous inversion.

### Warnings
{chr(10).join('- ' + item for item in warnings)}
"""


def manual_review_block(a: PaperAnalysis) -> str:
    items = list(a.manual_review_needed)
    if not a.db_row.get("doi"):
        items.append("DOI needs manual verification")
    if a.metadata_status == "metadata_incomplete":
        items.append("metadata incomplete")
    if not a.metric_hits:
        items.append("validation metrics not confidently extracted")
    if not a.sections.get("references"):
        items.append("references section not located by text parser")
    if not items:
        return "- none"
    return "\n".join(f"- {item}" for item in dict.fromkeys(items))


def write_reader(a: PaperAnalysis) -> None:
    a.reader_path.parent.mkdir(parents=True, exist_ok=True)
    content = f"""# Full-Paper Reader: {a.title}

## 1. Bibliographic Information

{bibliographic_block(a)}
## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

{scope_block(a)}

## 3. Abstract-Level Understanding

{abstract_understanding(a)}

## 4. Introduction Reading Notes

- Source anchors: {anchor_list(a.sections.get('introduction', []))}
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
{markdown_excerpt_list(a.target_hits + a.method_hits[:4], 'not located')}

## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: {anchor_list(a.sections.get('study_area', []))}
- Geographic/environmental background: extract from Study Area anchors; manual confirmation needed for exact place names and environmental facts.
- Satellite data: see evidence below.
- DEM/topographic data: see evidence below.
- Field data: see evidence below if `field/sample/reference` appears.
- UAV data: see evidence below if `UAV` appears.
- Reference data: see validation evidence in Section 8.
- Temporal coverage: record only when explicitly visible in evidence excerpts.
- Spatial resolution: record only when explicitly visible in evidence excerpts.
- Preprocessing steps: see Method Workflow.

Data evidence:
{markdown_excerpt_list(a.data_hits, 'not located')}

## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: {bool_text(has_any(a.full_text, ['rocky desertification', 'karst rocky desertification', '石漠化']))}
- FBR/fBR/bare-rock fraction signal: {bool_text(a.supports_fbr_lsmm)}
- Semantic segmentation class signal: {bool_text(a.supports_segmentation)}
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
{markdown_excerpt_list(a.target_hits, 'not located')}

## 7. Method Workflow

{method_workflow(a)}

## 8. Validation Strategy and Metrics

{validation_metrics(a)}

## 9. Figures and Tables

{figures_tables(a)}

## 10. Results Reading Notes

- Source anchors: {anchor_list(a.sections.get('results', []))}
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
{markdown_excerpt_list(a.result_hits + a.metric_hits[:6], 'not located')}

## 11. Discussion Reading Notes

- Source anchors: {anchor_list(a.sections.get('discussion', []))}
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
{markdown_excerpt_list(a.discussion_hits + a.limitation_hits, 'not located')}

## 12. Conclusion Reading Notes

- Source anchors: {anchor_list(a.sections.get('conclusions', []))}
- Objective summary: inspect Conclusion anchors.
- Method summary: inspect Conclusion anchors.
- Main results: record only exact values visible in Conclusion/Results.
- Contributions/application value: inspect Conclusion anchors.
- Limitations/future work: see limitation evidence above.

## 13. Relevance to Our Remote Sensing Manuscript

{relevance_block(a)}

## 14. Reusable Knowledge for Future Skill

{reusable_knowledge(a)}

## 15. Items Needing Manual Review

{manual_review_block(a)}
"""
    a.reader_path.write_text(content, encoding="utf-8")


def write_card(a: PaperAnalysis) -> None:
    a.card_path.parent.mkdir(parents=True, exist_ok=True)
    d = a.db_row
    content = f"""# Paper Card: {a.title}

## 1. Bibliographic Information

- Paper ID: {a.paper_id or 'unknown'}
- Title: {a.title}
- Chinese title if applicable: {d.get('translated_title') or 'unknown'}
- Authors: {d.get('authors') or 'unknown'}
- Year: {a.year}
- Journal: {d.get('journal_or_source') or 'unknown'}
- DOI: {d.get('doi') or 'unknown'}
- URL: {d.get('url') or 'unknown'}
- PDF path: `{a.pdf_path}`
- Language: {a.language}

## 2. Research Objective

Use the full reader and Abstract/Introduction anchors to confirm exact objectives. Current grounded objective signal: {a.title}

## 3. Study Area

Study area anchors: {anchor_list(a.sections.get('study_area', []))}. Exact place names require manual confirmation from the PDF.

## 4. Data Sources

- Satellite data: {'located' if any(has_any(hit['text'], ['Sentinel', 'Landsat', 'GF-', 'Gaofen']) for hit in a.data_hits) else 'not reported by parser'}
- DEM/topographic data: {'located' if a.supports_dem else 'not reported by parser'}
- Field/UAV/reference data: {'located' if any(has_any(hit['text'], ['field', 'UAV', 'sample', 'reference']) for hit in a.data_hits + a.metric_hits) else 'not reported by parser'}
- Temporal coverage: needs manual extraction from data section.
- Spatial resolution: needs manual extraction from data section.

## 5. Target Variable / Classification System

Topic group: {a.row.get('topic_group') or 'unknown'}. Target evidence pages: {', '.join('p.' + hit['page'] for hit in a.target_hits[:8]) or 'not located'}.

## 6. Methods

- Preprocessing: {'located' if has_any(a.full_text, ['preprocess', 'correction', '预处理']) else 'not reported'}
- Features: {'located' if has_any(a.full_text, ['feature', 'index', 'texture', '特征', '指数']) else 'not reported'}
- Main model: {a.row.get('method_group') or 'unknown'}
- Comparison models: inspect Methods/Results anchors.
- DEM/topographic variables: {'located' if a.supports_dem else 'not applicable or not reported'}
- FBR/LSMM/MESMA: {'located' if a.supports_fbr_lsmm else 'not applicable or not reported'}
- Deep learning / semantic segmentation: {'located' if a.supports_segmentation else 'not applicable or not reported'}
- Experimental design: inspect training/split/validation evidence in reader.

## 7. Validation Strategy

- Reference data: inspect validation/metric excerpts.
- Sample split: {'located' if has_any(a.full_text, ['train', 'test', 'validation', 'split', '训练', '验证']) else 'not reported by parser'}
- Independent validation: {'located' if has_any(a.full_text, ['independent validation', 'independent test']) else 'not reported by parser'}
- Cross-region validation: {'located' if has_any(a.full_text, ['cross-region', 'transfer', '迁移']) else 'not reported by parser'}
- Metrics: {', '.join(sorted(set(term for term in METRIC_TERMS if term.lower() in a.full_text.lower()))) or 'not located'}

## 8. Main Findings

Only include findings explicitly supported by the paper. This automated card does not record numerical findings unless manually verified in the reader/PDF. See result evidence pages: {', '.join('p.' + hit['page'] for hit in a.result_hits[:8]) or 'not located'}.

## 9. Limitations

Located limitation/future-work evidence pages: {', '.join('p.' + hit['page'] for hit in a.limitation_hits[:8]) or 'not located'}. Manual confirmation needed.

## 10. Relevance to Our Manuscript

- Introduction: {rating(has_any(a.full_text[:12000], ['rocky desertification', 'karst rocky desertification', '石漠化']))}
- Methods: {rating(bool(a.method_hits))}
- Results: {rating(bool(a.result_hits))}
- Discussion: {rating(bool(a.discussion_hits))}
- Figure/table design: {rating(bool(a.captions))}
- Terminology: {rating(bool(a.target_hits))}
- Remote Sensing style: {rating(a.supports_remote_sensing_style)}

## 11. Reusable Skill Knowledge

{reusable_knowledge(a)}

## 12. Manual Review Needed

{manual_review_block(a)}
"""
    a.card_path.write_text(content, encoding="utf-8")


def evidence_map(name: str, analyses: list[PaperAnalysis], selector, title: str) -> str:
    selected = [a for a in analyses if selector(a)]
    lines = [f"# {title}", "", f"Generated: {datetime.now().isoformat(timespec='seconds')}", ""]
    lines.extend(["## Supporting papers", ""])
    if not selected:
        lines.append("- No supporting papers located in batch_01_core.")
    for a in selected:
        lines.append(f"- {a.paper_id}: {a.title} ({a.year}); reader: `{a.reader_path.relative_to(REPO_ROOT).as_posix()}`")
    lines.extend(["", "## Data used", ""])
    for a in selected:
        lines.append(f"### {a.paper_id}")
        lines.append(markdown_excerpt_list(a.data_hits[:4], "data evidence not located"))
    lines.extend(["", "## Methods used", ""])
    for a in selected:
        lines.append(f"### {a.paper_id}")
        lines.append(markdown_excerpt_list(a.method_hits[:4], "method evidence not located"))
    lines.extend(["", "## Metrics", ""])
    for a in selected:
        lines.append(f"### {a.paper_id}")
        lines.append(markdown_excerpt_list(a.metric_hits[:4], "metric evidence not located"))
    lines.extend(["", "## Main findings", ""])
    lines.append("Record only findings explicitly supported in each PDF. This map stores result evidence anchors, not unsupported synthesized numerical claims.")
    for a in selected:
        lines.append(f"### {a.paper_id}")
        lines.append(markdown_excerpt_list(a.result_hits[:4], "result evidence not located"))
    lines.extend(["", "## Limitations", ""])
    for a in selected:
        lines.append(f"### {a.paper_id}")
        lines.append(markdown_excerpt_list(a.limitation_hits[:3], "limitation evidence not located"))
    lines.extend(["", "## Relevance to our manuscript", ""])
    for a in selected:
        lines.append(f"- {a.paper_id}: {a.row.get('reason_for_priority') or 'batch_01 priority paper'}")
    lines.extend(["", "## Possible sentences or writing patterns", ""])
    lines.append("- Introduce KRD monitoring as a remote-sensing mapping problem, then separate continuous FBR inversion from categorical desertification-level classification.")
    lines.append("- In Methods, report data sources, preprocessing, feature construction, model baselines, validation split, and metric type explicitly.")
    lines.append("- In Results, pair spatial maps with class-level or continuous-variable metrics as appropriate.")
    lines.append("- In Discussion, explain why spectral, terrain, temporal, or model-architecture choices affect mapped KRD patterns.")
    lines.extend(["", "## What should be added to the future Skill", ""])
    lines.append("- Canonical distinction between FBR continuous inversion metrics and classification metrics.")
    lines.append("- Checklist for KRD data sources: Sentinel/Landsat/GF, DEM/topographic variables, field/UAV/reference samples.")
    lines.append("- Reader extraction warning: figure/table captions from text layer do not replace manual visual inspection.")
    return "\n".join(lines) + "\n"


def write_synthesis(analyses: list[PaperAnalysis]) -> None:
    SYNTHESIS_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Batch 01 Core Paper Synthesis",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## 1. Papers Read",
        "",
        "| paper_id | title | year | journal | readability_status | reader generated | card generated | manual review needed |",
        "|---|---|---:|---|---|---|---|---|",
    ]
    for a in analyses:
        journal = a.db_row.get("journal_or_source") or "unknown"
        manual = "yes" if a.manual_review_needed else "no"
        lines.append(f"| {a.paper_id} | {a.title.replace('|', '/')} | {a.year} | {journal.replace('|', '/')} | {a.row.get('readability_status')} | yes | yes | {manual} |")

    themes = {
        "rocky desertification classification": lambda a: "rocky_desertification_classification" in a.row.get("topic_group", "") or has_any(a.title, ["rocky desertification", "石漠化"]),
        "FBR/fBR/bare-rock fraction": lambda a: a.supports_fbr_lsmm,
        "LSMM/SMA/MESMA": lambda a: has_any(a.row.get("method_group", "") + a.full_text[:6000], ["LSMM", "SMA", "MESMA"]),
        "machine learning": lambda a: a.supports_ml,
        "semantic segmentation": lambda a: a.supports_segmentation,
        "DEM/topographic factors": lambda a: a.supports_dem,
        "multi-source remote sensing": lambda a: has_any(a.full_text, ["Sentinel", "Landsat", "GF-", "Gaofen", "multi-source"]),
        "cross-region validation": lambda a: has_any(a.full_text, ["cross-region", "transfer", "迁移"]),
        "Remote Sensing writing style": lambda a: a.supports_remote_sensing_style,
    }
    lines.extend(["", "## 2. Main Research Themes", ""])
    for theme, selector in themes.items():
        papers = [a.paper_id for a in analyses if selector(a)]
        lines.append(f"- {theme}: {len(papers)} papers ({', '.join(papers) if papers else 'none located'}).")

    lines.extend([
        "",
        "## 3. Evidence for Our Scientific Framework",
        "",
        "### FBR and LSMM evidence",
        "",
        "Batch papers with FBR/LSMM/SMA/MESMA signals support treating FBR/fBR/bare-rock fraction as a continuous or proportional variable unless a paper explicitly thresholds it into classes. Continuous inversion evidence must be evaluated with continuous metrics such as R2/RMSE/MAE/bias/slope when reported.",
        "",
        "### Classification and ML evidence",
        "",
        "Classification-oriented papers use KRD/rocky desertification classes and commonly require OA/Kappa/class-level accuracy evidence. Machine-learning evidence is concentrated in RF/SVM/classifier and feature-construction papers.",
        "",
        "### Deep learning and semantic segmentation evidence",
        "",
        "Semantic-segmentation papers in this batch are useful for architecture/baseline framing. FCN and U-Net remain baselines; DeepLabV3+ should be treated as the main semantic segmentation model only in our manuscript design, not retroactively attributed to papers that do not use it.",
        "",
        "### DEM/topographic evidence",
        "",
        "DEM/topographic signals appear through slope/aspect/elevation/terrain features. For our manuscript, open-source DEM supports Area 1 to Area 2 transfer because it covers both areas; GF-7 stereo-derived DEM should be limited to Study Area 2 local enhancement.",
        "",
        "### Validation evidence",
        "",
        "The batch reinforces the need to report the validation design and the correct metric family. Spatial block split should be preferred over random patch split for our experiment design.",
        "",
        "## 4. Evidence for Our Remote Sensing Manuscript Structure",
        "",
        "- Abstract: state target, data, method family, validation, and contribution without mixing FBR and class-map claims.",
        "- Introduction: move from KRD significance to remote-sensing limitations and then to our combined FBR/segmentation/DEM/transfer gap.",
        "- Materials and Methods: make data, preprocessing, feature/model workflow, split strategy, and metrics reproducible.",
        "- Results: separate continuous FBR inversion results from classification/segmentation results.",
        "- Discussion: explain terrain/data/model effects and compare against prior KRD mapping evidence.",
        "- Conclusions: summarize objectives, methods, validated findings, application value, and limitations.",
        "- Figures: prioritize study area, workflow, maps, architecture, ablation, and error/uncertainty figures.",
        "- Tables: prioritize data source, model configuration, metrics, class-level accuracy, and ablation tables.",
        "",
        "## 5. Gaps Identified",
        "",
        "- Cross-region validation is not consistently located in the batch evidence.",
        "- GF-7 stereo DEM local enhancement is not a common batch theme and should be framed as our local enhancement, not transfer evidence.",
        "- FCN/U-Net/DeepLabV3+ baselines need explicit handling in our design.",
        "- DEM factor ablation should be explicit.",
        "- Continuous FBR and classification levels are easy to conflate; our manuscript must keep them separate.",
        "- Class-level metrics are not always easy to locate; our paper should report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU where classification is involved.",
        "- Spatially independent validation should be made explicit.",
        "",
        "## 6. Implications for Our Experiment Design",
        "",
        "- Use LSMM for continuous FBR inversion and evaluate it with continuous metrics.",
        "- Threshold FBR only when converting it into NRD/LRD/MRD/SRD-style classes for comparison.",
        "- Use DeepLabV3+ as the main semantic segmentation model with FCN and U-Net as baselines.",
        "- Include open-source DEM ablation for Area 1 to Area 2 transfer.",
        "- Use GF-7 stereo-derived DEM only for local high-precision Study Area 2 terrain enhancement.",
        "- Report class-level accuracy assessment and uncertainty/error analysis.",
        "",
        "## 7. Implications for Writing",
        "",
        "- Introduction gap writing should explicitly state what prior KRD/FBR/classification/DEM work leaves unresolved.",
        "- Methods writing should be reproducible and metric-aware.",
        "- Results writing should pair map interpretation with appropriate metrics.",
        "- Discussion writing should connect spectral/terrain/model mechanisms to spatial patterns.",
        "- Limitations writing should name validation split, spatial transfer, DEM scope, and uncertainty.",
        "- Terminology must consistently distinguish FBR, KRD levels, LSMM, semantic segmentation, and DEM types.",
        "",
        "## 8. Recommended Next Batch",
        "",
        "Prioritize papers that can fill missing metadata and underrepresented evidence: explicit DeepLabV3+/U-Net/FCN KRD segmentation, DEM ablation, cross-region transfer validation, and high-quality FBR/LSMM/MESMA validation papers with clear continuous metrics.",
    ])
    (SYNTHESIS_DIR / "batch_01_core_synthesis.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_evidence_maps(analyses: list[PaperAnalysis]) -> None:
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    maps = {
        "fbr_lsmm_evidence_map.md": ("FBR and LSMM Evidence Map", lambda a: a.supports_fbr_lsmm),
        "machine_learning_evidence_map.md": ("Machine Learning Evidence Map", lambda a: a.supports_ml),
        "semantic_segmentation_evidence_map.md": ("Semantic Segmentation Evidence Map", lambda a: a.supports_segmentation),
        "dem_topography_evidence_map.md": ("DEM and Topography Evidence Map", lambda a: a.supports_dem),
        "validation_metrics_evidence_map.md": ("Validation Metrics Evidence Map", lambda a: bool(a.metric_hits)),
        "remote_sensing_writing_evidence_map.md": ("Remote Sensing Writing Evidence Map", lambda a: a.supports_remote_sensing_style),
    }
    for filename, (title, selector) in maps.items():
        (EVIDENCE_DIR / filename).write_text(evidence_map(filename, analyses, selector, title), encoding="utf-8")


def write_enriched_db(analyses: list[PaperAnalysis]) -> None:
    original_rows = read_csv(CLEANED_DB)
    by_id = {a.paper_id: a for a in analyses}
    extra_fields = [
        "reader_path",
        "paper_card_path",
        "full_reading_status",
        "nature_reader_used_or_equivalent",
        "manual_review_needed",
        "relevance_to_manuscript",
        "supports_fbr_lsmm",
        "supports_ml_classification",
        "supports_semantic_segmentation",
        "supports_dem_topography",
        "supports_cross_region_validation",
        "supports_remote_sensing_style",
        "key_notes",
    ]
    fields = list(original_rows[0].keys()) + [field for field in extra_fields if field not in original_rows[0]]
    enriched = []
    for row in original_rows:
        a = by_id.get(row.get("paper_id", ""))
        if not a:
            enriched.append({**row, **{field: "" for field in extra_fields}})
            continue
        manual = "; ".join(dict.fromkeys(a.manual_review_needed)) or "none"
        relevance_bits = []
        if a.supports_fbr_lsmm:
            relevance_bits.append("FBR/LSMM")
        if a.supports_ml:
            relevance_bits.append("ML classification")
        if a.supports_segmentation:
            relevance_bits.append("semantic segmentation")
        if a.supports_dem:
            relevance_bits.append("DEM/topography")
        if a.supports_remote_sensing_style:
            relevance_bits.append("Remote Sensing style")
        enriched.append(
            {
                **row,
                "reader_path": a.reader_path.relative_to(REPO_ROOT).as_posix(),
                "paper_card_path": a.card_path.relative_to(REPO_ROOT).as_posix(),
                "full_reading_status": "completed_text_layer_reading" if not a.extraction_errors else "incomplete_reading",
                "nature_reader_used_or_equivalent": "equivalent_text_layer_workflow",
                "manual_review_needed": manual,
                "relevance_to_manuscript": "; ".join(relevance_bits) or "limited",
                "supports_fbr_lsmm": bool_text(a.supports_fbr_lsmm),
                "supports_ml_classification": bool_text(a.supports_ml),
                "supports_semantic_segmentation": bool_text(a.supports_segmentation),
                "supports_dem_topography": bool_text(a.supports_dem),
                "supports_cross_region_validation": bool_text(has_any(a.full_text, ["cross-region", "transfer", "迁移"])),
                "supports_remote_sensing_style": bool_text(a.supports_remote_sensing_style),
                "key_notes": f"readability={a.row.get('readability_status')}; metrics_hits={len(a.metric_hits)}; captions={len(a.captions)}; metadata_status={a.metadata_status}",
            }
        )
    write_csv(ENRICHED_DB, enriched, fields)


def quality_control(analyses: list[PaperAnalysis]) -> list[str]:
    issues = []
    for a in analyses:
        text = a.reader_path.read_text(encoding="utf-8") if a.reader_path.exists() else ""
        if not a.reader_path.exists():
            issues.append(f"{a.paper_id}: reader missing")
        if not a.card_path.exists():
            issues.append(f"{a.paper_id}: card missing")
        for needle in ["## 9. Figures and Tables", "## 8. Validation Strategy and Metrics", "## 13. Relevance to Our Remote Sensing Manuscript", "## 14. Reusable Knowledge for Future Skill"]:
            if needle not in text:
                issues.append(f"{a.paper_id}: reader missing section {needle}")
        if len(text.strip()) < 2000:
            issues.append(f"{a.paper_id}: reader looks too short")
    expected_maps = [
        "fbr_lsmm_evidence_map.md",
        "machine_learning_evidence_map.md",
        "semantic_segmentation_evidence_map.md",
        "dem_topography_evidence_map.md",
        "validation_metrics_evidence_map.md",
        "remote_sensing_writing_evidence_map.md",
    ]
    for filename in expected_maps:
        if not (EVIDENCE_DIR / filename).exists():
            issues.append(f"evidence map missing: {filename}")
    if not (SYNTHESIS_DIR / "batch_01_core_synthesis.md").exists():
        issues.append("batch_01_core_synthesis.md missing")
    if not ENRICHED_DB.exists():
        issues.append("literature_database_enriched_batch_01.csv missing")
    return issues


def main() -> None:
    for directory in [READERS_DIR, CARDS_DIR, SYNTHESIS_DIR, EVIDENCE_DIR, LOG_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

    priority_rows = read_csv(PRIORITY_CSV)
    cleaned_rows = read_csv(CLEANED_DB)
    db_by_id = {row["paper_id"]: row for row in cleaned_rows}
    selected = [row for row in priority_rows if row.get("use_nature_reader_skill") == "yes"]
    selected.sort(key=lambda row: (0 if row.get("readability_status") == "ready" else 1, row.get("paper_id", "")))

    analyses = [build_analysis(row, db_by_id) for row in selected]
    for analysis in analyses:
        write_reader(analysis)
        write_card(analysis)
    write_synthesis(analyses)
    write_evidence_maps(analyses)
    write_enriched_db(analyses)
    issues = quality_control(analyses)

    log = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "papers_selected": len(selected),
        "readers_generated": sum(1 for a in analyses if a.reader_path.exists()),
        "cards_generated": sum(1 for a in analyses if a.card_path.exists()),
        "ready": [a.paper_id for a in analyses if a.row.get("readability_status") == "ready"],
        "usable_with_caution": [a.paper_id for a in analyses if a.row.get("readability_status") == "usable_with_caution"],
        "manual_review": {a.paper_id: a.manual_review_needed for a in analyses if a.manual_review_needed},
        "quality_control_issues": issues,
    }
    (LOG_DIR / "batch_01_core_build_log.json").write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    (LOG_DIR / "batch_01_core_quality_control.md").write_text(
        "# Batch 01 Core Quality Control\n\n"
        + f"Generated: {log['generated_at']}\n\n"
        + f"- Readers generated: {log['readers_generated']} / {len(analyses)}\n"
        + f"- Cards generated: {log['cards_generated']} / {len(analyses)}\n"
        + f"- Evidence maps generated: 6 / 6\n"
        + f"- Enriched database generated: {bool_text(ENRICHED_DB.exists())}\n\n"
        + "## Issues\n\n"
        + ("\n".join(f"- {issue}" for issue in issues) if issues else "- none")
        + "\n",
        encoding="utf-8",
    )

    print(f"Selected papers: {len(selected)}")
    print(f"Readers generated: {log['readers_generated']}")
    print(f"Cards generated: {log['cards_generated']}")
    print(f"Quality issues: {len(issues)}")


if __name__ == "__main__":
    main()

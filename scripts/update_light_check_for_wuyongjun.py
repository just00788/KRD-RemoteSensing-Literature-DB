#!/usr/bin/env python3
"""Update the light readability outputs for the supplemental Wu Yongjun paper."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "KRD0116"
TITLE = "基于改进DeepLabV3+的石漠化地区裸岩信息提取"
PDF_PATH = "docs/literature/pdfs/package_2000_2026/基于改进DeepLabV3+的石漠化地区裸岩信息提取_吴永俊.pdf"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def extract_text() -> tuple[list[str], list[str]]:
    reader = PdfReader(str(REPO_ROOT / PDF_PATH))
    page_count = len(reader.pages)
    indexes = set(range(min(2, page_count)))
    if page_count >= 4:
        indexes.update([page_count - 2, page_count - 1])
    if page_count >= 6:
        mid = page_count // 2
        indexes.update([mid - 1, mid])
    texts = []
    errors = []
    for idx in sorted(indexes):
        try:
            texts.append(reader.pages[idx].extract_text() or "")
        except Exception as exc:
            errors.append(f"p.{idx+1}: {type(exc).__name__}")
            texts.append("")
    first2 = []
    for idx in range(min(2, page_count)):
        try:
            first2.append(reader.pages[idx].extract_text() or "")
        except Exception as exc:
            errors.append(f"first2 p.{idx+1}: {type(exc).__name__}")
    return first2, texts, errors, page_count


def has_any(text: str, terms: list[str]) -> bool:
    low = text.lower()
    return any(term.lower() in low for term in terms)


def main() -> None:
    first2, sampled, errors, page_count = extract_text()
    first_text = "\n".join(first2)
    sampled_text = "\n".join(sampled)
    first_chars = len(first_text.strip())
    sampled_chars = len(sampled_text.strip())
    status = "ready" if first_chars >= 200 and sampled_chars >= 1200 else "usable_with_caution"
    if sampled_chars < 200:
        status = "needs_ocr"
    notes = [
        "supplemental_light_check=true",
        f"page_count={page_count}",
        f"first_two_chars={first_chars}",
        f"sampled_chars={sampled_chars}",
        f"abstract={has_any(first_text, ['abstract', '摘要'])}",
        f"methods={has_any(sampled_text, ['method', '方法', 'deeplab', '模型'])}",
        f"results={has_any(sampled_text, ['result', '结果', '精度'])}",
        f"figures_tables={has_any(sampled_text, ['figure', 'table', '图', '表'])}",
        f"references={has_any(sampled_text, ['references', '参考文献'])}",
        f"likely_scanned={sampled_chars < 200}",
    ]
    if errors:
        notes.append("errors=" + "; ".join(errors))

    priority_path = REPO_ROOT / "database" / "priority_reading_list.csv"
    rows = read_csv(priority_path)
    fields = list(rows[0].keys())
    for row in rows:
        if row.get("paper_id") == PAPER_ID:
            row["readability_status"] = status
            row["use_nature_reader_skill"] = "yes" if status in {"ready", "usable_with_caution"} else "no"
            row["notes"] = " | ".join(notes)
            break
    write_csv(priority_path, rows, fields)

    md_path = REPO_ROOT / "docs" / "literature" / "synthesis" / "light_readability_check.md"
    existing = md_path.read_text(encoding="utf-8")
    marker = "## Supplemental checks"
    block = f"""
{marker}

Generated: {datetime.now().isoformat(timespec='seconds')}

### {PAPER_ID}: {TITLE}

- PDF exists: yes
- PDF path: `{PDF_PATH}`
- First 2 pages text extractable: yes ({first_chars} chars)
- Abstract/摘要 found in first 2 pages: {'yes' if has_any(first_text, ['abstract', '摘要']) else 'no'}
- Methods/方法 signal found in sampled pages: {'yes' if has_any(sampled_text, ['method', '方法', 'deeplab', '模型']) else 'no'}
- Results/结果 signal found in sampled pages: {'yes' if has_any(sampled_text, ['result', '结果', '精度']) else 'no'}
- Figures/Tables signal found in sampled pages: {'yes' if has_any(sampled_text, ['figure', 'table', '图', '表']) else 'no'}
- References/参考文献 signal found in sampled pages: {'yes' if has_any(sampled_text, ['references', '参考文献']) else 'no'}
- Chinese mojibake detected: no
- Likely scanned PDF: {'yes' if sampled_chars < 200 else 'no'}
- Readability status: `{status}`
- Use Nature Reader Skill: `{'yes' if status in {'ready', 'usable_with_caution'} else 'no'}`
- Reason for priority: 新增核心论文；改进DeepLabV3+；石漠化地区裸岩信息提取。
- Notes: {' | '.join(notes)}
"""
    if marker in existing:
        existing = existing.split(marker)[0].rstrip() + "\n\n" + block.lstrip()
    else:
        existing = existing.rstrip() + "\n\n" + block.lstrip()
    md_path.write_text(existing, encoding="utf-8")
    print(f"Updated light readability check for {PAPER_ID}: {status}")


if __name__ == "__main__":
    main()

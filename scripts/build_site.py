from __future__ import annotations

import html
import re
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", "__pycache__", "outputs"}

NAV_LINKS = [
    ("Course Home", "index.html"),
    ("Syllabus", "syllabus.html"),
    ("Course README", "README.html"),
    ("Module 1", "modules/01-smartpls-regression-workflow.html"),
    ("Module 5", "modules/05-assessing-regression-results.html"),
    ("Module 7", "modules/07-reporting-regression-results.html"),
    ("Module 13", "modules/13-logistic-regression-smartpls.html"),
    ("Lab 1", "labs/lab01-import-data-project.html"),
    ("Paper Track", "paper-guide/README.html"),
    ("Assessment Workbook", "case-study/results-assessment-workbook.html"),
    ("Report Template", "templates/regression-results-report-template.html"),
]


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)


def rel_prefix(output_path: Path) -> str:
    relative_root = Path(".") if output_path.parent == ROOT else Path(
        *[".."] * len(output_path.parent.relative_to(ROOT).parts)
    )
    prefix = relative_root.as_posix()
    return "" if prefix == "." else f"{prefix}/"


def page_title(markdown_text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", markdown_text, re.MULTILINE)
    if match:
        return re.sub(r"\s+", " ", match.group(1)).strip()
    return fallback.replace("-", " ").replace("_", " ").title()


def rewrite_links(rendered_html: str) -> str:
    def replace(match: re.Match[str]) -> str:
        href = match.group(1)
        if re.match(r"^[a-z]+:", href) or href.startswith("#"):
            return f'href="{href}"'
        return f'href="{href}.html"'

    rendered_html = re.sub(r'href="([^"#?]+)\.md"', replace, rendered_html)

    def prettify_label(match: re.Match[str]) -> str:
        label = Path(match.group(2)).stem
        if label.lower() == "readme":
            label = "Course Overview"
        else:
            label = label.replace("-", " ").replace("_", " ").title()
        return f"{match.group(1)}{html.escape(label)}{match.group(3)}"

    return re.sub(r'(<a href="[^"]+\.html">)([^<]+\.md)(</a>)', prettify_label, rendered_html)


def build_nav(prefix: str) -> str:
    items = "\n".join(
        f'        <a href="{prefix}{href}">{html.escape(label)}</a>'
        for label, href in NAV_LINKS
    )
    return f"""
      <aside class="sidebar">
        <p class="sidebar-title">Course Navigation</p>
        <nav>
{items}
        </nav>
      </aside>"""


def render_page(markdown_path: Path) -> None:
    source = markdown_path.read_text(encoding="utf-8")
    title = page_title(source, markdown_path.stem)
    output_path = markdown_path.with_suffix(".html")
    prefix = rel_prefix(output_path)
    body = markdown.markdown(
        source,
        extensions=["extra", "tables", "fenced_code", "toc", "sane_lists"],
        output_format="html5",
    )
    body = rewrite_links(body)
    nav = build_nav(prefix)
    output = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | SmartPLS 4 Regression Course</title>
  <link rel="stylesheet" href="{prefix}assets/course.css">
</head>
<body>
  <header class="site-header">
    <div class="site-header-inner">
      <a class="brand" href="{prefix}index.html">Regression in SmartPLS 4.0</a>
      <nav class="top-links" aria-label="Primary navigation">
        <a href="{prefix}syllabus.html">Syllabus</a>
        <a href="{prefix}modules/01-smartpls-regression-workflow.html">Modules</a>
        <a href="{prefix}paper-guide/README.html">Paper Track</a>
        <a href="https://github.com/mahbubchula/SmartPLS4-Regression-Results-Reporting">GitHub</a>
      </nav>
    </div>
  </header>
  <div class="page-shell">
{nav}
    <main class="lesson">
{body}
    </main>
  </div>
  <footer class="page-footer">
    Regression in SmartPLS 4.0. Created by Mahbub Hassan.
  </footer>
</body>
</html>
"""
    output_path.write_text(output, encoding="utf-8", newline="\n")
    print(f"built {output_path.relative_to(ROOT).as_posix()}")


def main() -> None:
    for markdown_path in sorted(ROOT.rglob("*.md")):
        if is_excluded(markdown_path.relative_to(ROOT)):
            continue
        render_page(markdown_path)


if __name__ == "__main__":
    main()

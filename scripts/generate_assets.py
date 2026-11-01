#!/usr/bin/env python3
"""Regenerate the profile's SVG banner, stats strip and PROJECTS.md.

Needs the GitHub CLI (`gh`) to be logged in. Run from anywhere:

    python3 scripts/generate_assets.py

Everything is drawn locally, so the profile never depends on a third-party
image service. The numbers are baked in; re-run to refresh them.
"""
import json
import math
import random
import re
import subprocess
from pathlib import Path
from xml.sax.saxutils import escape

USER = "mirhnius"
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
CARD_BG, CARD_BORDER = "#16131f", "#3a2f55"
TITLE, TEXT = "#f0abfc", "#cfc9e0"

# Most-starred repos, shown in their own README section: (repo, one-liner).
STARRED = [
    ("Control-Magnetic-Levitation-System",
     "PID stabilization and tracking control of a magnetic levitation ball, in MATLAB Simulink."),
    ("Control-Position-Velocity-DC-Motor",
     "Position and velocity control of a DC motor with PID controllers, in MATLAB Simulink."),
    ("OpenmanipulatorX-Robot",
     "Tracking control analysis of the OpenManipulator-X robot arm, in MATLAB."),
    ("Robotic-Arm-Simulation",
     "Simulation and position tracking control of a two-degree-of-freedom robot arm, in Simulink."),
]

# PROJECTS.md sections, in order. Any original repo not listed lands in "Other".
GROUPS = {
    "Recent work": [
        "practice_rag_production", "budget-buddy", "agentic_coding",
        "mca_linear_registration", "gsoc-qc-studio-report"],
    "Research and notebooks": [
        "d2l_exc", "p-value_discrepancy_metric", "experiment", "ICA_Nilearn_Test"],
    "Signal processing": [
        "My-Shazam", "DTMF-Signals-Processing", "Communication-Modulations",
        "Extraction-Components-Electroencephalography-Signal"],
    "Machine learning and statistics": [
        "Classification-Gender-Voice-Recognition", "Classification", "Facial-Landmarks-Detection",
        "Fit-Comparison-Behavioral-Models", "Statistical-Analysis", "Basic-Statistics",
        "Operation-Research", "Optimization-Electricity-Dispatching",
        "Forecasting-Covid-19-Cases-Dynamic-Model", "Ensemble-Classification",
        "Pyhton-Introduction-Tutorial-Class"],
    "Control and robotics": [n for n, _ in STARRED] + [
        "Control-Ball-and-Beam-System", "Robotic-Finger-Gesture-Emulation"],
    "Software and embedded": [
        "Local-Messenger", "Pacman-Game", "Restaurant-Orders-Management-App",
        "ARM-Frequency-Meter", "ARM-Weight-Distance-Temperature-Meter",
        "Piplined-ARM", "Recursive-Programming"],
}
# Repos whose GitHub language is empty but whose code is clearly one language.
LANG_OVERRIDE = {"Control-Position-Velocity-DC-Motor": "MATLAB", "Robotic-Arm-Simulation": "MATLAB"}
# Hand-written one-liners for repos with no (or a rough) GitHub description.
ABOUT_OVERRIDE = {
    "practice_rag_production": "A production-style agentic RAG system over arXiv papers: hybrid search, a local LLM that cites its sources, and tracing.",
    "budget-buddy": "An AI budgeting agent built with Google ADK and a custom MCP server. Math in code, judgment in the LLM.",
    "agentic_coding": "A 12-week course on building web software safely with a coding agent.",
    "mca_linear_registration": "Numerical stability of widely used linear MRI registration tools. The code behind my arXiv paper.",
    "gsoc-qc-studio-report": "My Google Summer of Code 2026 report on QC-Studio.",
}


def gh(*args):
    out = subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def banner():
    w, h = 1000, 260
    rng = random.Random(11)
    pts = []
    while len(pts) < 36:
        x, y = rng.uniform(570, 965), rng.uniform(22, 238)
        if all((x - px) ** 2 + (y - py) ** 2 > 46 ** 2 for px, py in pts):
            pts.append((x, y))
    parts = []
    for i, (x1, y1) in enumerate(pts):
        for x2, y2 in pts[i + 1:]:
            d = math.hypot(x1 - x2, y1 - y2)
            if d < 110:
                parts.append(
                    f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
                    f'stroke="#f5d0fe" stroke-opacity="{0.38 - d / 400:.2f}" stroke-width="1.2"/>')
    for i, (x, y) in enumerate(pts):
        pink = i % 6 == 0
        parts.append(
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rng.uniform(2.6, 5.4):.1f}" '
            f'fill="{"#f9a8d4" if pink else "#ffffff"}" fill-opacity="{0.9 if pink else 0.7}"/>')
    net = "\n  ".join(parts)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Niusha Mirhakimi, ML/AI engineer">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1e1b4b"/>
      <stop offset="0.55" stop-color="#5b21b6"/>
      <stop offset="1" stop-color="#be185d"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.82" cy="0.45" r="0.55">
      <stop offset="0" stop-color="#f0abfc" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#f0abfc" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{w}" height="{h}" rx="18" fill="url(#bg)"/>
  <rect width="{w}" height="{h}" rx="18" fill="url(#glow)"/>
  {net}
  <text x="56" y="118" font-family="{FONT}" font-size="50" font-weight="700" fill="#ffffff">Niusha Mirhakimi</text>
  <text x="58" y="162" font-family="{FONT}" font-size="23" font-weight="500" fill="#f5d0fe">ML/AI Engineer</text>
  <text x="58" y="200" font-family="{FONT}" font-size="16" fill="#e9d5ff">Neuroimaging  ·  Reproducible research  ·  LLM agents</text>
</svg>
'''


def stats_strip(n_repos, n_stars, n_prs, n_pr_repos):
    tiles = [
        (str(n_repos), "original public repos"),
        (str(n_stars), "stars earned"),
        (str(n_prs), f"merged PRs in {n_pr_repos} other projects"),
        ("GSoC '26", "INCF  ·  QC-Studio"),
    ]
    w, h, tw, gap = 1000, 100, 235, 20
    out = []
    for i, (big, small) in enumerate(tiles):
        x = i * (tw + gap)
        cx = x + tw / 2
        out.append(
            f'<rect x="{x}" y="1" width="{tw}" height="{h - 2}" rx="14" fill="{CARD_BG}" stroke="{CARD_BORDER}"/>'
            f'<text x="{cx}" y="50" text-anchor="middle" font-family="{FONT}" font-size="32" font-weight="700" fill="{TITLE}">{escape(big)}</text>'
            f'<text x="{cx}" y="76" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{TEXT}">{escape(small)}</text>')
    body = "\n  ".join(out)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="GitHub activity summary">\n  {body}\n</svg>\n')


def projects_page(originals):
    by_name = {r["name"]: r for r in originals}
    placed = {n for names in GROUPS.values() for n in names}
    groups = dict(GROUPS)
    leftovers = sorted(set(by_name) - placed)
    if leftovers:
        groups["Other"] = leftovers
    out = ["# Projects", "",
           "[← Back to profile](README.md)", "",
           "All of my original public repositories, grouped by topic. Most of the older ones are from 2021 "
           "and earlier, built in MATLAB, Python, C and C++.", ""]
    for title, names in groups.items():
        rows = [by_name[n] for n in names if n in by_name]
        if not rows:
            continue
        out += [f"## {title}", "", "| Repository | Language | Stars | About |", "|---|---|---|---|"]
        for r in rows:
            lang = LANG_OVERRIDE.get(r["name"]) or (r["primaryLanguage"] or {}).get("name", "")
            about = ABOUT_OVERRIDE.get(r["name"]) or " ".join((r["description"] or "").split())
            about = about.replace("|", "\\|")
            out.append(f"| [{r['name']}]({r['url']}) | {lang} | {r['stargazerCount'] or ''} | {about} |")
        out.append("")
    return "\n".join(out)


def starred_section(by_name):
    lines = ["<!-- starred:start -->", "## Starred projects", ""]
    for name, blurb in STARRED:
        r = by_name[name]
        lines.append(f"- **[{name}]({r['url']})** · ⭐ {r['stargazerCount']}<br>{blurb}")
    lines.append("<!-- starred:end -->")
    return "\n".join(lines)


def update_readme(by_name):
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r"<!-- starred:start -->.*?<!-- starred:end -->", re.S)
    if not pattern.search(text):
        raise SystemExit("README.md is missing the <!-- starred:start/end --> markers")
    path.write_text(pattern.sub(lambda _: starred_section(by_name), text), encoding="utf-8")


def main():
    repos = gh("repo", "list", USER, "--limit", "200", "--source", "--no-archived",
               "--visibility", "public", "--json", "name,description,stargazerCount,primaryLanguage,url")
    originals = [r for r in repos if r["name"] != USER]
    n_stars = sum(r["stargazerCount"] for r in originals)

    prs = gh("search", "prs", "--author", USER, "--merged", "--limit", "200", "--json", "repository")
    other = [p["repository"]["nameWithOwner"] for p in prs
             if not p["repository"]["nameWithOwner"].startswith(f"{USER}/")]

    write(ASSETS / "banner.svg", banner())
    write(ASSETS / "stats.svg", stats_strip(len(originals), n_stars, len(other), len(set(other))))
    write(ROOT / "PROJECTS.md", projects_page(originals))
    update_readme({r["name"]: r for r in originals})
    print(f"{len(originals)} original repos, {n_stars} stars, {len(other)} merged PRs in {len(set(other))} projects")


if __name__ == "__main__":
    main()

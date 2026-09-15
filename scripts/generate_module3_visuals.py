#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate the topic-specific Module 3 SVG learning visuals.

The diagrams deliberately use different visual models. A sourcing matrix should
look like a matrix, a cost model like a cost model, and a control loop like a
control loop. This prevents a generic workflow template from obscuring the
decision logic being taught.
"""

from __future__ import annotations

import math
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "diagrams" / "module-3"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)

W, H = 1200, 720
INK = "#102a43"
MUTED = "#486581"
BLUE = "#176b87"
TEAL = "#2a9d8f"
GOLD = "#e9b949"
CORAL = "#e76f51"
PALE = "#f4f8fc"
LINE = "#587d96"
WHITE = "#ffffff"


def el(parent: ET.Element, tag: str, **attrs: object) -> ET.Element:
    return ET.SubElement(parent, f"{{{NS}}}{tag}", {k.replace("_", "-"): str(v) for k, v in attrs.items()})


def text(
    parent: ET.Element,
    x: float,
    y: float,
    value: str,
    *,
    cls: str = "body",
    anchor: str = "start",
    max_chars: int | None = None,
    line_height: int = 23,
) -> ET.Element:
    node = el(parent, "text", x=x, y=y, **{"class": cls, "text-anchor": anchor})
    lines = textwrap.wrap(value, width=max_chars, break_long_words=False) if max_chars else [value]
    if not lines:
        lines = [""]
    for i, line in enumerate(lines):
        span = el(node, "tspan", x=x, y=y + i * line_height)
        span.text = line
    return node


def base(title: str, desc: str, eyebrow: str) -> ET.Element:
    root = ET.Element(
        f"{{{NS}}}svg",
        {
            "width": str(W),
            "height": str(H),
            "viewBox": f"0 0 {W} {H}",
            "role": "img",
            "aria-labelledby": "title desc",
        },
    )
    ti = el(root, "title", id="title")
    ti.text = title
    de = el(root, "desc", id="desc")
    de.text = desc
    defs = el(root, "defs")
    grad = el(defs, "linearGradient", id="bg", x1="0", x2="1", y1="0", y2="1")
    el(grad, "stop", offset="0", **{"stop-color": "#f7fafc"})
    el(grad, "stop", offset="1", **{"stop-color": "#eaf3f7"})
    marker = el(defs, "marker", id="arrow", markerWidth="10", markerHeight="10", refX="8", refY="5", orient="auto")
    el(marker, "path", d="M0 0 L10 5 L0 10 Z", fill=MUTED)
    style = el(root, "style")
    style.text = (
        "text{font-family:Arial,Helvetica,sans-serif}.title{font-size:30px;font-weight:700;fill:#102a43}"
        ".eyebrow{font-size:14px;font-weight:700;letter-spacing:1.4px;fill:#176b87}"
        ".subtitle{font-size:16px;fill:#486581}.label{font-size:19px;font-weight:700;fill:#102a43}"
        ".barlabel{font-size:15px;font-weight:700;fill:#fff}"
        ".body{font-size:16px;fill:#243b53}.small{font-size:14px;fill:#486581}"
        ".metric{font-size:24px;font-weight:700;fill:#176b87}.white{fill:#fff}"
        ".line{fill:none;stroke:#587d96;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}"
        ".arrow{fill:none;stroke:#486581;stroke-width:3;stroke-linecap:round;marker-end:url(#arrow)}"
    )
    el(root, "rect", width=W, height=H, rx="24", fill="url(#bg)")
    text(root, 60, 43, eyebrow.upper(), cls="eyebrow")
    text(root, 60, 80, title, cls="title")
    text(root, 60, 109, desc, cls="subtitle", max_chars=112)
    return root


def card(root: ET.Element, x: int, y: int, w: int, h: int, title_: str, body: str = "", color: str = WHITE) -> ET.Element:
    g = el(root, "g")
    el(g, "rect", x=x, y=y, width=w, height=h, rx="16", fill=color, stroke=LINE, **{"stroke-width": 2})
    text(g, x + 20, y + 34, title_, cls="label", max_chars=max(12, int((w - 40) / 10)))
    if body:
        text(g, x + 20, y + 68, body, cls="body", max_chars=max(16, int((w - 40) / 8.3)))
    return g


def badge(root: ET.Element, x: int, y: int, value: str, fill: str = BLUE) -> None:
    el(root, "circle", cx=x, cy=y, r="20", fill=fill)
    text(root, x, y + 6, value, cls="label white", anchor="middle")


def arrow(root: ET.Element, d: str) -> None:
    el(root, "path", d=d, **{"class": "arrow"})


def flow(title_: str, desc: str, labels: list[str], eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    n = len(labels)
    w = int((1060 - (n - 1) * 34) / n)
    y = 275
    for i, label in enumerate(labels):
        x = 60 + i * (w + 34)
        el(root, "rect", x=x, y=y, width=w, height=165, rx="16", fill=WHITE, stroke=LINE, **{"stroke-width": 2})
        badge(root, x + 24, y + 24, str(i + 1), [BLUE, TEAL, GOLD, CORAL, BLUE][i % 5])
        text(root, x + 54, y + 31, label, cls="label", max_chars=max(11, int((w - 66) / 9.5)))
        text(root, x + 20, y + 98, "Retain input, assumption, and owner.", cls="body", max_chars=max(15, int((w - 40) / 8.2)))
        if i < n - 1:
            arrow(root, f"M{x+w+6} {y+82} H{x+w+28}")
    text(root, 60, 515, "Decision rule", cls="label")
    el(root, "rect", x=60, y=535, width=1060, height=90, rx="14", fill="#e6f3f5", stroke=TEAL, **{"stroke-width": 2})
    text(root, 85, 570, "Move forward only when the evidence, accountable owner, and next control are explicit.", cls="body", max_chars=100)
    return root


def matrix(title_: str, desc: str, xlab: str, ylab: str, cells: list[tuple[str, str]], eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    x0, y0, cw, ch = 245, 185, 420, 205
    fills = ["#edf7f6", "#fff7df", "#eef3fa", "#fdeeea"]
    for i, (head, body) in enumerate(cells):
        col, row = i % 2, i // 2
        x, y = x0 + col * cw, y0 + row * ch
        el(root, "rect", x=x, y=y, width=cw, height=ch, fill=fills[i], stroke=WHITE, **{"stroke-width": 8})
        text(root, x + 24, y + 42, head, cls="label", max_chars=34)
        text(root, x + 24, y + 82, body, cls="body", max_chars=43)
    el(root, "line", x1=x0, y1=y0 + 2 * ch + 18, x2=x0 + 2 * cw, y2=y0 + 2 * ch + 18, stroke=INK, **{"stroke-width": 3})
    el(root, "line", x1=x0 - 18, y1=y0 + 2 * ch, x2=x0 - 18, y2=y0, stroke=INK, **{"stroke-width": 3})
    text(root, x0 + cw, y0 + 2 * ch + 56, xlab, cls="label", anchor="middle")
    text(root, 85, y0 + ch, ylab, cls="label", anchor="middle", max_chars=15)
    text(root, x0, y0 + 2 * ch + 42, "LOW", cls="small")
    text(root, x0 + 2 * cw, y0 + 2 * ch + 42, "HIGH", cls="small", anchor="end")
    text(root, x0 - 42, y0 + 2 * ch, "LOW", cls="small", anchor="end")
    text(root, x0 - 42, y0 + 14, "HIGH", cls="small", anchor="end")
    return root


def spectrum(title_: str, desc: str, labels: list[tuple[str, str]], left: str, right: str, eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    y = 340
    el(root, "line", x1=110, y1=y, x2=1090, y2=y, stroke=LINE, **{"stroke-width": 14, "stroke-linecap": "round"})
    for i, (head, body) in enumerate(labels):
        x = 140 + i * (920 / max(1, len(labels) - 1))
        el(root, "circle", cx=x, cy=y, r=24, fill=[BLUE, TEAL, GOLD, CORAL, BLUE][i % 5], stroke=WHITE, **{"stroke-width": 5})
        above = i % 2 == 0
        cy = 175 if above else 430
        card(root, int(x - 110), cy, 220, 120, head, body, "#ffffff")
        el(root, "line", x1=x, y1=y + (-25 if above else 25), x2=x, y2=cy + (120 if above else 0), stroke=LINE, **{"stroke-width": 2})
    text(root, 100, 610, left, cls="label")
    text(root, 1100, 610, right, cls="label", anchor="end")
    arrow(root, "M320 603 H880")
    return root


def timeline(title_: str, desc: str, stages: list[tuple[str, str]], eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    y = 355
    arrow(root, "M100 355 H1090")
    gap = 940 / (len(stages) - 1)
    for i, (head, body) in enumerate(stages):
        x = 120 + i * gap
        el(root, "circle", cx=x, cy=y, r=22, fill=[BLUE, TEAL, GOLD, CORAL, BLUE][i % 5])
        badge(root, int(x), y, str(i + 1), [BLUE, TEAL, GOLD, CORAL, BLUE][i % 5])
        cy = 175 if i % 2 == 0 else 415
        card(root, int(x - 105), cy, 210, 120, head, body)
        el(root, "line", x1=x, y1=y + (-24 if i % 2 == 0 else 24), x2=x, y2=cy + (120 if i % 2 == 0 else 0), stroke=LINE, **{"stroke-width": 2})
    return root


def hierarchy(title_: str, desc: str, levels: list[tuple[str, str]], eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    widths = [360, 560, 760, 960]
    for i, (head, body) in enumerate(levels):
        w = widths[min(i, len(widths) - 1)]
        x = (W - w) // 2
        y = 165 + i * 120
        el(root, "rect", x=x, y=y, width=w, height=90, rx="16", fill=["#dceef2", "#e7f5f2", "#fff4d6", "#fde9e4"][i % 4], stroke=LINE, **{"stroke-width": 2})
        text(root, x + 24, y + 34, head, cls="label", max_chars=28)
        text(root, x + 24, y + 65, body, cls="small", max_chars=max(28, int((w - 48) / 7.3)))
        if i < len(levels) - 1:
            arrow(root, f"M600 {y+92} V{y+114}")
    return root


def cost_stack(title_: str, desc: str, items: list[tuple[str, int, str]], eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    maximum = max(v for _, v, _ in items)
    x, y = 330, 170
    for i, (label, value, note) in enumerate(items):
        w = 200 + int(280 * value / maximum)
        fill = [BLUE, TEAL, GOLD, CORAL, MUTED][i % 5]
        el(root, "rect", x=x, y=y + i * 82, width=w, height=68, rx="10", fill=fill)
        text(root, x + 18, y + 27 + i * 82, label, cls="barlabel", max_chars=24)
        text(root, 835, y + 39 + i * 82, f"{value}%", cls="metric")
        text(root, 915, y + 39 + i * 82, note, cls="small", max_chars=26)
    text(root, 100, 210, "Visible price", cls="label")
    arrow(root, "M190 230 V555")
    text(root, 100, 600, "Full economic exposure", cls="label", max_chars=18)
    return root


def waterfall(title_: str, desc: str, items: list[tuple[str, int]], eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    x0, basey, scale = 110, 580, 4.0
    cumulative = 0
    bw, gap = 125, 28
    for i, (label, value) in enumerate(items):
        x = x0 + i * (bw + gap)
        start = cumulative
        cumulative += value
        y = basey - max(start, cumulative) * scale
        h = abs(value) * scale
        fill = TEAL if value >= 0 else CORAL
        el(root, "rect", x=x, y=y, width=bw, height=max(h, 3), rx="6", fill=fill)
        text(root, x + bw / 2, y - 12, f"{value:+}", cls="label", anchor="middle")
        text(root, x + bw / 2, 615, label, cls="small", anchor="middle", max_chars=15)
        if i < len(items) - 1:
            el(root, "line", x1=x + bw, y1=basey - cumulative * scale, x2=x + bw + gap, y2=basey - cumulative * scale, stroke=LINE, **{"stroke-width": 2, "stroke-dasharray": "5 5"})
    x = x0 + len(items) * (bw + gap)
    total_h = cumulative * scale
    el(root, "rect", x=x, y=basey - total_h, width=bw, height=total_h, rx="6", fill=BLUE)
    text(root, x + bw / 2, basey - total_h - 12, str(cumulative), cls="metric", anchor="middle")
    text(root, x + bw / 2, 615, "Should cost", cls="small", anchor="middle")
    text(root, 80, 160, "Should-cost bridge", cls="label")
    text(root, 80, 190, "Build from transparent cost drivers; negotiate the assumptions, not only the final price.", cls="body", max_chars=58)
    return root


def cycle(title_: str, desc: str, labels: list[tuple[str, str]], center: str, eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    cx, cy, radius = 600, 385, 220
    n = len(labels)
    for i, (head, body) in enumerate(labels):
        a = -math.pi / 2 + 2 * math.pi * i / n
        x, y = cx + radius * math.cos(a), cy + radius * math.sin(a)
        nx, ny = cx + radius * math.cos(a + 2 * math.pi / n), cy + radius * math.sin(a + 2 * math.pi / n)
        arrow(root, f"M{x:.1f} {y:.1f} Q{cx:.1f} {cy:.1f} {nx:.1f} {ny:.1f}")
        el(root, "rect", x=int(x - 95), y=int(y - 55), width=190, height=110, rx="16", fill=WHITE, stroke=LINE, **{"stroke-width": 2})
        badge(root, int(x - 70), int(y - 31), str(i + 1), [BLUE, TEAL, GOLD, CORAL, MUTED][i % 5])
        text(root, int(x - 40), int(y - 24), head, cls="label", max_chars=15)
        text(root, int(x - 75), int(y + 13), body, cls="body", max_chars=19)
    el(root, "circle", cx=cx, cy=cy, r="92", fill="#dceef2", stroke=BLUE, **{"stroke-width": 3})
    text(root, cx, cy - 8, center, cls="label", anchor="middle", max_chars=15)
    return root


def taxonomy(title_: str, desc: str, root_label: str, branches: list[tuple[str, list[str]]], eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    card(root, 430, 150, 340, 90, root_label, "Decision-ready taxonomy")
    cols = len(branches)
    for i, (head, leaves) in enumerate(branches):
        x = 80 + i * (1040 / cols)
        w = int(920 / cols)
        cx = x + w / 2
        el(root, "path", d=f"M600 240 V275 H{cx:.0f} V305", **{"class": "line"})
        card(root, int(x), 305, w, 90, head, "")
        for j, leaf in enumerate(leaves):
            ly = 430 + j * 72
            el(root, "line", x1=cx, y1=395, x2=cx, y2=ly, stroke=LINE, **{"stroke-width": 2})
            el(root, "rect", x=x + 12, y=ly, width=w - 24, height=52, rx="10", fill="#eef4f8", stroke=LINE)
            text(root, cx, ly + 31, leaf, cls="body", anchor="middle", max_chars=max(12, int(w / 8)))
    return root


def funnel(title_: str, desc: str, stages: list[tuple[str, str]], outcome: str, eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    y = 165
    for i, (head, body) in enumerate(stages):
        x = 140 + i * 75
        w = 920 - i * 150
        el(root, "polygon", points=f"{x},{y+i*92} {x+w},{y+i*92} {x+w-55},{y+70+i*92} {x+55},{y+70+i*92}", fill=["#dceef2", "#dff3ef", "#fff0ca", "#fbe2dc"][i % 4], stroke=LINE, **{"stroke-width": 2})
        text(root, 600, y + 29 + i * 92, head, cls="label", anchor="middle")
        text(root, 600, y + 54 + i * 92, body, cls="small", anchor="middle", max_chars=max(22, int((w - 90) / 7.3)))
    el(root, "rect", x=410, y=565, width=380, height=70, rx="18", fill=BLUE)
    text(root, 600, 607, outcome, cls="label white", anchor="middle", max_chars=32)
    arrow(root, "M600 535 V560")
    return root


def split_compare(title_: str, desc: str, left: tuple[str, list[str]], right: tuple[str, list[str]], center: str, eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    for x, data, fill in [(70, left, "#e8f4f6"), (650, right, "#fff2df")]:
        head, bullets = data
        el(root, "rect", x=x, y=170, width=480, height=420, rx="20", fill=fill, stroke=LINE, **{"stroke-width": 2})
        text(root, x + 240, 215, head, cls="title", anchor="middle", max_chars=28)
        for i, item in enumerate(bullets):
            badge(root, x + 42, 278 + i * 78, str(i + 1), BLUE if x < 100 else CORAL)
            text(root, x + 78, 272 + i * 78, item, cls="body", max_chars=40)
    el(root, "circle", cx=600, cy=380, r="48", fill=WHITE, stroke=INK, **{"stroke-width": 3})
    text(root, 600, 374, center, cls="label", anchor="middle", max_chars=8)
    return root


def dashboard(title_: str, desc: str, metrics: list[tuple[str, str, str]], controls: list[str], eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    for i, (value, label, note) in enumerate(metrics):
        x = 65 + i * 275
        el(root, "rect", x=x, y=165, width=245, height=145, rx="16", fill=WHITE, stroke=LINE, **{"stroke-width": 2})
        text(root, x + 20, 207, value, cls="metric")
        text(root, x + 20, 239, label, cls="label", max_chars=22)
        text(root, x + 20, 280, note, cls="small", max_chars=28)
    el(root, "rect", x=65, y=350, width=1070, height=245, rx="18", fill="#eef4f8", stroke=LINE, **{"stroke-width": 2})
    text(root, 90, 392, "Management controls", cls="label")
    for i, item in enumerate(controls):
        x = 100 + (i % 2) * 520
        y = 440 + (i // 2) * 72
        el(root, "rect", x=x, y=y, width=470, height=52, rx="12", fill=WHITE, stroke=LINE)
        badge(root, x + 26, y + 26, str(i + 1), [BLUE, TEAL, GOLD, CORAL][i % 4])
        text(root, x + 60, y + 31, item, cls="body", max_chars=45)
    return root


def triangle(title_: str, desc: str, nodes: list[tuple[str, str]], center: str, eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    pts = [(600, 175), (260, 545), (940, 545)]
    el(root, "polygon", points="600,245 335,515 865,515", fill="#e8f4f6", stroke=LINE, **{"stroke-width": 3})
    for i, ((head, body), (x, y)) in enumerate(zip(nodes, pts)):
        el(root, "rect", x=x - 135, y=y - 55, width=270, height=110, rx="16", fill=WHITE, stroke=LINE, **{"stroke-width": 2})
        badge(root, x - 108, y - 31, str(i + 1), [BLUE, TEAL, GOLD][i])
        text(root, x - 76, y - 24, head, cls="label", max_chars=22)
        text(root, x - 115, y + 14, body, cls="body", max_chars=29)
    el(root, "circle", cx=600, cy=425, r="86", fill=WHITE, stroke=BLUE, **{"stroke-width": 3})
    text(root, 600, 415, center, cls="label", anchor="middle", max_chars=15)
    return root


def ecosystem(title_: str, desc: str, center: str, nodes: list[tuple[str, str]], eyebrow: str) -> ET.Element:
    root = base(title_, desc, eyebrow)
    cx, cy = 600, 390
    el(root, "circle", cx=cx, cy=cy, r="105", fill="#dceef2", stroke=BLUE, **{"stroke-width": 3})
    text(root, cx, cy - 10, center, cls="label", anchor="middle", max_chars=16)
    for i, (head, body) in enumerate(nodes):
        a = -math.pi / 2 + 2 * math.pi * i / len(nodes)
        x, y = cx + 330 * math.cos(a), cy + 205 * math.sin(a)
        arrow(root, f"M{cx + 110*math.cos(a):.0f} {cy + 110*math.sin(a):.0f} L{x - 105*math.cos(a):.0f} {y - 60*math.sin(a):.0f}")
        card(root, int(x - 115), int(y - 60), 230, 120, head, body)
    return root


def save(section: str, filename: str, root: ET.Element) -> None:
    target = OUT / section / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    ET.indent(root, space="  ")
    target.write_text(ET.tostring(root, encoding="unicode") + "\n", encoding="utf-8")


def build() -> None:
    diagrams: list[tuple[str, str, ET.Element]] = [
        ("section-a", "01-strategic-sourcing-from-demand-workflow.svg", flow(
            "Strategic Sourcing from Demand", "Translate the demand signal into a governed sourcing decision.",
            ["Validate demand", "Define requirement", "Read supply market", "Choose sourcing route", "Control performance"], "Demand-to-source flow")),
        ("section-a", "02-make-buy-and-core-capability-workflow.svg", matrix(
            "Make, Buy, or Collaborate?", "Separate strategic importance from external supply capability before choosing the boundary.",
            "External supply capability", "Strategic importance",
            [("Make and protect", "Retain control; invest in capability and continuity."), ("Partner selectively", "Use a strategic alliance with protected knowledge."), ("Develop supply or redesign", "Create a viable option without overinvesting internally."), ("Buy competitively", "Use market leverage and clear specifications.")], "Capability boundary matrix")),
        ("section-a", "03-outsourcing-offshoring-and-nearshoring-workflow.svg", spectrum(
            "Location and Ownership Options", "Compare ownership and distance as two separate design choices.",
            [("Internal/local", "Highest control"), ("Outsource/local", "Flexible capacity"), ("Nearshore", "Balanced response"), ("Offshore", "Scale and cost")],
            "Control and proximity", "Scale and labor advantage", "Footprint spectrum")),
        ("section-a", "04-transition-risk-and-knowledge-retention-workflow.svg", timeline(
            "Transition Risk and Knowledge Retention", "Protect service and know-how across the full transfer window.",
            [("Baseline", "Map process and failure modes"), ("Shadow", "Supplier observes and rehearses"), ("Parallel run", "Both parties operate"), ("Cutover", "Release by exit criteria"), ("Stabilize", "Track defects and learning")], "Controlled transition")),
        ("section-a", "05-sourcing-requirements-and-timing-workflow.svg", hierarchy(
            "Sourcing Requirements and Timing", "Cascade business intent into a timed, testable sourcing package.",
            [("Business need", "Demand, service promise, risk appetite"), ("Category requirement", "Scope, volumes, constraints, target economics"), ("Supplier specification", "Technical, quality, logistics, compliance"), ("Sourcing calendar", "Market test, award, qualification, launch")], "Requirement cascade")),
        ("section-a", "06-landed-cost-and-total-cost-of-ownership-workflow.svg", cost_stack(
            "Landed Cost and Total Cost of Ownership", "Look beyond unit price to the cost created across the relationship lifecycle.",
            [("Unit price", 42, "Quoted purchase value"), ("Logistics and duties", 18, "Freight, handling, tariff"), ("Inventory and working capital", 15, "Pipeline and buffers"), ("Quality and disruption", 14, "Failure and recovery"), ("Lifecycle and exit", 11, "Change, disposal, switching")], "Cost exposure stack")),
        ("section-a", "07-should-cost-and-business-case-workflow.svg", waterfall(
            "Should-Cost and Business-Case Bridge", "Reconcile technical cost drivers with risk-adjusted commercial value.",
            [("Material", 38), ("Conversion", 20), ("Overhead", 12), ("Logistics", 8), ("Risk", 6), ("Productivity", -5)], "Transparent cost bridge")),

        ("section-b", "01-supply-plan-governance-workflow.svg", cycle(
            "Supply Plan Governance", "Turn market evidence into owned actions and controlled refresh decisions.",
            [("Sense", "Demand and supply signals"), ("Frame", "Assumptions and scenarios"), ("Decide", "Route and allocation"), ("Commit", "Owners and dates"), ("Review", "Variance and triggers")], "Approved supply plan", "Governance cycle")),
        ("section-b", "02-category-architecture-workflow.svg", taxonomy(
            "Category Architecture", "Build a taxonomy that supports spend visibility, accountability, and strategy.", "Enterprise spend",
            [("Direct", ["Raw materials", "Components", "Packaging"]), ("Indirect", ["Facilities", "IT and services", "MRO"]), ("Logistics", ["Transport", "Warehousing", "Brokerage"])], "Category tree")),
        ("section-b", "03-portfolio-analysis-workflow.svg", matrix(
            "Supply Portfolio Analysis", "Segment categories using profit impact and supply risk—not spend alone.",
            "Profit impact", "Supply risk",
            [("Bottleneck", "Secure supply, reduce dependency, carry options."), ("Strategic", "Collaborate, govern jointly, protect continuity."), ("Noncritical", "Simplify, automate, standardize demand."), ("Leverage", "Aggregate volume and use market competition.")], "Portfolio matrix")),
        ("section-b", "04-supplier-attractiveness-and-segmentation-workflow.svg", matrix(
            "Supplier Attractiveness and Segmentation", "Combine how much the supplier matters to you with how much you matter to the supplier.",
            "Supplier value to buyer", "Buyer attractiveness to supplier",
            [("Develop access", "Improve account attractiveness and executive connection."), ("Strategic fit", "Joint roadmap, innovation, and risk governance."), ("Transactional", "Standard controls and competitive alternatives."), ("Manage dependence", "Protect leverage and qualify options.")], "Two-way relationship matrix")),
        ("section-b", "05-relationship-models-workflow.svg", spectrum(
            "Supplier Relationship Models", "Match governance intensity to interdependence and switching difficulty.",
            [("Transactional", "Price and conformance"), ("Preferred", "Performance improvement"), ("Collaborative", "Joint planning"), ("Strategic", "Shared investment")],
            "Low interdependence", "High interdependence", "Relationship continuum")),
        ("section-b", "06-spend-analysis-and-market-intelligence-workflow.svg", funnel(
            "Spend Analysis and Market Intelligence", "Convert fragmented transactions into a category decision base.",
            [("Collect", "PO, invoice, contract, supplier, and demand data"), ("Clean and classify", "Normalize names, units, currencies, and taxonomy"), ("Enrich", "Add market capacity, cost drivers, and risk signals"), ("Prioritize", "Size value pools and decision urgency")], "Category opportunity map", "Evidence funnel")),
        ("section-b", "07-supply-base-right-sizing-workflow.svg", split_compare(
            "Supply-Base Right-Sizing", "Balance aggregation benefits against resilience and capacity constraints.",
            ("Consolidate", ["Increase leverage", "Reduce interfaces", "Standardize specifications", "Deepen supplier investment"]),
            ("Diversify", ["Protect continuity", "Create capacity options", "Reduce geographic exposure", "Preserve competitive tension"]), "BALANCE", "Supply-base design")),

        ("section-c", "01-design-as-economic-lever-workflow.svg", ecosystem(
            "Design as an Economic Lever", "Product choices create recurring effects across cost, service, risk, and sustainability.", "Design decision",
            [("Cost", "Material and conversion"), ("Service", "Availability and repair"), ("Risk", "Dependency and volatility"), ("Cash", "Inventory and cycle time"), ("Sustainability", "Energy and recovery")], "Lifecycle economics")),
        ("section-c", "02-collaborative-design-and-early-involvement-workflow.svg", timeline(
            "Collaborative Design and Early Supplier Involvement", "Place supplier knowledge before the design freedom closes.",
            [("Concept", "Invite capability options"), ("Architecture", "Trade modules and interfaces"), ("Detail design", "Validate tolerances and process"), ("Industrialize", "Prove tooling and capacity"), ("Launch", "Control changes and learning")], "Early involvement stage gates")),
        ("section-c", "03-design-for-supply-chain-and-logistics-workflow.svg", dashboard(
            "Design for Supply Chain and Logistics", "Use cross-functional measures to expose downstream design consequences.",
            [("−18%", "Pack cube", "Space per sellable unit"), ("−12 days", "Lead time", "Supply response"), ("+1", "Source options", "Qualified alternatives"), ("−22%", "Damage", "Handling exposure")],
            ["Approve packaging against transport lanes", "Validate material availability and source depth", "Test postponement and inventory placement", "Record owners for unresolved trade-offs"], "Design scorecard")),
        ("section-c", "04-standardization-commonality-and-universality-workflow.svg", hierarchy(
            "Standardization, Commonality, and Universality", "Move from shared rules to reusable parts and broad application.",
            [("Standardization", "Common specifications, methods, and interfaces"), ("Commonality", "Shared components across product families"), ("Universality", "One solution usable across markets or variants"), ("Economic result", "Lower complexity with controlled differentiation")], "Complexity reduction layers")),
        ("section-c", "05-modular-versus-integral-design-workflow.svg", split_compare(
            "Modular versus Integral Design", "Choose the architecture by weighing interface flexibility against optimized system performance.",
            ("Modular", ["Defined interfaces", "Independent replacement", "Variant flexibility", "Easier supplier substitution"]),
            ("Integral", ["Coupled functions", "System-level optimization", "Fewer interface compromises", "Higher switching effort"]), "TRADE-OFF", "Architecture comparison")),
        ("section-c", "06-simplification-dfma-and-serviceability-workflow.svg", funnel(
            "Simplification, DFMA, and Serviceability", "Remove avoidable complexity before optimizing the remaining work.",
            [("Challenge", "Question every part, fastening method, and tolerance"), ("Combine", "Integrate functions where risk stays controlled"), ("Simplify", "Reduce motions, tools, orientations, and variants"), ("Service test", "Verify access, diagnosis, replacement, and recovery")], "Lower lifecycle effort", "Design simplification funnel")),
        ("section-c", "07-quality-qfd-and-robust-design-workflow.svg", matrix(
            "Quality Function Deployment and Robust Design", "Translate customer priorities into technical responses and test robustness against noise.",
            "Technical response strength", "Customer importance",
            [("Critical gap", "Escalate weak technical coverage immediately."), ("Design priority", "Allocate tolerance, testing, and ownership."), ("Monitor", "Keep evidence without overengineering."), ("Optimize selectively", "Strengthen only where lifecycle value supports it.")], "Quality translation matrix")),
        ("section-c", "08-postponement-mass-customization-and-localization-workflow.svg", hierarchy(
            "Postponement and Mass Customization", "Keep common inventory upstream and delay differentiation until demand is clearer.",
            [("Common platform", "Shared materials and stable base configuration"), ("Decoupling point", "Place inventory before uncertainty branches"), ("Late differentiation", "Configure, label, package, or localize to order"), ("Customer variants", "Deliver variety without duplicating the full pipeline")], "Postponement architecture")),
        ("section-c", "09-circular-and-sustainable-design-workflow.svg", cycle(
            "Circular and Sustainable Design", "Design the reverse path together with the forward product flow.",
            [("Source", "Responsible material"), ("Make", "Efficient conversion"), ("Use", "Durable and repairable"), ("Recover", "Collect and inspect"), ("Loop", "Reuse, remanufacture, recycle")], "Lifecycle value", "Circular design loop")),

        ("section-d", "01-purchasing-flow-and-selection-routes-workflow.svg", flow(
            "Purchasing Flow and Selection Routes", "Use the requirement and market condition to choose the correct commercial route.",
            ["Need and specification", "Route decision", "Supplier evaluation", "Award and approval", "Order and control"], "Source-to-order route")),
        ("section-d", "02-supplier-criteria-and-scorecards-workflow.svg", dashboard(
            "Supplier Criteria and Scorecards", "Combine weighted selection evidence with hard qualification gates.",
            [("30%", "Quality", "Capability and defect control"), ("25%", "Delivery", "Capacity and reliability"), ("25%", "Commercial", "TCO and transparency"), ("20%", "Risk and ESG", "Continuity and compliance")],
            ["Fail any mandatory gate → no award", "Keep scoring scale and evidence source explicit", "Separate evaluator notes from final consensus", "Set post-award measures before signature"], "Weighted scorecard")),
        ("section-d", "03-competitive-bidding-and-direct-negotiation-workflow.svg", split_compare(
            "Competitive Bidding or Direct Negotiation?", "Choose the event format based on specification clarity, market depth, and need for collaboration.",
            ("Competitive bidding", ["Comparable specification", "Several qualified suppliers", "Price discovery matters", "Low solution co-design need"]),
            ("Direct negotiation", ["Unique capability", "Complex or evolving scope", "High switching constraint", "Joint value creation matters"]), "CHOOSE", "Commercial route")),
        ("section-d", "04-principled-negotiation-and-batna-workflow.svg", spectrum(
            "Principled Negotiation and BATNA", "Define the bargaining zone before trading variables across interests.",
            [("Buyer BATNA", "Best outside option"), ("Buyer limit", "Walk-away boundary"), ("Agreement zone", "Tradable value"), ("Supplier limit", "Counterparty boundary"), ("Supplier BATNA", "Their outside option")],
            "Buyer alternative", "Supplier alternative", "Negotiation range")),
        ("section-d", "05-contract-deployment-and-compliance-workflow.svg", cycle(
            "Contract Deployment and Compliance", "A signed agreement creates value only when operational controls use it.",
            [("Translate", "Obligations to controls"), ("Enable", "Catalog, PO, and users"), ("Monitor", "Price, volume, and SLA"), ("Correct", "Leakage and exceptions"), ("Renew", "Evidence-led decision")], "Realized contract value", "Compliance loop")),
        ("section-d", "06-contract-types-and-risk-allocation-workflow.svg", spectrum(
            "Contract Types and Risk Allocation", "Place cost and performance risk with the party best able to control it.",
            [("Cost reimbursable", "Buyer bears cost risk"), ("Time and materials", "Shared exposure"), ("Unit rate", "Volume remains variable"), ("Fixed price", "Supplier bears cost risk"), ("Outcome based", "Payment follows result")],
            "Buyer risk", "Supplier risk", "Risk-allocation continuum")),
        ("section-d", "07-terms-slas-and-incentives-workflow.svg", dashboard(
            "Terms, SLAs, and Incentives", "Connect definitions, measures, consequences, and improvement behavior.",
            [("98.5%", "On-time service", "Window and exclusions defined"), ("≤1.0%", "Defect rate", "Lot and sampling defined"), ("24 h", "Recovery response", "Clock and severity defined"), ("Quarterly", "Gainshare", "Baseline and cap defined")],
            ["Define the data source and calculation", "Assign dispute and escalation paths", "Balance service credits with positive incentives", "Review for gaming and unintended behavior"], "Performance control panel")),
        ("section-d", "08-payment-trade-finance-and-currency-workflow.svg", timeline(
            "Payment, Trade Finance, and Currency", "Map cash, title, documents, and foreign-exchange exposure across the transaction.",
            [("PO", "Currency and Incoterm set"), ("Shipment", "Title and transport risk move"), ("Documents", "Bank and customs evidence"), ("Receipt", "Quantity and quality confirmed"), ("Payment", "Terms and FX settle")], "Cash-and-risk timeline")),
        ("section-d", "09-purchase-orders-and-blanket-orders-workflow.svg", split_compare(
            "Purchase Orders and Blanket Orders", "Match the order instrument to demand frequency and commitment certainty.",
            ("Standard PO", ["Discrete requirement", "Known quantity and date", "Single approval event", "Close after receipt and invoice"]),
            ("Blanket order", ["Repeated demand", "Agreed ceiling and period", "Release-level controls", "Monitor consumption and expiry"]), "FIT", "Order-instrument comparison")),
        ("section-d", "10-receiving-and-three-way-match-workflow.svg", triangle(
            "Receiving and Three-Way Match", "Release payment only when commercial, physical, and invoice evidence agree.",
            [("Purchase order", "What was authorized"), ("Goods receipt", "What physically arrived"), ("Supplier invoice", "What is being charged")], "Match or route exception", "Evidence match")),
        ("section-d", "11-order-tracking-exceptions-and-expediting-workflow.svg", ecosystem(
            "Order Tracking, Exceptions, and Expediting", "Use a control-tower view to act on exceptions instead of chasing every order.", "Exception control tower",
            [("Supplier signal", "Commit and ship status"), ("Demand priority", "Customer and production impact"), ("Material flow", "Transit and receipt"), ("Response", "Recover, reallocate, escalate"), ("Learning", "Root cause and prevention")], "Exception management")),
        ("section-d", "12-digital-procurement-marketplaces-and-auctions-workflow.svg", ecosystem(
            "Digital Procurement, Marketplaces, and Auctions", "Connect transaction channels to common qualification, data, audit, and security controls.", "Digital procurement core",
            [("Catalog", "Guided recurring buy"), ("Supplier portal", "Direct collaboration"), ("Marketplace", "Broad discovery"), ("eAuction", "Structured competition"), ("Analytics", "Spend and compliance")], "Digital channel ecosystem")),
    ]

    for section, filename, diagram in diagrams:
        save(section, filename, diagram)
    print(f"Generated {len(diagrams)} topic-specific Module 3 SVG visuals.")


if __name__ == "__main__":
    build()

#!/usr/bin/env python3
"""Behavioral regression checks for BCE/CE boundary placement in generated SVG."""
from pathlib import Path
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
RENDER = ROOT / "scripts" / "render_timeline_svg.py"
SVG_NS = "{http://www.w3.org/2000/svg}"
LABEL = "1 BCE | 1 CE (no year 0)"


def render(start, end):
    result = subprocess.run(
        [sys.executable, str(RENDER), str(start), str(end), "6"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    path = ROOT / "rendered" / (
        f"timeline_v1_foundation_{abs(start)}{'BCE' if start < 0 else 'CE'}_"
        f"{abs(end)}{'BCE' if end < 0 else 'CE'}.svg"
    )
    if not path.is_file():
        raise AssertionError(f"SVG not created: {path}; stdout={result.stdout}")
    return ET.parse(path).getroot()


def boundary_labels(root):
    return [
        node for node in root.iter(f"{SVG_NS}text")
        if (node.text or "").strip() == LABEL
    ]


class BoundaryPlacementTests(unittest.TestCase):
    def test_bce_only_window_excludes_transition(self):
        root = render(-600, -300)
        self.assertEqual(boundary_labels(root), [])

    def test_ce_only_window_excludes_transition(self):
        root = render(100, 200)
        self.assertEqual(boundary_labels(root), [])

    def test_crossing_window_shows_single_visible_transition(self):
        root = render(-10, 10)
        labels = boundary_labels(root)
        self.assertEqual(len(labels), 1)
        width = float(root.attrib["viewBox"].split()[2])
        x = float(labels[0].attrib["x"])
        self.assertGreaterEqual(x, 0)
        self.assertLessEqual(x, width)


if __name__ == "__main__":
    unittest.main()

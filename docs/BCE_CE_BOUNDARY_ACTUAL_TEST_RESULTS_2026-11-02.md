# Actual offline regression execution — 2026-11-02

**VERIFIED PASS** in an isolated Linux/Python 3.13.5 container; no Work, Windows, GitHub Actions, paid services, merge or deployment.

## Authentic source provenance
User supplied the complete ZIP for branch `partner-bce-boundary-review-20261102`. ZIP size 319720 bytes, SHA-256 `d9b1edee8589f62d6342fe4a2e7da70a90525e1ecc8505b7e955331bc331ffaa`, 52 archive entries, ZIP CRC check returned None (no corrupted member). Extracted it and verified exact local Git blob SHAs against authenticated current GitHub reads:
- `scripts/render_timeline_svg.py` `51234aae31068fb830d8959834f6591d15533a94`
- `scripts/test_bce_ce_boundary.py` `a9fdc6e9dfba0102d5ec3398d69fb3db5256975f`
- `scripts/test_render_contract.py` `2a1fbfe6950738eca88d249ba4a48fb83b400acb`

## Executed commands and actual exit codes
```
python scripts/test_bce_ce_boundary.py
exit: 0
stdout: (empty)
stderr:
...
----------------------------------------------------------------------
Ran 3 tests in 4.501s

OK
```

```
python scripts/test_render_contract.py
exit: 0
stderr: (empty)
stdout:
PASS SVG output
PASS canonical entities input
PASS canonical date claims input
PASS provenance IDs in tooltips
PASS evidence-class encoding
PASS configurable window
PASS reject explicit year-zero bounds
PASS vector text retained
PASS no raster canvas
PASS old five-track cap absent
PASS crowded marks are not dropped
PASS historical coordinate transform exists
PASS year zero coordinate rejected
PASS date fallback uses explicit None checks
PASS render-contract static gate: 14 checks
```

The three actual behavioral tests generate BCE-only, CE-only and crossing-window SVG outputs and parse the resulting XML. Their PASS proves the scoped era-label behavior checked by those tests, not correctness of all historical dates or the whole renderer.

## Decision
Scoped regression gate PASSED (3/3 actual behavioral + 14/14 actual static). Main unchanged; branch remains unmerged and undeployed. Next bounded action: inspect exact review-branch diff and decide separately whether to open/merge an approved pull request. No further file changes needed for this narrow fix.

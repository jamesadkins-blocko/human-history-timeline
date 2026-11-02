# Review evidence — BCE/CE boundary correction (2026-11-02)

Scope: minimal approved source/test change on this review branch only. Main remains untouched. No workflow was dispatched, no merge/deployment or Windows changes.

Source baseline: main 53ba5275e3b6aeebe1336ba72ba86a8b5c5a56f0.
Provenance: historical successful SVG build 37612299764 artifact 11477858979; PARTNER artifact review records out-of-window boundary label x=7559 beyond 600–300 BCE SVG canvas width=4040.

Changes:
- `scripts/render_timeline_svg.py` blob `51234aae31068fb830d8959834f6591d15533a94`: only generate the boundary and label if `START <= -1 and END >= 1`. The historical coordinate transform is unchanged.
- `scripts/test_bce_ce_boundary.py` blob `a9fdc6e9dfba0102d5ec3398d69fb3db5256975f`: standard-library subprocess + ElementTree behavioral cases: entirely BCE, entirely CE, and boundary-crossing SVG output. All are based on canonical repository data and create only local generated SVG derivatives when executed.

Verification performed via authenticated GitHub read-back:
- Both current source blobs matched the returned commit blobs.
- Guard/indentation exact pattern and test entrypoints inspected.
- Seven deterministic boolean guard truth-table cases PASS: (-600,-300), (100,200), (-10,10), (-1500,500), (-1,1), (-100,-1), (1,100).
- The test file genuinely calls the renderer subprocess and parses generated SVG XML.
- **Actual Python rendering tests were NOT executed** in this session; no runtime PASS assertion is made. Integration tests and Actions remain pending for later approved execution. The source-code guard check is not a replacement for executing the real tests.

Suggested local validation command once explicitly allowed in a suitable sandbox: `python scripts/test_bce_ce_boundary.py` followed by `python scripts/test_render_contract.py`. Avoid triggering CI automatically without cost verification.

Pending: independent Python test run, reviewer approval and any integration/merge. No additional project code or data changes were authorized.

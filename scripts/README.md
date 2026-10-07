# Build and Validation Scripts

The pipeline will validate normalized CSV data and generate derived releases.

Required checks:
- unique IDs
- valid foreign keys
- no normalized year 0
- source references resolve
- competing date claims remain distinct
- person/text/manuscript/artifact separation
- duplicate-candidate reporting
- release counts and checksums

Generated spreadsheets and timeline views are outputs; normalized repository data is authoritative.

# Evidence Bundle Format

Assurance evidence should be reproducible and attributable to a specific repository state.

Recommended bundle:

- `repository_commit`
- `generated_at`
- `tool_version`
- `assurance_profile`
- `results[]` with `control_id`, `status`, `evidence`, and `notes`
- checksum of the repository manifest
- unresolved `MANUAL`, `UNKNOWN`, and `WAIVED` items

Allowed result states are `PASS`, `FAIL`, `MANUAL`, `N/A`, `UNKNOWN`, and `WAIVED`.

`UNKNOWN` never implies `PASS`. `MANUAL` requires recorded human evidence before promotion to `PASS`. `WAIVED` requires rationale and an expiration or review date.

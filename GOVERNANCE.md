# Governance

This repository is maintained as a public research-methodology starter kit. Changes should preserve evidence quality, reproducibility, provenance, user safety, and legal clarity.

## Decision model

- Maintainers may merge routine corrections and improvements after verification.
- Changes that alter the research method, evidence model, licensing, provenance rules, or security posture require explicit maintainer review.
- Material methodological changes should state the problem, evidence, tradeoffs, and migration impact.
- Security-sensitive reports should follow `SECURITY.md`.
- Human judgment requirements must not be silently converted into automated PASS results.

## Review expectations

Pull requests should distinguish fact, inference, recommendation, and decision; cite authoritative sources for material claims; state remaining uncertainty; and run the repository verification and assurance checks.

## Releases

A release should be traceable to a repository commit, pass required automated checks, preserve the checksum manifest, and record any unresolved MANUAL, UNKNOWN, or WAIVED assurance items.

# AI-Powered Research Starter Kit

A beginner-friendly framework for conducting rigorous, evidence-driven research with AI assistance.

This project is for people who want the leverage of AI research tools without treating a fluent answer, a search result, or a citation as proof.

> **Licensing notice:** Current v0.2.0+ distributions are proprietary and all rights are reserved. Earlier v0.1.0 distributions were released under CC BY 4.0 and those historical grants are not revoked. See `LICENSE` and `LICENSE_HISTORY.md`.

## The problem

AI can make research dramatically faster. It can search, summarize, compare, organize, brainstorm, and synthesize.

It can also confidently cite material that does not support a claim, repeat secondary sources without checking originals, turn correlation into causation, ignore contradictory evidence, collapse uncertainty into certainty, or convert a plausible interpretation into an accepted fact.

The problem is not that AI cannot help with research. The problem is that **research needs a method for deciding what the evidence actually supports**.

## Revelation is not verification

Telling an LLM, **“Research this and tell me the truth,”** without checking its sources is like starting a religion because one guy woke up from a dream and said:

> **“God told me.”**

No scripture. No witnesses. No corroboration.

Just confidence.

The problem is not that the revelation was not delivered confidently enough. The problem is that a defensible conclusion requires evidence, provenance, corroboration, competing explanations, and a serious attempt to determine whether you might be wrong.

AI can help enormously with that process.

**But it cannot replace the process.**

A second way to think about it:

> Asking an LLM to **“research this and tell me the truth”** without a research methodology is like asking a detective to solve a murder by interviewing one witness and then writing the closing argument.

**One witness is not an investigation. One citation is not a conclusion.**

And asking AI to **“find sources proving I’m right”** is not research methodology.

**It is building a prosecution.**

Three rules worth remembering:

- **Revelation is not verification.**
- **One citation is not a conclusion.**
- **Research the question—not your preferred answer.**

A useful operating principle for AI-assisted research is:

> **AI output is a lead until evidence supports the relevant conclusion.**

## Core rules

> **AI is not a source.**

> **A citation is not evidence until you verify what the source actually says.**

> **AI-generated research is a proposal or synthesis until the underlying evidence supports it.**

> **Do not ask only what supports your hypothesis. Ask what would prove it wrong.**

## The research chain

Important conclusions should be traceable backward:

```text
CONCLUSION
    ↓
CLAIM
    ↓
ARGUMENT
    ↓
EVIDENCE
    ↓
SOURCE
    ↓
SOURCE VERSION / DATE / SNAPSHOT
```

Contradictory evidence belongs on the same claim record.

## Evidence is not authority

This kit deliberately separates:

```text
Research evidence
    ↓
Candidate interpretation
    ↓
Recommendation
    ↓
Accepted decision
```

Research can support a decision. It does not silently become the decision.

## Method selection

Before inventing a new methodology, framework, scoring system, or experiment, use:

**ADOPT → PROFILE → EXTEND → BUILD**

1. **ADOPT** a mature research method or standard when it already fits.
2. **PROFILE** it to the actual research question and risk.
3. **EXTEND** only where a material requirement is not covered.
4. **BUILD** a bespoke method only when there is evidence that mature approaches cannot satisfy a necessary property.

## Research rigor profiles

- **EXPLORATORY** — learning, orientation, brainstorming, and low-consequence investigation.
- **EVIDENCE-BASED** — reports, technical/business decisions, serious synthesis, and claims that need traceability.
- **HIGH ASSURANCE** — consequential domains such as medicine, law, public policy, safety, regulated work, formal scientific review, or other decisions where being wrong could cause major harm.

Profiles change the evidence burden. They are not certificates.

## Download and use it

Current distributions are controlled by the proprietary license in `LICENSE`. Do not copy, redistribute, adapt, or commercialize the current version unless you have written authorization.

Authorized users should follow [`INSTALL_INTO_YOUR_RESEARCH_WORKFLOW.md`](INSTALL_INTO_YOUR_RESEARCH_WORKFLOW.md).

## Current release

**v0.2.0 — Proprietary Baseline**

This release preserves the research methodology while changing the active distribution model from the historical CC BY 4.0 public preview to a proprietary, all-rights-reserved baseline. See `LICENSE_HISTORY.md`.

A deeper standards-reconciliation pass remains planned before a 1.0 release, particularly for domain-specific formal research and high-assurance use.

## Quick start

1. Read `OPEN_THIS_FIRST.md`.
2. Choose a rigor profile.
3. Define the question before searching.
4. Register sources before treating them as evidence.
5. Extract evidence separately from interpretation.
6. Build claims from evidence.
7. Search for contradiction and falsification.
8. Record uncertainty.
9. Keep recommendation separate from accepted decision.
10. Audit the final report.

## License

Copyright © 2026 Kyle Gannon. All Rights Reserved.

Current v0.2.0+ distributions are proprietary. No public license is granted except as expressly stated in a separate written authorization or agreement and subject to rights necessarily arising under applicable law or hosting-platform terms.

Historical v0.1.0 copies distributed under CC BY 4.0 remain governed by that historical grant. See `LICENSE_HISTORY.md`.

## Contributions

Substantive contributions are not accepted as project-owned intellectual property without an appropriate signed contributor, employment, contractor, or IP-assignment agreement. See `CONTRIBUTING.md` and `LEGAL/CONTRIBUTOR_POLICY.md`.

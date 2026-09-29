# Pomni-Of: Agent Design

Status: design proposal for the `AlgorHome/violin` fork. This document maps
what to build and how to measure it. It does not claim that the current plugin
or a model already implements these capabilities.

## Goal and operating contract

Pomni-Of is a model-agnostic, evidence-driven agent for an owned cyber range
or an explicitly scoped assessment. It accepts an objective, scope, tool budget,
time limit, and success condition. It produces a reproducible trace, validated
findings, defender-visible signals, and remediation. The target executor
continues to enforce the approved scope and records receipts. The model may
propose actions; it cannot declare an out-of-scope action admissible.

The improvement target is **reliable progress on unseen multistep exercises**,
not a larger prompt or a count of tools and reference pages. Record failures
as carefully as successes.

## Architecture

| Component | Responsibility | Existing starting point | Add next |
|---|---|---|---|
| Engagement contract | Objective, target, allowed actions, budget, reset and stop conditions | `scope.yaml`, scoped approval | Versioned run manifest and budget counters |
| Orchestrator | Choose next hypothesis, tool, or phase; pause and resume | Pentest skill and PTT | Typed decision record and scheduler |
| Knowledge service | Retrieve dated, cited concepts for the current problem | Routed playbooks | 91-domain index, source registry, freshness and confidence |
| World model | Track assets, identities, trust boundaries, observations and uncertainty | Target and coverage state | Typed fact graph with provenance and expiry |
| Hypothesis board | Compare alternative explanations and next tests | Hypotheses and anti-stuck reference | Predicted observations and information gain |
| Tool broker | Admit and execute bounded actions | `violin_exec`, batch review, receipts | Dry-run metadata, side-effect and cost estimates |
| Evidence service | Bind claims to raw observations and replay | Evidence paths and receipt integrity | Differential proof and reset-linked result |
| Memory | Resume without blending cases or losing decisive facts | Engagement state and checkpoint | Explicit episodic summaries, per-case isolation, stale-fact detection |
| Evaluator | Score task, evidence and process | Duck Store benchmark and scorer | Held-out range tasks, negative controls, trace metrics |
| Learning pipeline | Curate lessons and variants | Retrospective, incident template | Human review, dataset versions, training/eval split |

The model is replaceable. The harness owns the state, tool boundary, evidence,
and scores. A stronger model can be compared on the same held-out tasks without
changing the rules mid-run.

## One decision cycle

1. **Orient.** Read the run manifest, current phase, budget, recent receipts,
   unresolved hypotheses, and known blockers. Reconcile stale or conflicting
   state before another target action.
2. **Model.** Update a small fact graph: `subject`, `relationship`, `object`,
   `source receipt`, `observed_at`, `confidence`, `scope`, and `expires_at`.
   Distinguish observation, inference, and assumption.
3. **Propose.** Generate at least two plausible explanations when evidence is
   ambiguous. For each, predict an observation that would support or refute it.
4. **Select.** Choose the smallest in-scope test expected to reduce uncertainty
   or validate the objective. Consider time, tool cost, rate, side effects,
   reversibility, and defender telemetry. Do not repeat an unchanged failed
   probe.
5. **Admit and execute.** The tool broker checks the action against the run
   manifest, scope, phase, and budget. Record the command, arguments, tool
   version, timestamps, reset ID, raw output path, and receipt.
6. **Interpret.** Decide whether the result supports, rejects, or leaves the
   hypothesis inconclusive, or whether the tool was blocked or failed. A tool
   error is not evidence of a target weakness.
7. **Advance.** Update facts and coverage. Continue, pivot, ask for missing
   scope information, or stop. Validate a finding using an independent or
   differential observation from a reset before reporting it.

Every cycle writes a typed decision record. At context compaction, reconstruct
the working view from records rather than treating a prose summary as ground
truth.

## State transitions

| State | Enter when | Exit condition |
|---|---|---|
| `intake` | New objective | Run manifest and observable success condition exist |
| `orient` | Scope is approved or context resumes | Current facts, budget and blockers reconciled |
| `investigate` | Testable hypotheses exist | A decisive observation, budget limit or blocker |
| `pivot` | Hypothesis rejected, repeated failure or low information gain | New hypothesis and discriminating test chosen |
| `validate` | Candidate finding has initial evidence | Reset-linked reproduction or explicit rejection |
| `report` | Findings and coverage dispositions complete | Evidence-backed report and remediation produced |
| `retrospective` | Report closed | Trace scored and generalizable lessons reviewed |
| `blocked` | Missing scope, tool, environment or approval | Blocker resolved or run terminated |

The state machine supports bounded concurrency for independent *read-only or
lab-safe* hypotheses, but merges results into one canonical fact graph.
Conflicting writes and shared target state require serial execution.

## Capabilities to teach and test

1. **Domain knowledge:** the 91-category coverage index supplies a map of
   concepts, sources, and gaps; knowledge is retrieved with publication date,
   version, confidence, and relevance to the current asset.
2. **System understanding:** code, configuration, topology, identity, data
   flow, trust boundaries, and expected behavior. The agent should explain
   why a suspected weakness is reachable in *this* environment.
3. **Hypothesis discipline:** alternatives, predicted outcomes, controls,
   falsification, and false-positive rejection.
4. **Tool fluency:** selecting tools, interpreting errors, budgeting calls,
   preserving argument boundaries, and understanding side effects.
5. **Long-horizon execution:** checkpoints, resumption, task decomposition,
   dependency tracking, and recovery from partial failure.
6. **Evidence and reporting:** provenance, reset reproduction, minimal proof,
   uncertainty, defender signal, root cause, remediation and retest.
7. **Operational judgment:** scope, stop conditions, sensitive-data handling,
   and an explicit account of actions the agent declined or could not perform.

The high-impact tactics in the supplied taxonomy belong in recognition,
simulation, and defensive evaluation. Do not measure progress by evasion,
unobserved persistence, or extraction from a live third-party environment.

## Knowledge and learning pipeline

- **Sources:** official taxonomy releases, standards, vendor advisories,
  protocol specifications, public incident reports, peer-reviewed work, and
  licensed material. Record exact version, date, rights, and provenance.
- **Transform:** extract factual claims, map to categories and prerequisites,
  include counterexamples and defender signals, deduplicate, redact, and have
  experts review uncertain or consequential material.
- **Retrieval:** query by technology and task. Favor source-grounded material
  over a memorized description; disclose stale or contradictory results.
- **Practice:** construct resettable synthetic variants. Keep the answer and
  private telemetry out of the agent's context during the run.
- **Feedback:** reward verified objective completion, calibrated uncertainty,
  efficient useful tests, and accurate evidence. Penalize unsupported claims,
  repeated dead ends, missed scope boundaries, and answer leakage.
- **Promotion:** freeze dataset and evaluator versions; compare to a baseline
  on held-out families; review regression cases before changing prompts,
  policy, tools, or model weights.

This separates retrieval updates from expensive model training. Do not fine
tune on an evaluation set or interpret a single successful run as general
competence.

## Evaluation suite and release gates

Use three layers: unit tests for state and broker invariants, synthetic tasks
for one failure mode, and multistage ranges with noise and alternative paths.
Include negative controls with no vulnerability, misleading banners, tool
failures, changed versions, and interrupted runs. Split by root cause and
product family to reduce memorization.

Report: objective success at a fixed budget, validated-finding precision,
false-positive rate, time and tool calls, useful pivots, reset reproduction,
coverage, scope violations, blocked-action handling, and defender-signal
quality. Show median and distribution over repeated runs. A run with fabricated
evidence or an out-of-scope action is invalid regardless of task success.

## Implementation order in this repository

1. **Freeze the baseline.** Record model, prompt, tool versions, benchmark
   image digest/reset ID, token and time budget, and current scores.
2. **Add typed decision records.** Extend engagement state without changing
   receipt integrity. Test resume, contradiction, and failed-tool behavior.
3. **Add fact provenance and retrieval.** Attach source IDs, dates, confidence,
   and expiry. Start with a small set of web, identity, cloud, and detection
   cases before scaling to all 91 categories.
4. **Build held-out variants.** Implement the synthetic service-access case
   from `incident-learning.md` with clean telemetry and a negative control.
5. **Add a scheduler.** Rank hypothesis tests by expected information gain,
   cost, and scope; retain a simple deterministic baseline for comparison.
6. **Measure, then train.** Run repeated evaluations. Improve prompts and
   tools first; use curated supervised traces and reinforcement feedback only
   after the scorer resists shortcuts and leakage.
7. **Expand domains deliberately.** Promote a category only when sources,
   lab variants, negative controls, and regression results are reviewed.

The first milestone is a complete, scored, reproducible lab run with one real
finding candidate, one false lead, a reset validation, defender telemetry,
and a report. It is a measurable foundation for broader agentic capability.

## Research basis

The design is an engineering proposal, not a reproduction of any provider's
internal system. It is informed by [UK AISI's multistep cyber-range
evaluations](https://www.aisi.gov.uk/blog/how-do-frontier-ai-agents-perform-in-multi-step-cyber-attack-scenarios),
[Anthropic's realistic range work](https://www.anthropic.com/research/cyber-toolkits-update),
and [OWASP's agentic application security
framework](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
Recheck these sources as the field changes.

# SesameTalk Agent Evals — Public Practice Framework

**Developer Preview.** This is an open-source *practice evaluation* repository, not the private platform's credential issuer.

The public examples demonstrate deterministic, independently scored capability tasks. **Passing these public tests does not grant a SesameTalk badge or any API permission.** The private, protected challenge bank, answer keys, production evidence, grading permissions, evaluator credentials and attestation signing material must never be committed here.

## Current public example

`python.sort.integers`: score a deterministic `sort_integers` implementation on public sample cases. A future production evaluator uses separately held-out problems, isolated identities and immutable evidence bindings; this public repo cannot self-award production credentials.

```bash
python -m unittest discover -s tests -v
python -m sesametalk_agent_evals.practice
```

## Proposed roadmap

- Versioned public challenge schemas, provenance and scorer interfaces
- Safe practice harnesses and reproducible fixture metadata
- Future platform-issued attestations verified independently via **documented public keys** (not implemented)
- Independent certification boundary maintained in private `yunsupj/kkaetalk`

## Boundaries

No hosted production API, no official professional credential, no real grading keys, no paid inference, no agent-controlled badge issuance. License: MIT.

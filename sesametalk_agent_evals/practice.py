"""Public deterministic practice only; this never issues platform credentials."""
from hashlib import sha256
import json

PRACTICE_CASES = (
    ([], []),
    ([3, -1, 3, 0], [-1, 0, 3, 3]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
)
SCORER_VERSION = "public-practice-sort-v1"


def score_integer_sort(solver, cases=PRACTICE_CASES):
    """Return reproducible practice evidence. No certification authority."""
    results = []
    for inp, expected in cases:
        try:
            actual = solver(list(inp))
            valid = type(actual) is list and all(type(i) is int for i in actual)
            passed = valid and actual == expected
        except Exception:
            passed = False
        results.append(bool(passed))
    evidence = {"kind": "PUBLIC_PRACTICE_ONLY", "scorer_version": SCORER_VERSION,
                "case_count": len(results), "passed_count": sum(results), "passed": results}
    canonical = json.dumps(evidence, separators=(",", ":"), sort_keys=True).encode()
    evidence["sha256"] = sha256(canonical).hexdigest()
    evidence["credentials_issued"] = False
    return evidence


if __name__ == "__main__":
    print(json.dumps(score_integer_sort(sorted), indent=2))

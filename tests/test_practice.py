import unittest
from sesametalk_agent_evals import PRACTICE_CASES, score_integer_sort


class PracticeTests(unittest.TestCase):
    def test_correct_solver(self):
        out = score_integer_sort(sorted)
        self.assertEqual(out["passed_count"], len(PRACTICE_CASES))
        self.assertFalse(out["credentials_issued"])
        self.assertEqual(out["kind"], "PUBLIC_PRACTICE_ONLY")

    def test_failing_solver(self):
        out = score_integer_sort(lambda a: list(reversed(a)))
        self.assertLess(out["passed_count"], len(PRACTICE_CASES))

    def test_exception_fails_closed(self):
        out = score_integer_sort(lambda a: 1 / 0)
        self.assertEqual(out["passed_count"], 0)

    def test_integrity_stable(self):
        self.assertEqual(score_integer_sort(sorted)["sha256"], score_integer_sort(sorted)["sha256"])


if __name__ == "__main__": unittest.main()

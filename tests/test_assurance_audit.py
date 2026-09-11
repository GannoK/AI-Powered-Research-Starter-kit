from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("assurance_audit", ROOT / "tools" / "assurance_audit.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class AssuranceAuditTests(unittest.TestCase):
    def test_full_sha(self):
        self.assertTrue(MODULE.is_full_sha("a" * 40))
        self.assertFalse(MODULE.is_full_sha("v4"))
        self.assertFalse(MODULE.is_full_sha("a" * 39))

    def test_rejects_mutable_action_ref(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "workflow.yml"
            path.write_text(
                "permissions: read-all\nsteps:\n"
                "  - uses: actions/checkout@v4\n"
                "    with:\n"
                "      persist-credentials: false\n",
                encoding="utf-8",
            )
            findings = MODULE.workflow_findings(path)
            self.assertTrue(any("unpinned action" in item for item in findings))

    def test_accepts_pinned_checkout_with_explicit_permissions(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "workflow.yml"
            path.write_text(
                "permissions: read-all\nsteps:\n"
                f"  - uses: actions/checkout@{'a' * 40}\n"
                "    with:\n"
                "      persist-credentials: false\n",
                encoding="utf-8",
            )
            self.assertEqual(MODULE.workflow_findings(path), [])


if __name__ == "__main__":
    unittest.main()

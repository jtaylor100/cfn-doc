import os
import shutil
import tempfile
import unittest
from pathlib import Path

from cfn_doc.cfn_doc import main


class MainTest(unittest.TestCase):
    def test_it_generates_document_file(self):
        temp_dir = tempfile.TemporaryDirectory()
        test_dir = Path(__file__).parent
        prime_test_template_path = str((test_dir / "basic-template.yaml").resolve())
        clone_test_template_path = str(
            (Path(temp_dir.name) / "basic-template.yaml").resolve()
        )
        shutil.copyfile(prime_test_template_path, clone_test_template_path)

        main(["cfn-doc", clone_test_template_path])

        expected_doc_path = (Path(temp_dir.name) / "basic-template-doc.md").resolve()
        self.assertTrue(
            os.path.exists(expected_doc_path),
            f"Generated document file not found at {str(expected_doc_path)}",
        )
        temp_dir.cleanup()

    def test_it_outputs_template_title(self):
        temp_dir = tempfile.TemporaryDirectory()
        test_dir = Path(__file__).parent
        prime_test_template_path = str((test_dir / "basic-template.yaml").resolve())
        clone_test_template_path = str(
            (Path(temp_dir.name) / "basic-template.yaml").resolve()
        )
        shutil.copyfile(prime_test_template_path, clone_test_template_path)

        main(["cfn-doc", clone_test_template_path])

        expected_doc_path = (Path(temp_dir.name) / "basic-template-doc.md").resolve()
        with (open(expected_doc_path, "r+")) as f:
            actual_doc = f.read()

        self.assertRegex(actual_doc, "# A sample template")
        temp_dir.cleanup()

import os
import shutil
import tempfile
import unittest
from pathlib import Path

from cfn_doc.cfn_doc import main


class MainTest(unittest.TestCase):
    def test_it_generates_document_file(self):
        test_template_path = self.copy_fixture_to_temp_dir("basic-template.yaml")

        main(["cfn-doc", test_template_path])

        self.assertPathExists(self.applyTempPath("basic-template-doc.md"))

    def test_it_generates_multiple_document_files(self):
        test_template_path = self.copy_fixture_to_temp_dir(
            "basic-template.yaml", "basic-template.yaml"
        )
        second_test_template_path = self.copy_fixture_to_temp_dir(
            "basic-template.yaml", "basic-template-second.yaml"
        )

        main(["cfn-doc", test_template_path, second_test_template_path])

        self.assertPathExists(self.applyTempPath("basic-template-doc.md"))
        self.assertPathExists(self.applyTempPath("basic-template-second-doc.md"))

    def test_it_outputs_template_title(self):
        test_template_path = self.copy_fixture_to_temp_dir(
            "basic-template.yaml", "basic-template.yaml"
        )

        main(["cfn-doc", test_template_path])

        expected_doc_path = (
            Path(self.temp_dir.name) / "basic-template-doc.md"
        ).resolve()
        with (open(expected_doc_path, "r+")) as f:
            actual_doc = f.read()

        self.assertRegex(actual_doc, "# A sample template")

    def copy_fixture_to_temp_dir(self, fixture_path, dest_name=None):
        if dest_name is None:
            dest_name = fixture_path

        test_dir = Path(__file__).parent
        prime_test_template_path = str((test_dir / fixture_path).resolve())
        clone_test_template_path = str((Path(self.temp_dir.name) / dest_name).resolve())
        shutil.copyfile(prime_test_template_path, clone_test_template_path)
        return clone_test_template_path

    def assertPathExists(self, path):
        self.assertTrue(
            os.path.exists(path),
            f"File not found at {str(path)}",
        )

    def applyTempPath(self, file_name):
        return (Path(self.temp_dir.name) / file_name).resolve()

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()
        del self.temp_dir

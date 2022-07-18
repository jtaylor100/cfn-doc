import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from cfn_doc.cfn_doc import main


class MainTest(unittest.TestCase):
    def test_it_outputs_template_title(self):
        test_dir = Path(__file__).parent
        prime_test_template_path = str((test_dir / "basic-template.yaml").resolve())

        f = io.StringIO()
        with redirect_stdout(f):
            main([prime_test_template_path])
        stdout = f.getvalue()

        self.assertRegex(stdout, "# A sample template")

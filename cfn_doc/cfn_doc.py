import argparse
from pathlib import Path

import yaml


def main(argv):
    tool_description = "Generate markdown documentation for CloudFormation templates"
    parser = argparse.ArgumentParser(prog="cfn-doc", description=tool_description)
    parser.add_argument("template_files", nargs="+", metavar="template-file")
    args = parser.parse_args(argv[1:])

    for template_file_path_str in args.template_files:
        template_file_path = Path(template_file_path_str)
        with open(template_file_path, "r") as f:
            template_yaml = yaml.load(f, Loader=yaml.SafeLoader)

        template_file_name = template_file_path.name
        template_doc_file_name = template_file_name.replace(".yaml", "-doc.md")
        template_doc_file_path = template_file_path.parent / template_doc_file_name
        with open(template_doc_file_path, "w+") as f:
            f.write("# " + template_yaml["Description"])

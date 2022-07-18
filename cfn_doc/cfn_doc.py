import argparse

import yaml


def get_output():
    return "Hello world"


def main(argv):
    tool_description = "Generate markdown documentation for CloudFormation templates"
    parser = argparse.ArgumentParser(description=tool_description)
    parser.add_argument("template_files", nargs="+", metavar="file")
    args = parser.parse_args(argv)

    template_file_path = args.template_files[0]
    with open(template_file_path, "r") as f:
        template_yaml = yaml.load(f, Loader=yaml.SafeLoader)
        print("# " + template_yaml["Description"])

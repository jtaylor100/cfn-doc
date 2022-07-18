# AWS CloudFormation Documenter (cfn-doc)

Generate markdown documentation for CloudFormation templates

## Usage

```shell
python -m cfn_doc /path/to/template.yaml
```

A `template-doc.md` file is generated at `/path/to/template-doc.md`.

## Run tests

In the repository directory, create and use a virtual environment:

```shell
python -m venv env
source env/bin/activate
```

Install dependencies:

```shell
pip install -r requirements.txt
```

Execute the test runner:

```shell
python -m unittest
```

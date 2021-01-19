---
description: bcregistries-schemas readme
ignore: true
---

## About

This has the common JSONSchema for BCRegistry transactions, as well as sample test data.

This also includes an installable python package for flask apps for working with the schemas and making validations easier within python code.

### This is part of the BCRegistry services.

## Usage
To use with a flask app, add the following to the app requirements.txt file:
   git+https://github.com/bcgov/bcregistries-schemas.git@1.0.0#egg=registry_schemas
Where "1.0.0" is the version of the schemas to use. 

### Local development
Use the dependencies in requirements/dev.txt (temporarily copy them to requirements.txt in this directory).
Run the following commands from this directory to create, verify a virtual environment and install the packages.
python3 -m venv env
source env/bin/activate
which python
make setup
pip install -e .
pip freeze

Test all schemas from the root directory:
pytest

Test an individual schema from the root directory:
pytest -v -s ./tests/unit/ppr/test_amendment_statement.py

## Getting Help or Reporting an Issue

To report bugs/issues/feature requests, please file an [issue](https://github.com/bcgov/business-schemas/issues/).

## How to Contribute

If you would like to contribute, please see our [CONTRIBUTING](CONTRIBUTING.md) guidelines.

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). 
By participating in this project you agree to abide by its terms.

## Issues/Suggestions
Make Suggestions/Issues [here!](https://github.com/bcgov/business-schemas/issues/new)
Issues are [markdown supported](https://guides.github.com/features/mastering-markdown/).

## License

    Copyright 2021 Province of British Columbia

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

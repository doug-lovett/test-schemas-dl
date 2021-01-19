# Copyright © 2020 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test Suite to ensure the PPR court order information schema is valid.

"""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import COURT_ORDER


def test_valid_court_order():
    """Assert that the schema is performing as expected."""
    is_valid, errors = validate(COURT_ORDER, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_court_order_missing_courtname():
    """Assert that an invalid court order fails - court name is missing."""
    coInfo = copy.deepcopy(COURT_ORDER)
    del coInfo['courtName']

    is_valid, errors = validate(coInfo, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_court_order_missing_courtregistry():
    """Assert that an invalid court order fails - court registry is missing."""
    coInfo = copy.deepcopy(COURT_ORDER)
    del coInfo['courtRegistry']

    is_valid, errors = validate(coInfo, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_court_order_missing_filenumber():
    """Assert that an invalid court order fails - file number is missing."""
    coInfo = copy.deepcopy(COURT_ORDER)
    del coInfo['fileNumber']

    is_valid, errors = validate(coInfo, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_court_order_missing_orderdate():
    """Assert that an invalid court order fails - order date is missing."""
    coInfo = copy.deepcopy(COURT_ORDER)
    del coInfo['orderDate']

    is_valid, errors = validate(coInfo, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_court_order_courtname():
    """Assert that an invalid court order fails - court name is too short."""
    coInfo = copy.deepcopy(COURT_ORDER)
    coInfo['courtName'] = 'xx'

    is_valid, errors = validate(coInfo, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_court_order_courtregistry():
    """Assert that an invalid court order fails - court registry is too short."""
    coInfo = copy.deepcopy(COURT_ORDER)
    coInfo['courtRegistry'] = 'XX'

    is_valid, errors = validate(coInfo, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_court_order_filenumber():
    """Assert that an invalid court order fails - file number is too long."""
    coInfo = copy.deepcopy(COURT_ORDER)
    coInfo['fileNumber'] = 'FILE NUMBER TOO LONGXXXX'

    is_valid, errors = validate(coInfo, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_court_order_date():
    """Assert that an invalid court order fails - order date format is invalid."""
    coInfo = copy.deepcopy(COURT_ORDER)
    coInfo['orderDate'] = 'XXXXXXXX'

    is_valid, errors = validate(coInfo, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

def test_invalid_court_order_effect():
    """Assert that an invalid court order fails - effect of order is too short."""
    coInfo = copy.deepcopy(COURT_ORDER)
    coInfo['effectOfOrder'] = 'XX'

    is_valid, errors = validate(coInfo, 'courtOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid



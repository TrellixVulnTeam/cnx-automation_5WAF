# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

import os

# Load environment variables from .env file
from dotenv import load_dotenv

DOTENV_PATH = os.path.join(
  os.path.realpath(os.path.dirname(__file__)), '../.env')
load_dotenv(dotenv_path=DOTENV_PATH)

# Import fixtures from our package so pytest can detect them
from fixtures.base import chrome_options, selenium # flake8: noqa
from fixtures.snapshot import snapshot
from fixtures.archive import archive_base_url
from fixtures.webview import american_gov_url, content_url
from fixtures.legacy import (legacy_base_url, legacy_username, legacy_password,
                             m46922_1_13_cnxml_filepath)


def pytest_addoption(parser):
    group = parser.getgroup('selenium', 'selenium')
    group.addoption('--headless',
                    action='store_true',
                    default=os.getenv('HEADLESS', False),
                    help='enable headless mode for chrome.')
    parser.addoption('--runslow',
                     action='store_true',
                     default=os.getenv('RUNSLOW', False),
                     help='run slow tests')
    # Adapted from:
    # https://github.com/pytest-dev/pytest-base-url/blob/master/pytest_base_url/plugin.py#L51
    parser.addini('archive_base_url', help='base url for CNX archive.')
    parser.addoption(
        '--archive_base_url',
        metavar='url',
        default=os.getenv('ARCHIVE_BASE_URL', None),
        help='base url for CNX archive.')
    parser.addini('legacy_base_url', help='base url for CNX legacy.')
    parser.addoption(
        '--legacy_base_url',
        metavar='url',
        default=os.getenv('LEGACY_BASE_URL', None),
        help='base url for CNX legacy.')
    parser.addoption(
        '--legacy_username',
        default=os.getenv('LEGACY_USERNAME'),
        help='username for CNX legacy.')
    parser.addoption(
        '--legacy_password',
        default=os.getenv('LEGACY_PASSWORD'),
        help='password for CNX legacy.')

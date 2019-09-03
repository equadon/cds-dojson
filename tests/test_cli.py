# -*- coding: utf-8 -*-
#
# This file is part of CERN Document Server.
# Copyright (C) 2016 CERN.
#
# CERN Document Server is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Document Server is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Document Server; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.
"""Test cds-dojson CLI and jsonschema compiler."""

from __future__ import absolute_import

import json
import os
import shutil

import pkg_resources
import pytest
from click.testing import CliRunner

from cds_dojson.cli import compile_schema, convert_yaml2json


@pytest.mark.parametrize('source, destination', [
    ('./tests/fixtures/books/ymls/', './tests/fixtures/books/results/')
])
def test_cli_convert_yaml2json(source, destination):
    """Test cds-dojson CLI 'convert_yaml2json' command"""
    runner = CliRunner()

    result = runner.invoke(convert_yaml2json, [source, destination])

    assert 0 == result.exit_code

    with open('./tests/fixtures/books/books_title_mock.json') as s:
        # read the mock JSON file
        json_mock = json.load(s)

    with open(os.path.join(destination, 'books_title.json')) as s:
        # read the newly created JSON file
        json_converted = json.load(s)

    assert json_mock == json_converted

#!/bin/bash

set -euxo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TOP="$(dirname "${BASEDIR}")"

cd "${TOP}"
git checkout -- \
 NEWS.rst \
 app/resplendent/__init__.py \
 app/resplendent/filters/__init__.py \
 app/resplendent/filters/filterdump.py \
 app/resplendent/filters/restructuredtext.py \
 app/resplendent/version.py

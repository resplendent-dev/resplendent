#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

cp "${BASEDIR}/README.rst" "${BASEDIR}/app/README.rst"
cp "${BASEDIR}/LICENSE" "${BASEDIR}/app/LICENSE"

MAIN_MODULE="resplendent"
MODULES=( "${MAIN_MODULE}" "tests" )
export MODULES
export MAIN_MODULE

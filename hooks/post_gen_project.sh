#!/bin/bash

set -euxo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TOP="$(dirname "${BASEDIR}")"

cd "${TOP}"
git checkout -- \
 NEWS.rst \
 app/pip/3.4/app/requirements.txt \
 app/resplendent \
 app/tests \
 docs/index.rst docs/modules.rst docs/resplendent.rst

#!/bin/sh

set -e

./bin/coverage run \
    --source src/yafowil/widget/multiselect \
    --omit src/yafowil/widget/multiselect/example.py \
    -m yafowil.widget.multiselect.tests
./bin/coverage report
./bin/coverage html

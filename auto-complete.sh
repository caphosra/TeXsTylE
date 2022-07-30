#!/bin/bash

mkdir -p ./dist
pushd workshop/dev/ > /dev/null
python3 pkgcommand.py -i ../../texstyle.cwl -o ../../dist
popd  > /dev/null

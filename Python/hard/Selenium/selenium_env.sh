#!/bin/bash
set -e

virtualenv -p python3 venv3

. venv3/bin/activate

pip install selenium

wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz

tar vfxz geckodriver-v0.23.0-linux64.tar.gz

mv geckodriver venv3/bin

rm geckodriver-v0.23.0-linux64.tar.gz

deactivate

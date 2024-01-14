#!/bin/bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

. $SCRIPTPATH/venv/bin/activate
python3 "$SCRIPTPATH/main.py"
deactivate

#!/bin/bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

$SCRIPTPATH/.venv/bin/python3 "$SCRIPTPATH/main.py"

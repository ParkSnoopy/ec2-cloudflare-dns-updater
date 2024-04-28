#!/bin/bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ $(dpkg-query -W -f='${Status}' python3-venv 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo "python3-venv not installed"
  apt-get install python3-venv;
else
  echo "python3-venv already installed"
fi

if [ $(dpkg-query -W -f='${Status}' python3-venv 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo "python3-venv still not installed"
  echo "try run with sudo"
  exit 1
fi

python3 -m venv .venv

$SCRIPTPATH/.venv/bin/pip install -r requirements.txt

#!/bin/bash
if [ -f .venv ]; then
    echo "virtual environment directory is already created"
    exit 0
fi

echo "create new virtual environment directory"
python3 -m venv .venv

source .venv/bin/activate

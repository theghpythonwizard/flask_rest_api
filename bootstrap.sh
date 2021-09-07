#!/bin/sh

export FLASK_APP=./src/app.py
source ./maccloudapi-venv/bin/activate

flask run --host 0.0.0.0

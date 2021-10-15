#!/bin/bash

# run our server locally:
PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=endpoints flask run --host=$hostAddress --port=8000

#!/bin/sh

pipenv install --dev

pipenv run python -m playwright install

#!/bin/sh

pipenv install --dev

pipenv run playwright install

pipenv run pytest

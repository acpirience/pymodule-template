@echo off

flake8 .\PROJECT\ .\test  --exclude=__init__.py --max-line-length=100
pylint PROJECT
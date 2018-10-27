@echo off
cd docs
rmdir /S /Q _build
sphinx-apidoc -f -e -M -o . ../PROJECT
make html
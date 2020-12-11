PUSHD %~dp0
set HOME=%~dp0
python setup.py sdist --formats=gztar,zip upload -r local
POPD

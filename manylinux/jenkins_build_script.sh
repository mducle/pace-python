#!/bin/bash
cd /mnt
/opt/python/cp37-cp37m/bin/pip wheel . --no-deps
/opt/python/cp36-cp36m/bin/pip wheel . --no-deps
find . -type f -iname "*-linux*.whl" -exec auditwheel repair '{}' \;

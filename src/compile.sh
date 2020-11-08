#!/bin/sh

#TODO: convert ducky scripts to c code
python3 ducky_convert.py --scripts /app/scripts/
# qmk compile --keyboard disobey2018 --keymap default
# mv /app/qmk_firmware/*.bin /build/

#!/bin/sh

#TODO: convert ducky scripts to c code
TARGET_FILE=/app/qmk_firmware/keyboards/disobey2018/shared_keyboard_utils.c
python3 ducky_convert.py --scripts /app/scripts/ --target $TARGET_FILE
cat $TARGET_FILE
qmk compile --keyboard disobey2018 --keymap default
mv /app/qmk_firmware/*.bin /build/

#!/bin/sh

TARGET_FILE=/app/qmk_firmware/keyboards/disobey2018/shared_keyboard_utils.c
python3 ducky_convert.py --scripts /app/scripts/ --target $TARGET_FILE --lang fi
qmk compile --keyboard disobey2018 --keymap default
mv /app/qmk_firmware/*.bin /build/

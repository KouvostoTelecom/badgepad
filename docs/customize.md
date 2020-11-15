# Customizing keymap

This document describes how you can add your own scripts to the Disobey badge 2018. This makes all kinds of bad USB attacks possible on the badge, but also makes it possible to use the Disobey badge as a macropad for all your needs. For example, you can customize the keymap so that it holds `F13`-`F24` keys, which are supported in Windows, Linux and MacOS, but are rarely used by any of the programs.

## How keymaps are compiled?
The firmware and everything is compiled by [QMK firmware](https://github.com/qmk/qmk_firmware). KouvostoTelecom gracefully forked and added support for [Disobey badge 2018](https://github.com/KouvostoTelecom/qmk_firmware/tree/keyboard/rubberheikki/keyboards/disobey2018).

The keymaps are stored within `qmk_firmware/keyboards/disobey2018/keymaps/` folder. To add your own keymap, copy the default folder and rename it as you'd like. The keymaps and everything are customized by customizing the `keymap.c` file. The list of all supported keycodes can be found from [QMK docs](https://docs.qmk.fm/#/keycodes). 

## Layers?
Yes.


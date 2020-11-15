# Customizing keymap

This document describes how you can add your own scripts to the Disobey badge 2018. This makes all kinds of bad USB attacks possible on the badge, but also makes it possible to use the Disobey badge as a macropad for all your needs. For example, you can customize the keymap so that it holds `F13`-`F24` keys, which are supported in Windows, Linux and MacOS, but are rarely used by any of the programs.

If you decide to not modify badge hardware to include a rotary encoder and a screen; use 

## How keymaps are compiled?
The firmware and everything is compiled by [QMK firmware](https://github.com/qmk/qmk_firmware). KouvostoTelecom gracefully forked and added support for [Disobey badge 2018](https://github.com/KouvostoTelecom/qmk_firmware/tree/keyboard/rubberheikki/keyboards/disobey2018).

The keymaps are stored within `qmk_firmware/keyboards/disobey2018/keymaps/` folder. To add your own keymap, copy the default folder and rename it as you'd like. The keymaps and everything are customized by customizing the `keymap.c` file. The list of all supported keycodes can be found from [QMK docs](https://docs.qmk.fm/#/keycodes). 

**If you did not add OLED screen and a rotary encoder**, use `default-lite` folder instead of the `default` folder! Otherwise you might have latency problems.

## Layers?
One button can hold multiple different functions, if you use layers. Layers are similar to how laptops, with limited keyboards, use `FN`-button. This is refered to layers. You can switch layers by multiple different ways. The full list of how you can change the layer is documented in [QMK docs](https://docs.qmk.fm/#/feature_layers). 

You can also modify your badge to have a rotary encoder to swap layers. Very convenient!
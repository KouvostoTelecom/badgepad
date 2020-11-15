# Customizing keymap

This document describes how you can add your own scripts to the Disobey badge 2018. This makes all kinds of bad USB attacks possible on the badge, but also makes it possible to use the Disobey badge as a macropad for all your needs. For example, you can customize the keymap so that it holds `F13`-`F24` keys, which are supported in Windows, Linux and MacOS, but are rarely used by any of the programs.

If you decide to not modify badge hardware to include a rotary encoder and a screen; use 

## How keymaps are compiled?
The firmware and everything is compiled by [QMK firmware](https://github.com/qmk/qmk_firmware). KouvostoTelecom gracefully forked and added support for [Disobey badge 2018](https://github.com/KouvostoTelecom/qmk_firmware/tree/keyboard/rubberheikki/keyboards/disobey2018).

The keymaps are stored within `qmk_firmware/keyboards/disobey2018/keymaps/` folder. To add your own keymap, copy the default folder and rename it as you'd like. The keymaps and everything are customized by customizing the `keymap.c` file. The list of all supported keycodes can be found from [QMK docs](https://docs.qmk.fm/#/keycodes). Due to our script and compile way, we have moved the customizing part to `shared_keymap.c` file in `qmk_firmware/keyboards/disobey2018/` folder root.

**If you did not add OLED screen and a rotary encoder**, use `lite` folder instead of the `default` folder! Otherwise you might have latency problems.

## Layers?
One button can hold multiple different functions, if you use layers. Layers are similar to how laptops, with limited keyboards, use `FN`-button. This is refered to layers. You can switch layers by multiple different ways. The full list of how you can change the layer is documented in [QMK docs](https://docs.qmk.fm/#/feature_layers). 

You can also modify your badge to have a rotary encoder to swap layers. Very convenient!

# `Keymap.c` file
`keymap.c` holds all the keycodes that you use. 

```c
    [0] = LAYOUT(
/*	----  ----  ----  ----  ----  ----*/
	      KC_0,             KC_1, 
	KC_2,       KC_3, KC_4,       KC_5,
	      KC_6,             KC_7
   ),
};
```
This is the default layer, layer 0, according to `shared_keymap.c` file. When not pressing any buttons, the buttons output numbers from `0` to `7`. To change these keycodes to anything you'd like, you can check the [QMK documentation](https://docs.qmk.fm/#/keycodes) and customize these.

To add another layer, you can copy & paste the first layer and make some changes;
```c
    [0] = LAYOUT(
/*	----  ----  ----  ----  ----  ----*/
	      KC_0,             KC_1, 
	KC_2,       KC_3, KC_4,       KC_5,
	      KC_6,             KC_7
   ),
   [1] = LAYOUT(
	      KC_A,             KC_B, 
	KC_C,       KC_D, KC_E,       KC_F,
	      KC_G,             KC_H
   ),
};
```
Remember to change the number of the other layer! By default, we added it so that the rotary encoder cycles layers. If you did not add a rotary encoder, and want more layers, you need to implement a way to change the layer (refer to [QMK documentation about layers](https://docs.qmk.fm/#/feature_layers)).

_The ASCII doesn't have to match the grid in the keymap-file_.


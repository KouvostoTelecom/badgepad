# BadgePAD

* Output - firmware will appear here
* Scripts - put your duckscripts here

The BadgePAD project uses a forked [QMK firmware](https://github.com/KouvostoTelecom/qmk_firmware) when used as a macropad. You are free to check out [QMK's documentation](https://docs.qmk.fm) and unlock the full potential of the firmware!

You don't have to use the KouvostoTelecom provided Docker to achieve greatness. This just tries to streamline stuff for you and your use.

# Setup & compile

## QMK Toolbox (win & mac)
1. Build and compile firmware
```
make compile
```
2. Boot badge to flash mode according to the guide at [docs/firmware.md](docs/firmware.md)
3. Open QMK Toolbox and select .bin file from `output`-folder
4. Press `Flash` from QMK Toolbox
5. Profit

## dfu-util (linux & mac)
1. Build and compile firmware

```
make compile
```
2. Boot badge to flash mode according to the guide at [docs/firmware.md](docs/firmware.md)
3. Run the following dfu-util command
```
dfu-util -a 0 -s 0x08000000:leave -D output/disobey2018_default.bin
```
4. Profit

## Scripts
Add your DuckyScripts as txt-files to `scripts` folder according to the layers.
- Maximum of 8 txt-files per layer
- The keybindings will be in alphabetical order
- Keys are mapped like this:
```
    1           2
3       4   5       6
    7           8
```
- `a.txt` would be binded to key #1

## Parts

### OLED display
https://a.aliexpress.com/_mLHUDWN

### Rotary Encoder
https://a.aliexpress.com/_mM4yNON

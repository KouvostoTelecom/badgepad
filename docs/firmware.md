# Firmware

The badge supports [QMK firmware](https://github.com/qmk/qmk_firmware/), which makes the badge to act like a keyboard, instead of a gamepad. You can use `dfu-util`or [QMK Toolbox](https://github.com/qmk/qmk_toolbox) to flash the firmware. QMK Toolbox supports only Windows and MacOS (boooo). Remember that the original firmware for the badge is available at Disobey repositories.

## How to flash QMK to Disobey 2018 badge

You need to install Docker! Get Docker from [here](https://docs.docker.com/get-docker/)! If you do not, you need to follow QMK's documentation.

### BadgePad way
1. `git clone https://github.com/KouvostoTelecom/badgepad`
2. Run the Docker setup with `make compile` command as mentioned in the [README.md](../README.md). This generates the binary file, which contains the firmware. The firmware .bin-file can be found from `badgepad/output` folder. The filename is `disobey2018_<keymap>.bin` where keymap can be almost anything.
3. Short the badge
   1. Make a jumper wire (you can use a small AWG wire or, for example, ESD tweezers)
   2. Connect the middle (5th from left) resistor to get to the bootloader mode to the right side component (3,3V linear voltage regulator). The jump wire should be connected **when powering on the device** (either pressing the `RESET` button, or reconnecting USB-cable while shorting). Otherwise it won't work.
   3.  The three LEDs should be on (see picture below) as a sign that the badge is in bootloader mode and it should show up in the QMK toolbox. 
   4.  You can now remove the jumper wire. The badge remains in bootloader mode until flash or badge reboot.

![Short the badge](img/badge_flash.png)

![STM32 DFU refers to the badge in bootloader mode](img/toolbox1.png)
`STM32 DFU device connected` message refers to the badge being in the bootloader mode.

4. Choose the generated `.bin` file and press `Flash`-button. After this, the device disconnects and reconnects as a keyboard.

![Firmware uploading](img/toolbox2.png)

5. Reconnect the USB device.
6. ???
7. Profit!

**NOTE:** You only need to do this once! For future flashing, you can achieve the same results by pressing `UP` on badge while connecting the badge to get to bootloader mode

### dfu-util way
1. Follow BadgePad way to part 3.4. and then continue from here:
2. `dfu-util -a 0 -s 0x08000000:leave -D output/disobey2018_default.bin`
3. The badge should leave the DFU mode automatically (hence the `:leave` option) and you should be able to start using your badge.

## Restoring the original firmware
If for any reason you want to go back to original Disobey 2018 firmware, you can get the original firmware from [Disobey 2018 repository](https://github.com/disobeyfi/badge-2018/tree/master/badgefw-final). To flash the OG firmware, you can use the QMK toolbox or `dfu-util` to reflash it.
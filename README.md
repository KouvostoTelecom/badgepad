# BadgePAD

* Output - firmware will appear here
* Scripts - put your duckscripts here

The BadgePAD project uses a forked [QMK firmware](https://github.com/KouvostoTelecom/qmk_firmware) when used as a macropad. You are free to check out [QMK's documentation](https://docs.qmk.fm) and unlock the full potential of the firmware!

You don't have to use the KouvostoTelecom provided Docker to achieve greatness. This just tries to streamline stuff for you and your use.

# Setup & compile

1. Build image

```
docker build . -t badgepad-latest 
```

2. Compile firmware

```
docker run -it --rm -v $(pwd)/output:/build badgepad-latest
```

3. Boot badge to flash mode (TBD)
4. Open QMK Toolbox and select .bin file from `output`. Press Flash.
5. Profit

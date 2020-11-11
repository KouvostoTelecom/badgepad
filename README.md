# BadgePAD

* Output - firmware will appear here
* Scripts - put your duckscripts here

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

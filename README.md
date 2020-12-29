# Micro:bit Workspace
Create a workspace folder with micro:bit's stubs functions for IDE and script to upload multiple scripts to micro:bit

## Requirements
- Python 3.6+
- Virtual enviroment with:
   - pylint
   - microfs

## Micro:bit stubs
The function stubs were created based on the [micro:bit MicroPython Documentation](https://microbit-micropython.readthedocs.io/en/latest/index.html) and work with vscode Intellisense/pylint

### Created stubs:
- Core Functions
- Accelerometer
- Buttons
- Compass
- Display
- Input/Output Pins
- I²C
- Image
- SPI
- UART
- Audio (separated folder)
- Music (separated)
- NeoPixel

### Todo
- Bluetooth (discover how)
- Radio

## Folder Creation
By using create_workspace script a folder with the desired name is created containing a upload script and the stubs functions inside folder with the same name as the modules.
The upload script use the internal configurations to upload the main script and any additional scripts to the micro:bit

Usage:
```
$ create_workspace.ps1 foldername

-- or --

$ create_workspace.sh foldername
```

## Upload Script Configurations
| Name | Type | Values
| --- | --- | ---|
| MAIN | `string` | Name of the main script
| ADDONS | `list of srings` | List with the names of additionals scripts

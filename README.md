# Sensorama Datapath - data stuff for sensorama.org

[![Build Status](https://travis-ci.org/wkoszek/sensorama-datapath.svg?branch=master)](https://travis-ci.org/wkoszek/sensorama-datapath)

This repository holds datafiles obtained from sensorama.org mobile apps.
Within `files/` folder you have compressed `bzip2` files. They contain the
actual sensor data.

The `tools` directory has scripts including its main `sensorama.py` used for
validating JSON files from `files/`

`schema` has the schema (skeleton file) which describes the layout of the
sample JSON files.

# Data format

Data is stored in a JSON format. The 1st hierarchy holds `date`, `device`
and `desc`, which are self-explanatory. The `interval` specifies number of
milliseconds between asking the sensor to give you data. The `sensors` will
dump out all sensors known to the device. Then it comes to actual data, the
fields areas folows:

- `acc` - accelerator coordinates
- `gyro` - gyroscompe values
- `steps` - step counter
- `grav` - gravity counter
- `env` - contains 4 variables:
   - ambient light 
   - light sensor
   - pressure sensor
   - humidity sensor
- `batt` - monitor the state usage


# Author

- Wojciech Adam Koszek, [wojciech@koszek.com](mailto:wojciech@koszek.com)
- [http://www.koszek.com](http://www.koszek.com)

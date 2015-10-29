# Sensorama Datapath - data stuff for sensorama.org

[![Build Status](https://travis-ci.org/wkoszek/sensorama-datapath.svg?branch=master)](https://travis-ci.org/wkoszek/sensorama-datapath)

This repository holds datafiles obtained from sensorama.org mobile apps.
Within `files/` folder you have compressed `bzip2` files. They contain the
actual sensor data.

The `tools` directory has scripts including its main `sensorama.py` used for
validating JSON files from `files/`

`schema` has the schema (skeleton file) which describes the layout of the
sample JSON files.

# Author

- Wojciech Adam Koszek, [wojciech@koszek.com](mailto:wojciech@koszek.com)
- [http://www.koszek.com](http://www.koszek.com)

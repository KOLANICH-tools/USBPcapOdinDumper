USBPcapOdinDumper [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
[![PyPi Status](https://img.shields.io/pypi/v/USBPcapOdinDumper.svg)](https://pypi.python.org/pypi/USBPcapOdinDumper)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/USBPcapOdinDumper.svg)](https://libraries.io/github/KOLANICH/USBPcapOdinDumper)

It's a tool to dump ODIN3 messages into files with human-readable names for further reverse-engineering. Both ```usbmon``` (the subsystem in Linux kernel) and ```usbpcap``` (the app for Windows) captures are supported.

Requirements
------------
* [`plumbum`](https://github.com/tomerfiliba/plumbum) ![](https://img.shields.io/github/license/tomerfiliba/plumbum.svg) [![TravisCI Build Status](https://travis-ci.org/tomerfiliba/plumbum.svg?branch=master)](https://travis-ci.org/tomerfiliba/plumbum) - for the fancy CLI.
* [`RichConsole`](https://github.com/KOLANICH/RichConsole) ![](https://img.shields.io/github/license/KOLANICH/RichConsole.svg) [![TravisCI Build Status](https://travis-ci.org/KOLANICH/RichConsole?branch=master)](https://travis-ci.org/KOLANICH/RichConsole) - for colors in console. It's mandatory because this shit is used internally to generate file names, so in console the names are colorful.
* [`Pipeline`](https://github.com/KOLANICH/Pipeline.py) ![](https://img.shields.io/github/license/KOLANICH/Pipeline.py.svg) [![TravisCI Build Status](https://travis-ci.org/KOLANICH/Pipeline.py?branch=master)](https://travis-ci.org/KOLANICH/Pipeline.py) - The main app's pipeline.
* [`kaitaistruct`](https://github.com/kaitai-io/kaitai_struct_python_runtime) ![](https://img.shields.io/github/license/kaitai-io/kaitai_struct_python_runtime.svg)  [![TravisCI Build Status](https://travis-ci.org/kaitai-io/kaitai_struct_python_runtime?branch=master)](https://travis-ci.org/kaitai-io/kaitai_struct_python_runtime) - runtime for Kaitai Striuct-generated parsers.

How to use
----------
```
python3 -m USBPcapOdinDumper pcap_file_1.pcap
```

or

```
python3 -m USBPcapOdinDumper
```

to process all the files in the current folder.

It will generate the folders in the current folder for each pcap file.

For each ```isUseful``` (see ```isUseful``` methods) packet it will generate the file, which name usually have encoded:
 * the packet number in pcap
 * the type of USB transaction (only ```bulk``` are useful for us)
 * the direction showed with an arrow
 * some info from enums of odin messages. If enum values are incorrect, an error occurs, info about which enum and which value is incorrect will be added into a file name.

The parser of ODIN3 messages is based on Benjamin Dobell's [Heimdall](https://github.com/Benjamin-Dobell/Heimdall) ![](https://img.shields.io/github/license/Benjamin-Dobell/Heimdall.svg)  [![TravisCI Build Status](https://travis-ci.org/Benjamin-Dobell/Heimdall?branch=master)](https://travis-ci.org/Benjamin-Dobell/Heimdall) flasher.

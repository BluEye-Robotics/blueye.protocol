# blueye.protocol
[![Test status](https://github.com/BluEye-Robotics/p2_app_protocol/workflows/PythonTests/badge.svg)](https://github.com/BluEye-Robotics/p2_app_protocol/actions)

This repository provides the definition of the app protocol in form of a json file (protocol.json).

An html version of the protocol is found in the html folder.

Important: This repository includes generated code. If protocol.json is changed, the compiled files need to be updated and later committed:
```
./generate_all.sh
```

All changes need to be backwards-compatible.

**Important:
Make sure to update meta-blueye but also the the Yocto SDK after protocol changes, otherwise cross compilation might fail and will not be compatible.**

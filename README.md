# firmwaretools
a set of scripts and tools for various firmware analysis tasks

########################

Updated file: parse-uboot-dump.py
Display errors if transfer data via UART are broken. Like missing lines or data is too short or too long.

E.g. log if dump file is broken:
```
Error! Wrong line legth:  119
813b20b0: ffffffff ffffffff ffffffff ffffffff    .............. ffffffff ffffffff ffffffff ffffffff    ................
-----------------------------------------------------
Error! Missing data line
Before line:  813bb120
-----------------------------------------------------
Error! Wrong line legth:  12
8152cb......
-----------------------------------------------------
Error! Missing data line
Before line:  8159eb90
-----------------------------------------------------
```

#!/usr/bin/env python3
import re
import sys

infile = sys.argv[1]
outfile = sys.argv[2]

i = open(infile,"r")
o = open(outfile,"wb")

line_address_prev = 0

for count, line in enumerate(i.readlines()):
    line = line.strip("\n\t\r")
    if len(line) != 65:
    	print("Error! Wrong line length: ", len(line))
    	print(line)
    	print("-----------------------------------------------------")
#    	break
    if re.match(r'^[0-9a-f]{8}:',line):
        line = line.split(":")
        if len(line) > 1:
            line_address = int(line[0], base=16)
            if count > 0:
            	if (line_address - line_address_prev) != 16:
            		print("Error! Missing data line")
            		print("Before line: ", line[0])
            		print("-----------------------------------------------------")
#            		break
            line_address_prev = line_address	
            line = line[1]
            line = line.replace(" ","")[:32]
            data = bytes.fromhex(line)
            o.write(data)

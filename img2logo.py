#!/usr/bin/env python

import sys
from PIL import Image
import struct

idnum=-1


if sys.argv != 4:
   print "Usage: img2logo.py id infile outfile"   
   raise SystemExit

outname = sys.argv[3]
inname = sys.argv[2]
idnum = int(sys.argv[1])




f = open(outname,"w")



f.write(struct.pack("!BBBBiBBB",0x10,0x60,0x64,0x15,idnum,0x1b,0x58,0xb))



img = Image.open(inname)

for y in range(27):
  for x in range(11):
      xprim = x*8

      i = 0
      l = range(xprim,xprim+8)

      for p in l:
      	  i = i*2

          if img.getpixel((p,y)) != 255:
	    i= i+1	  

      f.write(chr(i))

f.close()

#!/usr/bin/python
import os

source_dir = "source"
target_dir = "target"

target_encoding = "utf16"

if not os.path.exists( source_dir):
    raise IOError( "Source Directory \"%s\" doesn't exist!" % source_dir)

if not os.path.exists( target_dir):
    os.mkdir( target_dir)

for root, dirs, files in os.walk( source_dir):
    for file in files:
        full = os.path.join( source_dir, file)
        full_to = os.path.join( target_dir, file)
        
        fs = open( full, "rb")
        content = fs.read()
        fs.close()
        
        fo = open( full_to, "wb")
        fo.write( (content.decode()).encode( target_encoding))
        fo.close()

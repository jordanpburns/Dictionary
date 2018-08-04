from struct import unpack
from zlib import decompress
import os
import re

# this is some gnarly stuff I found on the internet to unpack/decompress the dictionary.
# should work for any downloaded mac dicitonary, just enter the desired filename

filename = "/System/Library/Assets/com_apple_MobileAsset_DictionaryServices_dictionaryOSX/2a679af89e5bb8b417ff02b0fef81ca39ffad9a5.asset/AssetData/German - English.dictionary/Contents/Resources/Body.data"
f = open(filename, 'rb')

def gen_chunk():
    f.seek(0x40)
    limit = 0x40 + unpack('i', f.read(4))[0]
    f.seek(0x60)
    while f.tell()<limit:
        sz, = unpack('i', f.read(4))
        buf = decompress(f.read(sz)[8:])
        yield re.sub(b'(?m)^....<', b'<', buf)

with open('dict.xml', 'wb') as fo:
  for s in gen_chunk():
    fo.write(s)

os.system('bash getWords.bash')

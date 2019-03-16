# convert string to hex value
def str2hex(string, encoding='ascii'):
  return hex(int(byte2hex(bytearray(string.encode(encoding))), 16))

# convert hex value to string
def hex2str(hexVal):
  return ''.join(map(chr, hex2byte(hexVal)))

# convert hex to binary data
def hex2byte(hexVal):
  import codecs
  return codecs.getdecoder('hex')(hexVal.lstrip('0x'))[0]

# convert binary data to hex
def byte2hex(byteArray):
  return hex(int(b2hbyte(byteArray), 16))

# convert string to hexadecimal integer
def str2int(string, encoding='ascii'):
  return int(byte2hbyte(bytearray(string.encode(encoding))), 16)

# helper function for converting bytearray to hex bytearray
def byte2hbyte(byteArray):
  import codecs
  return codecs.getencoder('hex')(byteArray)[0]

# convert hexadecimal integer to byte array
def int2byte(val):
  return hex2byte(hex(val))

# convert hexadecimal integer to string
def int2str(val):
  return hex2str(hex(val))

# TODO: replace this (not compatible with python2)
# bytearray to binary string
def byte2bit(byteArray):
  return bin(int.from_bytes(byteArray, byteorder='big')).strip('0b')

# TODO: replace this (not compatible with python2)
# Convert base-2 (01) string to bytearray
def base22byte(base2string):
  return bytearray(int(base2string, 2).to_bytes((len(base2string) + 7) // 8, 'big'))

# Printing formatted data as string
# hex
# print "\x12\x02\x00"
# octal
# print "\112\102\x100"

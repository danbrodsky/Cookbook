''' Python2/3 module for converting between common data representations '''

def str_to_hex(string, encoding='ascii'):
    ''' Convert string value to hexdecimal type '''
    return hex(int(byte_to_hex(bytearray(string.encode(encoding))), 16))

def hex_to_str(hex_val):
    ''' Convert hexdecimal type object to string '''
    return ''.join(map(chr, hex_to_byte(hex_val)))

def hex_to_byte(hex_val):
    ''' Convert hexdecimal type object to bytearray object '''
    import codecs
    return codecs.getdecoder('hex')(hex_val.lstrip('0x'))[0]

def byte_to_hex(byte_array):
    ''' Convert bytearray object to hexdecimal object '''
    return hex(int(byte_to_hbyte(byte_array), 16))

def str_to_int(string, encoding='ascii'):
    ''' Convert string object to Int object '''
    return int(byte_to_hbyte(bytearray(string.encode(encoding))), 16)

def byte_to_hbyte(byte_array):
    ''' Convert data in bytearray object to hexdecimal representation '''
    import codecs
    return codecs.getencoder('hex')(byte_array)[0]

def int_to_byte(val):
    ''' Convert hexadecimal integer to byte array '''
    return hex_to_byte(hex(val))

def int_to_str(val):
    ''' Convert hexadecimal integer to string '''
    return hex_to_str(hex(val))

# TODO: replace this (not compatible with python2)
def byte_to_bit(byte_array):
    ''' Bytearray to binary string '''
    return bin(int.from_bytes(byte_array, byteorder='big')).strip('0b')

# TODO: replace this (not compatible with python2)
def base_to_2byte(base_to_string):
    ''' Convert base-2 (01) string to bytearray '''
    return bytearray(int(base_to_string, 2).to_bytes((len(base_to_string) + 7) // 8, 'big'))

# Printing formatted data as string
# hex
# print "\x12\x02\x00"
# octal
# print "\112\102\x100"

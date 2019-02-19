from pwn import *

# general
proc = process('<target') # load process
proc = remote('<ip/hostname>', '<port>') # load url
text = proc.recvuntil('<text>') # run until text

# Execute shellcode on target binary
sh = process('<target>')

sh.sendlineafter('!\n', asm(shellcraft.i386.linux.sh()))
sh.interactive()

# Change hex value in file
with open('./<target-file>', 'rb') as f:
  data = f.read()

print (enhex(data[:]))

offset = 0

data = data[:0] + p16(0x0000) + data[0:]

with open('<new-file>', 'wb') as f:
  f.write(data)

# multi-precision integer arithmetic
import gmpy2
x = gmpy2.mpz(x)
gmpy2.iroot(x , n) # compute nth root of x
gmpy2.invertnc 2018shell.picoctf.com 37402(x, m) # modulus inverse
pow(x, y, m) # fast y^y mod m

# binary/hex conversion to ascii
import binascii
print(binascii.unhexlify('<hex_val>'[2:]))

# execute binary in gdb
bash = gdb.debug('<target-binary>', '''<initial commands>''')
bash.interactive()

# modify ELF file
f = ELF('<target-binary>')
f.asm(<address>, '<instruction>')
f.save('<new-location>')

# Printing formatted data as string
# hex
print "\x12\x02\x00"
# octal
print "\112\102\x100"
# binary
n = int('0b110100001100101011011000110110001101111', 2)
n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

# xor 2 strings together
def xor(a, b):
    a = bytearray(a)
    b = bytearray(b)
    out = bytearray()
    for i,c in enumerate(a):
        out.append(c ^ b[i])
    return bytes(out)

# convert binary data to hex
print hex(unpack('<binary-data>', 32, endian='little'))

# convert hex to binary data
print bytearray.fromhex('<hex-value>')

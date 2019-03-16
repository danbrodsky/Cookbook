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
gmpy2.invert(x, m) # modulus inverse
pow(x, y, m) # fast y^y mod m

# execute binary in gdb
bash = gdb.debug('<target-binary>', '''<initial commands>''')
bash.interactive()

# modify ELF file
f = ELF('<target-binary>')
f.asm('<address>', '<instruction>')
f.save('<new-location>')

# xor 2 strings together
def xor(a, b):
    a = bytearray(a)
    b = bytearray(b)
    out = bytearray()
    for i,c in enumerate(a):
        out.append(c ^ b[i])
    return bytes(out)

# load/disassemble a binary (*.pyc) module (Python2)
import pwn as moduleName
import dis
dis.dis('<module-name>')
moduleName.main()
moduleName.variableName

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
# lookup GOT entries in ELF file
print f.got['system']
# lookup symbol location in ELF file
print f.symbols['<func>']
# lookup bytearray location in ELF file
print next(f.search('/bin/sh\x00'))

# convert between integer and bytearray
b = bytearray('<32-bit-address>')
u32(b) # converts to 32-bit integer
p32(b) # converts back to bytes (little endian)

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

# decompile *.pyc file
>> uncompyle6 <target *.pyc file>


# Z3 solver
from z3 import *

x = Real('x') # use Real() for floating-point operations
y = Real('y')

array = [ BitVec('vec_%s' % i, 16) for i in range(30)  ]
S = Solver()

for i in range(30):
  S.add(array[i] >= 0)
  S.add(array[i] <= 255)

S.add(array[0] < 100, array[1] > 100)

S.add(x * x == y) # Same as saying x = sqrt(y)
S.add(x > 0) # add more constraints to prevent unwanted results

S.check()
S.model()


# Create a C struct
from ctypes import *
class struct(Structure):
    _fields_ = [
            ('attr1', c_int32),
            ('attr2', c_int32),
            ('attr3', c_int64),
            ]
    def to_bytes(self):
        return buffer(self)[:]

# parse data using regex
import re
r = re.compile("<regex> (capture-group> <regex>)")
s = '<target-string>'
capture_group = r.search(s).group(1)

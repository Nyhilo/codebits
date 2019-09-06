# In reference to this reddit thread https://redd.it/bjyhap

from struct import pack, unpack

# Note that ^ (xor) works on ints but not floats
def toIntAtMemLocation(num):
    return unpack('!i',pack('!f',num))[0]

def toFloatAtMemLocation(num):
    return unpack('!f',pack('!i',num))[0]

# values from Metacritic, IGN had too much water
ruby = toIntAtMemLocation(.82)  # 1062333317
go = toIntAtMemLocation(.69)    # 1060152279

print(bin(ruby))
print(bin(go))

print(toFloatAtMemLocation(go^ruby))    # 8.933986767093657e-39
print(bin(go^ruby))    # 8.933986767093657e-39
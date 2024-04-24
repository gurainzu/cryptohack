# -- [Crypto Hack Solver] -- #
import base64
from Crypto.Util.number import *
from math import *
from pwn import *

# --- ASCII --- #
#number = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
#result = ''.join(chr(num) for num in number)
#a = chr()

# --- HEX --- #
#hexstrings = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
#decoded_bytes = bytes.fromhex(hexstrings)
#print(decoded_bytes.decode('utf-8'))

# --- BASE64 --- #
#hexstrings = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#decoded_bytes = bytes.fromhex(hexstrings)
#encoded_bytes = base64.b64encode(decoded_bytes).decode('utf-8')
#print(encoded_bytes)

# --- Bytes and Big Integers --- #
#integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
#message_bytes = long_to_bytes(integer)
#flag = message_bytes.decode('utf-8')
#print(flag)

# --- XOR Starter --- #
#string = "label"
#flag = xor(string, 13).decode('utf-8')
#print("crypto{"+(flag)+"}")

# --- XOR Properties --- #
#def xorhexstring(hexstr1, hexstr2):
#   byte1 = bytes.fromhex(hexstr1)
#   byte2 = bytes.fromhex(hexstr2)
#   result = bytes(a ^ b for a, b in zip(byte1, byte2))
#   return result.hex()

#hexKEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
#hexKEY2xorKEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
#hexKEY2xorKEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
#hexFLAGxorKEY1xorKEY3xorKEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

#hexKEY2 = xorhexstring(hexKEY2xorKEY1, hexKEY1)
#hexKEY3 = xorhexstring(hexKEY2, hexKEY2xorKEY3)
#hexFLAG = xorhexstring(hexFLAGxorKEY1xorKEY3xorKEY2, hexKEY1)
#hexFLAG = xorhexstring(hexFLAG, hexKEY3)
#hexFLAG = xorhexstring(hexFLAG, hexKEY2)

#FLAG = bytes.fromhex(hexFLAG).decode('utf-8')
#print(FLAG)

# --- Favourite byte --- #

#def xor(string, key):
#    return bytes([byte ^ key for byte in string])

#def find_crypto(string):
#    bhanxor = 0
#    while True:
#        flag = xor(string, bhanxor)
#        if b'crypto' in flag:
#            return flag
#        bhanxor += 1

#string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
#string = bytes.fromhex(string)
#flag = find_crypto(string).decode('utf-8')
#print(flag)

# --- You either know, XOR you dont --- #

#flag = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
#key = (xor(flag, 'crypto{'.encode()))
#b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'# #ambil myXORkey aja
#key = ("myXORkey")
#print(xor(flag, key.encode()).decode('utf-8'))

# --- Extented GCD --- #

p = 26513
q = 32321

if p < q:
   p,q = q,p

r1,r2 = p,q
s1,s2 = 1,0
t1,t2 = 0,1

while r2 > 0:
   q,r = divmod(r1,r2)
   r1,r2 = r2,r
   s1,s2 = s2,s1 -q * s2
   t1,t2 = t2,t1 -q * t2

gcd = r1
u = t1
v = s1

print('GCD:',gcd, 'U:',u, 'V:', v)

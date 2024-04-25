## XOR Properties
<sup>15 pts</sup>

In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.

There are four main properties we should consider when we solve challenges using the XOR operator
>Commutative: A ⊕ B = B ⊕ A \
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C \
Identity: A ⊕ 0 = A \
Self-Inverse: A ⊕ A = 0

Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.

Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

```
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

Now we learn more complicated xoring, i cant expalin it well, just try to read the code, xD

```
from pwn import *

def xorhexstring(hexstr1, hexstr2):
   byte1 = bytes.fromhex(hexstr1)
   byte2 = bytes.fromhex(hexstr2)
   result = bytes(a ^ b for a, b in zip(byte1, byte2))
   return result.hex()

hexKEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
hexKEY2xorKEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
hexKEY2xorKEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
hexFLAGxorKEY1xorKEY3xorKEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

hexKEY2 = xorhexstring(hexKEY2xorKEY1, hexKEY1)
hexKEY3 = xorhexstring(hexKEY2, hexKEY2xorKEY3)
hexFLAG = xorhexstring(hexFLAGxorKEY1xorKEY3xorKEY2, hexKEY1)
hexFLAG = xorhexstring(hexFLAG, hexKEY3)
hexFLAG = xorhexstring(hexFLAG, hexKEY2)

FLAG = bytes.fromhex(hexFLAG).decode('utf-8')
print("Here's your flag :",FLAG)
```

<details>
<summary>and if you run the code, you'll get</summary>

  ```
Here's your flag : crypto{x0r_i5_ass0c1at1v3}
```
</details>

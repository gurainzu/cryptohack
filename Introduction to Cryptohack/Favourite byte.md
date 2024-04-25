## Favourite byte
<sup>20 pts</sup>

 For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

 I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

 ```
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
```

In the previous challange we xoring "label" with "13" and now we xoring this hex? idk xD, with secret thing. So the solve should be like ...

```
from pwn import *

def xor(string, key):
    return bytes([byte ^ key for byte in string])

def find_crypto(string):
    bhanxor = 0
    while True:
        flag = xor(string, bhanxor)
        if b'crypto' in flag:
            return flag
        bhanxor += 1

string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
string = bytes.fromhex(string)
flag = find_crypto(string).decode('utf-8')
print("Here's your flag :",flag)
```

<details>
<summary>and if you run the code, you'll get</summary>

  ```
Here's your flag : crypto{0x10_15_my_f4v0ur173_by7e}
```
</details>

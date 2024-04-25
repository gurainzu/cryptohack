## Bytes and Big Integers
<sup>10 pts</sup>

 Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

 The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

 To illustrate:
>message: HELLO \
ascii bytes: [72, 69, 76, 76, 79] \
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f] \
base-16: 0x48454c4c4f \
base-10: 310400273487

Hint : 
> Python's PyCryptodome library implements this with the methods bytes_to_long() and long_to_bytes(). You will first have to install PyCryptodome and import it with from Crypto.Util.number import *. For more details check the FAQ.

Convert the following integer back into a message:
```
11515195063862318899931685488813747395775516287289682636499965282714637259206269
```

From the explanation we can know RSA works on number, and the hint says we can use bytes_to_long() and long_to_bytes() from pycryptodome library in python. So the solve should be like...

To install pycryptodome :
```
pip install pycryptodome
```

And the solver : 
```
from Crypto.Util.number import *

integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
message_bytes = long_to_bytes(integer)
flag = message_bytes.decode('utf-8')
print("Here's your flag :",flag)
```
<details>
<summary>and if you run the code, you'll get</summary>

  ```
Here's your flag : crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
```
</details>

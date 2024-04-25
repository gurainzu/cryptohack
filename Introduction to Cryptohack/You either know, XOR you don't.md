## You either know, XOR you don't
<sup>30 pts</sup>

I've encrypted the flag with my secret key, you'll never be able to guess it. 

Hint :
>Remember the flag format and how it might help you in this challenge!

```
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
```
In this challange we know that the hint says the flag format which is "crypto{}", we can use that to find the secret key, and this should be the solver...

```
from pwn import *

flag = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
key = (xor(flag, 'crypto{'.encode()))

#b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f' << the xoring result the question with "crypto{", we just need to take the ""myXORkey"

key = ("myXORkey")
print("Here's your flag :",xor(flag, key.encode()).decode('utf-8'))
```

<details>
<summary>and if you run the code, you'll get</summary>

  ```
Here's your flag : crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
```
</details>

## Hex
<sup>5 pts</sup>
 
When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.
 
Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.

Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.

```
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
```

Hint :

>In Python, the bytes.fromhex() function can be used to convert hex to bytes. The .hex() instance method can be called on byte strings to get the hex representation.

In this course we will learn about converting hex to character, from the hint we know we can use bytes.fromhex() function to convert the hex, so the solve should be like...

```
hexstring = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
#make a variable to put the hex into a string

decoded_bytes = bytes.fromhex(hexstring)
#using bytes.fromhex() function to convert those string variable and store it in another variable

print("Here's your flag :", decoded_bytes.decode('utf-8'))
#printing the converted variable that store the flag
```

<details>
<summary>and if you run the code, you'll get</summary>

  ```
Here's your flag : crypto{You_will_be_working_with_hex_strings_a_lot}
```
</details>

## ASCII
<sup>5 pts</sup>

 ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127. Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.

 ```
[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
```

Hint : 

> In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).

In 'Great Snakes' we know we can use chr() to conver an ASCII number into a character like hint says, so we just have to..

```
number = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
#put the number that will be converted to character in list

flag = ''.join(chr(num) for num in number)
#converting every number in 'number' into character using chr() function and combine all combined character into one string.

print("Here's your flag : ", flag)
#printing the string (flag)
```

<details>
<summary>and if you run the code, you'll get</summary>

  ```
Here's your flag :  crypto{ASCII_pr1nt4bl3}
```
</details>

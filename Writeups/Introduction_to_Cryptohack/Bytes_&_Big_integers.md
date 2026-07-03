# Bytes and Big Integers

**Challenge Description:**  
Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

To illustrate:

```
message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487
```

Python's `PyCryptodome` library implements this with the methods `bytes_to_long()` and `long_to_bytes()`. You will first have to install PyCryptodome and import it with from `Crypto.Util.number import *`. For more details check the FAQ.

Convert the following integer back into a message:

```text
11515195063862318899931685488813747395775516287289682636499965282714637259206269
```

---

### Solve

The challenge provided a large decimal integer representing an encoded message.

The hint suggested using PyCryptodome's `long_to_bytes()` function, which converts a large integer into its corresponding bytes object.

After importing the required function, I stored the given integer in a variable and passed it to `long_to_bytes()`. Since the resulting value was a bytes object, I used `.decode()` to convert it into a readable string.

Python Code:

```python
from Crypto.Util.number import *

big_int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

flag = long_to_bytes(big_int)

print(flag.decode())
```

Output:

```text
crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
```

This produced the correct flag.

**Flag:**

```text
crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
```

---

### New Learnings

- Cryptographic algorithms such as **RSA** perform computations on **integers**, not directly on text.
- Messages are commonly converted into bytes and then interpreted as large integers before cryptographic operations are applied.
- **PyCryptodome** is a Python library that provides utility functions commonly used in cryptography.
- The `long_to_bytes()` function converts a large integer into its corresponding bytes representation.
- The `bytes_to_long()` function performs the reverse operation by converting a bytes object into a large integer.
- The `.decode()` method converts a bytes object into a human-readable string using a character encoding such as UTF-8.
- Converting between bytes and large integers is a fundamental concept in public-key cryptography and is widely used in RSA implementations.
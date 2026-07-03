# Base64

**Challenge Description:**  
Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

Take the below hex string, decode it into bytes and then encode it into Base64.

```text
72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
```

In Python, after importing the `base64` module, the `base64.b64encode()` function can be used to encode bytes into Base64. Since the input is hexadecimal, it must first be converted into bytes using `bytes.fromhex()`.

---

### Solve

The challenge provided a hexadecimal string instead of plain text.

Since `base64.b64encode()` operates on bytes, the hexadecimal string first needed to be converted into a bytes object using `bytes.fromhex()`.

After obtaining the bytes, I encoded them into Base64 using Python's `base64.b64encode()` function and printed the resulting bytes object.

Python Code:

```python
import base64

hex_word = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytes_data = bytes.fromhex(hex_word)
flag = base64.b64encode(bytes_data)

print(flag)
```

Output:

```text
b'crypto/Base+64+Encoding+is+Web+Safe/'
```

The output is a bytes object, and the flag can be read directly from it.

**Flag:**

```text
crypto/Base+64+Encoding+is+Web+Safe/
```

---

### New Learnings

- **Base64** is an encoding scheme that represents binary data using **64 printable ASCII characters**.
- Each **Base64 character represents 6 bits**, meaning **4 Base64 characters encode 3 bytes (24 bits)**.
- Base64 is commonly used to safely transmit binary data over text-based protocols such as HTTP, email, HTML, and JSON.
- Python's `base64` module provides functions for Base64 encoding and decoding.
- The `base64.b64encode()` function accepts a **bytes object** and returns the Base64-encoded bytes.
- Since the challenge input was a hexadecimal string, it first had to be converted into bytes using `bytes.fromhex()` before it could be Base64 encoded.
- Base64 is **not encryption**; it is simply an encoding format that can be reversed without any key.
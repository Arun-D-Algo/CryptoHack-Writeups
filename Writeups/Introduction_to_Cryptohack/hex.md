# Hex

**Challenge Description:**  
When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.

Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.

Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.

```63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d```

In Python, the `bytes.fromhex()` function can be used to convert hex to bytes. The `.hex()` instance method can be called on byte strings to get the hex representation.

---

### Solve

The challenge provided a long hexadecimal string representing the flag.

The hint suggested using Python's `bytes.fromhex()` function, which converts a hexadecimal string directly into its corresponding bytes.

I stored the given hexadecimal string in a variable and used `bytes.fromhex()` to decode it. The resulting bytes object was then printed to reveal the flag.

Python Code: 

```python
hex_word = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

flag = bytes.fromhex(hex_word)

print(flag)
```

Output:

```text
b'crypto{You_will_be_working_with_hex_strings_a_lot}'
```

Since the output is a bytes object, it can also be decoded into a normal string using `.decode()`:

```python
print(flag.decode())
```

Output:

```text
crypto{You_will_be_working_with_hex_strings_a_lot}
```

This produced the correct flag.

**Flag:**

```text
crypto{You_will_be_working_with_hex_strings_a_lot}
```

---

### New Learnings

- **Hexadecimal (base-16)** is a numbering system that uses the digits `0–9` and the letters `A–F` (or `a–f`) to represent values from **0 to 15**.
- Each hexadecimal digit represents **4 bits**, so two hexadecimal digits represent exactly **1 byte (8 bits)**.
- Hexadecimal is commonly used to represent binary data in a compact, human-readable form.
- Python's `bytes.fromhex()` function converts a hexadecimal string into its corresponding bytes object.
- A **bytes object** is displayed with a leading `b`, indicating that it represents raw binary data rather than a normal string.
- The `.decode()` method converts a bytes object into a human-readable string using a character encoding such as UTF-8.
- Hexadecimal encoding is widely used in cryptography, networking, file formats, and CTF challenges because it provides a convenient textual representation of binary data.
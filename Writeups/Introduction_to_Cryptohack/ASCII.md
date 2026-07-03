# ASCII

**Challenge Description:**  
ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0–127.

Using the given integer array, convert each number into its corresponding ASCII character to obtain the flag.

[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).
---

### Solve

The challenge provided an array of decimal integers and mentioned that they represented ASCII values.

The hint suggested using Python's `chr()` function, which converts an ASCII (or Unicode) integer into its corresponding character.

I stored the given integer array in a Python list and iterated through each value, converting it into a character using `chr()`. Each character was appended to a string to reconstruct the original message.

```python
ASCII_code = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = ""

for i in ASCII_code:
    flag += chr(i)

print(flag)
```

Output:

```text
crypto{ASCII_pr1nt4bl3}
```

This produced the correct flag.

**Flag:**

```text
crypto{ASCII_pr1nt4bl3}
```

---

### New Learnings

- **ASCII (American Standard Code for Information Interchange)** is a 7-bit character encoding standard that represents 128 characters using decimal values from **0 to 127**.
- Printable characters such as letters, digits, punctuation, and symbols all have unique ASCII values (e.g., `65 → A`, `97 → a`, `48 → 0`).
- Python's `chr()` function converts an integer into its corresponding ASCII/Unicode character.
- Python's `ord()` function performs the reverse operation by converting a character into its integer ASCII/Unicode value.
- A list of ASCII values can be decoded by iterating through the list and converting each integer using `chr()`, then joining the resulting characters into a string.
- ASCII encoding is commonly encountered in cryptography and CTF challenges as one of the most basic forms of text representation.
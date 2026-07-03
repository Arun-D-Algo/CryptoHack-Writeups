# Favourite byte

**Challenge Description:**  
For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

```text
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
```

---

### Solve

The challenge provided a hexadecimal string that had been encrypted using XOR with a **single unknown byte**.

The first step was to convert the hexadecimal string into bytes using Python's `bytes.fromhex()` function.

Since the XOR key was only **one byte**, there are only **256 possible keys** (0–255). I created a simple XOR function and brute-forced every possible key by XORing the ciphertext with each value from 0 to 255.

Any outputs that could not be decoded as UTF-8 were ignored using a `try`/`except` block. Among the readable outputs, one clearly revealed the flag.

Python Code:

```python
KEY = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

def xor(data, key):
    return bytes(b ^ key for b in data)

for key in range(256):
    try:
        print(key, xor(KEY, key).decode())
    except:
        pass
```

Output (Relevant):

```text
16 crypto{0x10_15_my_f4v0ur173_by7e}
```

The correct key was **16** (`0x10` in hexadecimal), which successfully decrypted the ciphertext.

**Flag:**

```text
crypto{0x10_15_my_f4v0ur173_by7e}
```

---

### New Learnings

- **XOR with a single-byte key** means every byte of the plaintext is XORed with the same value.
- A single-byte XOR cipher has only **256 possible keys**, making brute-force attacks practical.
- `bytes.fromhex()` converts a hexadecimal string into its corresponding byte sequence.
- The XOR operation on bytes can be performed using the `^` operator.
- `range(256)` iterates through every possible one-byte key (0–255).
- Using `try`/`except` while decoding helps ignore invalid UTF-8 outputs during brute-force.
- The key **16** is represented as **0x10** in hexadecimal, which is reflected in the challenge's flag.
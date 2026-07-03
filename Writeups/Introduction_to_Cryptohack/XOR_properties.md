# XOR Properties

**Challenge Description:**  
In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.

There are four main properties we should consider when we solve challenges using the XOR operator.

```text
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity:    A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0
```

Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.

Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

```text
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

---

### Solve

The challenge provided four hexadecimal values related through XOR operations. Using the four fundamental XOR properties, the missing keys and the flag could be recovered.

Since:

- `KEY2 ^ KEY1` was given, `KEY2` could be recovered by XORing the value with `KEY1`.
- `KEY2 ^ KEY3` was given, `KEY3` could be recovered by XORing the value with the recovered `KEY2`.
- Finally, the encrypted flag (`FLAG ^ KEY1 ^ KEY3 ^ KEY2`) was XORed with `KEY2`, `KEY3`, and `KEY1` to cancel out each key, leaving only the original flag.

I first created a helper function to XOR two byte strings together, then used `bytes.fromhex()` to convert each hexadecimal string into bytes before performing the XOR operations.

Python Code:

```python
def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2KEY1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAGKEY1KEY3KEY2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

KEY2 = xor(KEY2KEY1, KEY1)
KEY3 = xor(KEY2KEY3, KEY2)
FLAG = xor(xor(xor(FLAGKEY1KEY3KEY2, KEY2), KEY3), KEY1)

print(FLAG.decode())
```

Output:

```text
crypto{x0r_i5_ass0c1at1v3}
```

This produced the correct flag.

**Flag:**

```text
crypto{x0r_i5_ass0c1at1v3}
```

---

### New Learnings

- **Commutative Property:** `A ⊕ B = B ⊕ A`, meaning the order of XOR operands does not matter.
- **Associative Property:** `A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C`, allowing XOR operations to be grouped in any order.
- **Identity Property:** XORing any value with `0` leaves it unchanged (`A ⊕ 0 = A`).
- **Self-Inverse Property:** XORing a value with itself always produces `0` (`A ⊕ A = 0`).
- These properties allow unknown values to be recovered by rearranging XOR expressions, making XOR-based encryption reversible when the required keys are known.
- `bytes.fromhex()` is useful for converting hexadecimal strings into bytes before performing byte-wise XOR operations.
- A custom XOR function can be implemented by XORing corresponding bytes from two byte strings using Python's `zip()` function.
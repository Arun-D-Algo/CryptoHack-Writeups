# You either know, XOR you don't

**Challenge Description:**  
I've encrypted the flag with my secret key, you'll never be able to guess it.

**Hint:**  
Remember the flag format and how it might help you in this challenge!

```text
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
```

---

### Solve

The challenge provided a hexadecimal string encrypted using a **repeating-key XOR** cipher.

Since every CryptoHack flag begins with the known prefix `crypto{`, the hint suggested using this known plaintext to recover part of the encryption key.

First, I converted the hexadecimal string into bytes using `bytes.fromhex()`.

Knowing that:

```text
Ciphertext = Plaintext XOR Key
```

the key can be recovered by XORing the known plaintext with the corresponding ciphertext bytes:

```text
Key = Ciphertext XOR Plaintext
```

XORing the first eight ciphertext bytes with the known prefix `crypto{` produced:

```text
myXORke
```

From this, it was easy to infer that the complete repeating key was:

```text
myXORkey
```

I then decrypted the entire ciphertext by XORing each ciphertext byte with the corresponding byte of the repeating key, wrapping around the key using the modulo operator.

Python Code:

```python
cipher = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
key = b"myXORkey"

flag = bytes(cipher[i] ^ key[i % len(key)] for i in range(len(cipher)))

print(flag.decode())
```

Output:

```text
crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
```

This produced the correct flag.

**Flag:**

```text
crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
```

---

### New Learnings

- **Repeating-key XOR** encrypts data by XORing each plaintext byte with a repeating sequence of key bytes.
- If part of the plaintext is already known (such as the `crypto{` flag prefix), the corresponding key bytes can be recovered using:
  ```text
  Key = Ciphertext XOR Plaintext
  ```
- XOR is its own inverse, meaning:
  ```text
  A XOR B XOR B = A
  ```
  This property allows both encryption and decryption using the same operation.
- The modulo operator (`%`) is commonly used to repeat the key during encryption and decryption.
- This challenge demonstrates a **known-plaintext attack**, where knowledge of part of the original message allows recovery of the encryption key.
- Reusing a repeating XOR key is insecure because known plaintext can reveal the key and compromise the entire ciphertext.
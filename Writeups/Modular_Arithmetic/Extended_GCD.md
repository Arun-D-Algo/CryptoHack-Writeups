# Extended GCD

**Challenge Description:**  
Let *a* and *b* be positive integers.

The extended Euclidean algorithm is an efficient way to find integers *u*, *v* such that

> **a · u + b · v = gcd(a, b)**

Later, when we learn to decrypt RSA ciphertexts, we will need this algorithm to calculate the modular inverse of the public exponent.

Using the two primes **p = 26513** and **q = 32321**, find the integers *u*, *v* such that

> **p · u + q · v = gcd(p, q)**

Enter whichever of *u* and *v* is the lower number as the flag.

---

## Solution

Since `p` and `q` are both prime numbers, we know:

```text
gcd(p, q) = 1
```

The goal is therefore to find integers `u` and `v` satisfying:

```text
26513u + 32321v = 1
```

This can be done using the **Extended Euclidean Algorithm**, which computes both the greatest common divisor and the Bézout coefficients (`u` and `v`).

The following Python script was used:

```python
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


p = int(input("Enter first number : "))
q = int(input("Enter second number : "))

gcd, u, v = extended_gcd(p, q)

print("GCD =", gcd)
print("u =", u)
print("v =", v)

print("Verification:")
print(p * u + q * v)
```

Running the script produces:

```text
GCD = 1
u = 10245
v = -8404

Verification:
1
```

The challenge asks for the **lower** of the two coefficients.

### Flag

```text
-8404
```

---

### New Learning

- The **Extended Euclidean Algorithm** computes both the Greatest Common Divisor (GCD) and the Bézout coefficients `u` and `v` that satisfy `a·u + b·v = gcd(a, b)`.

- If two numbers are **coprime** (GCD = 1), the algorithm can express `1` as a linear combination of those two numbers. This property is essential for finding modular inverses.

- Unlike the standard Euclidean Algorithm, the extended version keeps track of additional coefficients while recursively working back through the division steps.

- The Extended Euclidean Algorithm is widely used in cryptography, particularly in **RSA**, where it is used to compute modular multiplicative inverses.
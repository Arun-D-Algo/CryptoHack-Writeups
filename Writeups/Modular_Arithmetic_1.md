# Modular Arithmetic 1

**Challenge Description:**  
Imagine you lean over and look at a cryptographer's notebook. You see some notes in the margin:

```text
4 + 9 = 1
5 - 7 = 10
2 + 3 = 5
```

At first you might think they've gone mad. Maybe this is why there are so many data leaks nowadays you'd think, but this is nothing more than modular arithmetic modulo 12 (albeit with some sloppy notation).

You may not have been calling it modular arithmetic, but you've been doing these kinds of calculations since you learnt to tell the time (look again at those equations and think about adding hours).

Formally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo **m** if **a ≡ b mod m**.

Another way of saying this, is that when we divide the integer **a** by **m**, the remainder is **b**. This tells you that if **m** divides **a** (this can be written as **m|a**) then **a ≡ 0 mod m**.

Calculate the following integers:

```text
11 ≡ x mod 6
8146798528947 ≡ y mod 17
```

The solution is the smaller of the two integers, *(x, y)*, you obtained after reducing by the modulus.

---

## Solution

In modular arithmetic, finding a number modulo another simply means finding the **remainder** after division.

The following Python script was used:

```python
num1 = int(input("Enter dividend 1 : "))
mod1 = int(input("Enter divisor 1 : "))
num2 = int(input("Enter dividend 2 : "))
mod2 = int(input("Enter divisor 2 : "))

x = num1 % mod1
y = num2 % mod2

print(f"{num1} = {x} mod {mod1}")
print(f"{num2} = {y} mod {mod2}")
```

Running the script with the given values produces:

```text
11 = 5 mod 6
8146798528947 = 4 mod 17
```

The challenge asks for the **smaller** of the two values.

### Flag

```text
4
```

---

## New Learning

- Modular arithmetic is based on the **remainder** obtained after dividing one number by another.
- In Python, the `%` operator directly computes the modulo (remainder) of two integers.
- Two integers are **congruent modulo m** if they leave the same remainder when divided by `m`.
- Modular arithmetic is widely used in cryptography because it keeps numbers within a fixed range while preserving useful mathematical properties.
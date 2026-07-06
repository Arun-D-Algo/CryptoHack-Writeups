# Greatest Common Divisor

**Challenge Description:**  
The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b).

For a=12,b=8 we can calculate the divisors of a: {1,2,3,4,6,12} and the divisors of b: {1,2,4,8}. Comparing these two, we see that gcd(a,b)=4.

Now imagine we take a=11,b=17. Both a and b are prime numbers. As a prime number has only itself and 1 as divisors, gcd(a,b)=1.

We say that for any two integers a,b, if gcd(a,b)=1 then a and b are coprime integers.

If a and b are prime, they are also coprime. If a is prime and b < a then a and b are coprime.

Think about the case for a prime and b>a, why are these not necessarily coprime?

There are many tools to calculate the GCD of two integers, but for this task we recommend looking up Euclid's Algorithm.

Try coding it up; it's only a couple of lines. Use a=12,b=8 to test it.

Now calculate gcd(a,b) for a=66528,b=52920 and enter it below.

```text
gcd(66528, 52920)
```

---

### Solve

Instead of checking every possible divisor, I implemented **Euclid's Algorithm**, which repeatedly replaces the larger number with the remainder obtained after division.

The algorithm is based on the identity:

```text
gcd(a, b) = gcd(b, a mod b)
```

This process continues until the second number becomes `0`. At that point, the first number is the Greatest Common Divisor.

I created a Python function that repeatedly performs this operation using a `while` loop. After taking the two integers as input, the function returns their GCD.

Python Code:

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))

print(f"GCD of {a} and {b} is : {gcd(a, b)}")
```

Output:

```text
Enter First number : 66528
Enter Second number : 52920
GCD of 66528 and 52920 is : 1512
```

This produced the correct answer.

**Answer:**

```text
1512
```

---

### New Learnings

- The **Greatest Common Divisor (GCD)** is the largest positive integer that divides two numbers exactly.
- Two numbers are **coprime** if their GCD is `1`, even if neither number is prime.
- **Euclid's Algorithm** is the fastest and most commonly used algorithm for finding the GCD of two integers.
- The algorithm relies on the mathematical property:

  ```text
  gcd(a, b) = gcd(b, a mod b)
  ```

- The algorithm terminates when the second number becomes `0`; the remaining first number is the GCD.
- Using the modulo (`%`) operator repeatedly is significantly more efficient than checking every possible divisor, especially for large numbers.
- Euclid's Algorithm has a time complexity of **O(log(min(a, b)))**, making it one of the oldest and most efficient algorithms still widely used in mathematics, cryptography, and computer science.
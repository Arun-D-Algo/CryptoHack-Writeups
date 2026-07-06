def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
print(f"GCD of {a} and {b} is : {gcd(a,b)}")

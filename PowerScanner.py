# Power of Two Scanner

n = int(input("Enter a number: "))

# Remove the rightmost set bit
removed = n & (n - 1)

print("After removing rightmost set bit:", removed)

# Check power of 2
if n > 0 and (n & (n - 1)) == 0:
    print("It is a power of 2")
else:
    print("It is not a power of 2")

# Check powers of 2, 4 and 8
if n == 2:
    print("It is 2")
elif n == 4:
    print("It is 4")
elif n == 8:
    print("It is 8")
else:
    print("It is not 2, 4, or 8")

# Binary exponentiation
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

while exponent > 0:
    if exponent & 1:
        result = result * base

    base = base * base
    exponent = exponent >> 1

print("Power:", result)
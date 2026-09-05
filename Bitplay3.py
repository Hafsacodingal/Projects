
a=56
b=12

#Part1
print("===Bitplay 3===")
print("Before: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("Swapped: a =", a, "b =", b)
print()

#Part2
a= 56
b= 12
a= a ^ b
b= a ^ b
a= a ^ b
print("XOR Swap: a =", a, "b =", b)
print()

#Part3
print("Left Shift:")
print("3 << 1 =", 3 << 1)
print("3 << 2 =", 3 << 2)
print("3 << 3 =", 3 << 3)
print("3 << 4 =", 3 << 4)
print("3 << 5 =", 3 << 5)
print()

#Part4
def divide(a, b):
    negative = (a < 0) ^ (b < 0)
    a= abs(a)
    b= abs(b)
    count = 0
    while a >= b:
        a = a - b
        count = count + 1
    if negative:
        count = -count
    return count

print("Divide without / operator:")
print("50 / 2 =", divide(50, 2))
print("72 /3 =", divide(72, 3))
print("-50 / 2 =", divide(-50, 2))
print("50 / -2 =", divide(50, -2))

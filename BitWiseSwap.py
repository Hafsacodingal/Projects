a=5
b= 3
print("===BitWise Swap Challenge===")
print("Before: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("Swapped: a =", a, "b =", b)
print()

a=5
b= 3
a= a ^ b
b= a ^ b
a= a ^ b
print("XOR Swap: a =", a, "b =", b)
print()



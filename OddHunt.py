
a,b=7,7

print("===Odd Hunt===")
print("a ^ a =", a ^ a)
print("a^0 =", a ^ 0)
print("Equal (XOR):", (a ^ b) == 0)
print()

arr = [3, 5, 3, 5, 9]
result = 0
for n in arr: result ^= n
print("XOR of ",arr, "=", result)
print()

nums = [4,7,4,2,7,2,9]
result = 0
for n in nums: result ^= n
print("Odd occurring: ", result)
print()

pair = [3,9,3,5,5,7]
Xab=0
for n in pair: Xab ^= n
print("XOR of two odds: ", Xab,"->", bin(Xab))
print()

setbit = Xab & -Xab
x, y = 0, 0
for n in pair:
    if n & setbit: x ^= n
    else: y ^= n
print("Two odd-occurring: ", x,"and", y)

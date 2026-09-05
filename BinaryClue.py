print("================================")
print("BINARY CLUE INVESTIGATOR")
print("================================")

# Part 1: XOR Identity

a = 7
b = 7

print("\nPART 1: XOR Identity")
print("a ^ a =", a ^ a)
print("a ^ 0 =", a ^ 0)

if a ^ b == 0:
    print("Both numbers are equal")
else:
    print("Both numbers are different")


# Part 2: XOR Cancellation

clues = [3, 5, 3, 5, 9]

result = 0

for number in clues:
    result = result ^ number

print("\nPART 2: XOR Cancellation")
print("Remaining number:", result)


# Part 3: One Odd-Occurring Number

numbers = [4, 7, 4, 2, 7, 2, 9]

result = 0

for number in numbers:
    result = result ^ number

print("\nPART 3: One Odd-Occurring Number")
print("Odd-occurring number:", result)


# Part 4: Two Odd-Occurring Numbers

numbers = [3, 9, 3, 5, 5, 7]

result = 0

for number in numbers:
    result = result ^ number

print("\nPART 4: Two Odd-Occurring Numbers")
print("XOR result:", result)


# Part 5: Rightmost Set Bit

bit = result & -result

first = 0
second = 0

for number in numbers:
    if number & bit:
        first = first ^ number
    else:
        second = second ^ number

print("\nPART 5: Rightmost Set Bit")
print("First odd-occurring number:", first)
print("Second odd-occurring number:", second)

print("\n================================")
print("SUMMARY")
print("One odd number:", 9)
print("Two odd numbers:", first, "and", second)
print("================================")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    greater = number1
else:
    greater = number2

while True:
    if greater % number1 == 0 and greater % number2 == 0:
        lcm = greater
        break
    greater += 1

print("LCM =", lcm)
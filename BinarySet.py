items=["A","B","C"]
n=len(items)
print("===Binary Subset Building===")
print("Power Set:",)

for mask in range(2**n):
    subset=[]
    for i in range(n):
        if mask & (1 << i):
            subset.append(items[i])
    print(subset)

print("\nBit Difference")
a=3
b=5
difference=a^b
count=0
for i in range(8):
    if difference & (1 << i):
        count+=1

print("Number of differing bits:", count)

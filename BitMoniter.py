
switches=56
def bits(n): return bin(n)[2:]

print("===My Smart Switch Bit Monitor===")
print("Switches: ", switches)
print("Bits: ", bits(switches))
print("Binary Representation: ", bits(switches))
print("Decimal Representation: ", switches)
print()

if switches > 0:
    print("Switches are ON")
    print("Number of ON switches: ", bits(switches).count('1'))

elif switches == 0:
    print("All switches are OFF")
elif switches < 0:
    print("Invalid switch count")
else:
    print("Switches are OFF")


    

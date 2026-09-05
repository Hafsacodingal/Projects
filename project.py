
n=12

print("===POWERS Surge===")
print("n=", n,"->",bin(n))
print("n-1=", n-1,"->",bin(n-1))
print("n & (n-1)=", n & (n-1),"->",bin(n & (n-1)))
print()

print("Powers of 2 check")
for x in [1,4,6,16,18,64]:
    result=x>>0 and (x & (x-1))==0
    print("",x,"->",bin(x),"-> ",result)
print()

def pow4(n):
    if n<=0 or n & (n-1) != 0: 
        return False
    count=0
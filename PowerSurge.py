
n=12
#part1
print("===Power Surge===")
print("n=",n,"->",bin(n))
print("n-1=",n-1,"->",bin(n-1))
print("n & (n-1)=",n & (n-1),"->",bin(n & (n-1)))
print()

#part2
print("===Power of 2 check===")
for x in[1,4,6,16,18,64]:
    result=x>>0 and (x & (x-1))==0
    print("",x,"->",bin(x),"->",result)
print()

#part3
def Pow4(n):
    if n<=0 or n & (n-1)!=0:
        return False
    count=0
    while n>1:
        n=n>>1
        count=count+1
    return count%2==0

print("===Power of 4 check===")
for x in [1,4,8,16,32,64]:
    print("",x,"->",Pow4(x))
print()

#part4
def Pow8(n):
    if n<=0 or n & (n-1)!=0:
        return False
    count=0
    while n>1:
        n=n>>1
        count=count+1
    return count%3==0

print("===Power of 8 check===")
for x in [1,8,16,64,32,512]:
    print("",x,"->",Pow8(x))
print()

#part5
def fast_power(base,exp):
    result=1
    while exp>0:
        if exp & 1==1:
            result=result*base
        base=base*base
        exp=exp>>1
    return result

print("Binary exponentiation:")
print("6^5=",fast_power(6,5))
print("2^10=",fast_power(2,10))
print("3^8=",fast_power(3,8))
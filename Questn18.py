# O(nlogn)
n=16
bits=[None]*(n+1)

for i in range(n+1):
    count=0
    temp=i
    while temp>0:
        count+=temp%2
        temp=temp//2
    bits[i]=count

print(bits)


# O(n)

i=1
while i<=n:
    i=2*i
print(i)
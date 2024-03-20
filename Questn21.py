

#basic approach
nums=[1,2,3,4,5]
temp=[1]*len(nums)
for i in range(len(temp)):
    for j in range(len(nums)):
        if i==j:
            continue
        temp[i]*=nums[j]

print(temp)

print('-----------------------------')
#using math concept approach but in this we cannot deal with zero in array
nums=[-1,1,0,-3,3]
nums=[0,0] #it is not working with this input after modifying also to work with 0 ininput
result=1
flag=0
for i in range(len(nums)):
    if nums[i]==0:
        flag=1
        continue
    else:
        result*=nums[i]
if flag==1:
    for i in range(len(nums)):
        if nums[i]==0:
            nums[i]=result
        else:
            nums[i]=0
else:
    for i in range(len(nums)):
        nums[i]=result//nums[i]

print(nums)

print('-----------------------------')
#using prifix suffix approach

nums=[1,2,3,4,5]
suffix=[1]*len(nums)
prefix=[1]*len(nums)
n=len(nums)
for i in range(1,n):
    prefix[i]=prefix[i-1]*nums[i-1]
    suffix[n-1-i]=suffix[n-i]*nums[n-i]
print(prefix,suffix)

for i in range(n):
    nums[i]=prefix[i]*suffix[i]
print(nums)

print('-----------------------------')
#using only one extra array
nums=[1,2,3,4,5]
n=len(nums)
suffix=[1]*len(nums)
for i in range(1,n):
    suffix[n-1-i]=suffix[n-i]*nums[n-i]
print(suffix)
print(nums)
prod=1
for i in range(0,n):
    temp=prod*suffix[i]
    prod=nums[i]*prod
    nums[i]=temp
print(nums)

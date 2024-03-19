


nums=[1,2,3,4,5]
temp=[1]*len(nums)
for i in range(len(temp)):
    for j in range(len(nums)):
        if i==j:
            continue
        temp[i]*=nums[j]

print(temp)

nums=[-1,1,0,-3,3]
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
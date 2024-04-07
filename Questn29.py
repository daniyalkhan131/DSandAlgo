def twoSum(nums,target):
    dic={}
    for i in range(len(nums)):
        dic[nums[i]]=i
    
    for i in range(len(nums)):
        try:
            b=dic[target-nums[i]]
            if b==i:
                continue
            else:
                return i,b
        except KeyError as error:
            continue
    return -1


nums=[3,2,4]
print(twoSum(nums,6))
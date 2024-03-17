nums = [2,7,4,5,9,0,6,8,3]
print(nums)
# nums.append(len(nums))
# for i in range(len(nums)):        

#     #temp=nums[nums[i]]
#     print(nums[nums[i]],nums[i])
#     nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
#     print(nums)
# for i in range(len(nums)):
#     nums[nums[i]],nums[i]=nums[i],nums[nums[i]]

# print(nums)

# for i in range(len(nums)):
# 	if i!=nums[i]:
# 		print('final',i)

indices_sum=len(nums)
element_sum=0
for i in range(len(nums)):
	indices_sum+=i
	element_sum+=nums[i]
print(indices_sum-element_sum)


print((n:=len(nums))*(n+1)//2-sum(nums))
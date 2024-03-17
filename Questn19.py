import math
nums=[1,2,3]
l=[]
#per= math.factorial(len(nums))


def perm(i,nums):

	if i==len(nums):
		print(nums)
		return
	
	for j in range(i,len(nums)):
		nums[i],nums[j]=nums[j],nums[i]
		perm(i+1,nums)
		nums[i],nums[j]=nums[j],nums[i]

perm(0,nums)
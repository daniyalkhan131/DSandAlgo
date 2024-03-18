nums=[1,2,3,4]
def perm(i,nums):

	if i==len(nums):
		print(nums)
		return
	
	for j in range(i,len(nums)):
		nums[i],nums[j]=nums[j],nums[i] #this is for swapping to get new list
		perm(i+1,nums)
		nums[i],nums[j]=nums[j],nums[i] #this is for swapping to get previous one as 
										#when we return we need to be in that state

perm(0,nums)
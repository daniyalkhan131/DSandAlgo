#https://leetcode.com/problems/next-permutation/

nums=[1,2,3,4,5,6]

# def swap(a,b):
#     a,b=b,a
# for i in range(len(nums)-1,-1,-1):
#     temp=nums.copy()
#     for j in range(i,0,-1):
#         if temp[j]>temp[j-1]:
#             breaker=True
#         temp[i],temp[j]=temp[j],temp[i]

#         if breaker:
#             break

def bubblesort(ptr,nums):
    for i in range(len(nums)-ptr):
        for j in range(ptr,len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

def nextPermutation(nums) -> None:
    ptr=-1
    for i in range(len(nums)-1,-1,-1):
        for j in range(len(nums)-1,i,-1):
            #print(nums[i],nums[j])
            if nums[i]<nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                ptr=i
                break
        if ptr!=-1:
            break
    bubblesort(ptr+1,nums)

nextPermutation(nums)
print(nums)

nums=[1,2,3]
#calculating all possible permuations
def fac(n):
    sum=1
    while n>0:
        sum=sum*(n)
        n-=1
    return sum

for i in range(fac(len(nums))):
    print(nums)
    nextPermutation(nums)
    
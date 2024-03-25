# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
# The solution set must not contain duplicate subsets. Return the solution 
#in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


# def power(w,i,j,arr):
    # if len(arr)<=1:
    #     return
    # for j in range(i+w-2,len(arr)):
    #     temp=arr[i:w-2]
    #     temp.append(j)
    #     res.append(temp)
    #     power(w,i,j,temp)
    

res=[]
def power(i,temp,arr):
    if i==len(arr):
        res.append(temp[:])
        print(temp)
        return
    temp.append(arr[i])
    power(i+1,temp,arr)
    temp.pop()
    power(i+1,temp,arr)

power(0,[],[1,2,3])
print(res)


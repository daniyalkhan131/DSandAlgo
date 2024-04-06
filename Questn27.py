#binary search

#recursion
def binary_search(arr,l,h,target):
    mid=(l+h)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,l,mid,target)
    else:
        return binary_search(arr,mid,h,target)
    
#direct approach
def binary_search_basic(arr,target):
    l,h=0,len(nums)-1
    mid=(l+h)//2
    while l<=h:
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        else:
            h=mid-1
        mid=(l+h)//2
    return -1


nums = [-1,0,3,5,9,12]
target = 13
print(binary_search_basic(nums,target))
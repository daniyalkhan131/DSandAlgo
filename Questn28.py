
# Given an n x n matrix where each of the rows and columns is sorted in 
# ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the 
# kth distinct element.
# You must find a solution with a memory complexity better than O(n2).


#this will not work because in this I assumed that smallest element can only in first
#row and first col then 2nd n so on

# def merging(l1,l2):
#     i,j=0,0
#     arr=[]
#     while i<len(l1) and j<len(l2):
#         if l1[i]<l2[j]:
#             arr.append(l1[i])
#             i+=1
#         else:
#             arr.append(l2[j])
#             j+=1
#     while i<len(l1):
#         arr.append(l1[i])
#         i+=1
#     while j<len(l2):
#         arr.append(l2[j])
#         j+=1

#     return arr

# def kthSmallest(mat,k):
#     for i in range(len(mat)):
#         temp=0
#         arr=merging(mat[i],[j[i] for j in mat])
#         print(arr)
#         try:
#             arr[k]
#         except IndexError as error:
#             print(f'not in {i}th row or col')
#         else:
#             temp=arr[k]
#             break
#         k=k-len(arr)+2
#     return temp


# using binary search

# As monotonicity is found we can use Binary Search
def countLesserThanMid(mat,mid):
    count =0
    for i in mat:
        j=0
        while j<len(i) and i[j]<=mid:
            j+=1
        count=count+j
    return count 

def kthSmallest(mat,k):
    n=len(mat)
    l,h=mat[0][0],mat[n-1][n-1]
    while l<h:
        mid=(l+h)//2
        count=countLesserThanMid(mat,mid)
        print(f'l={l}, h={h}, mid={mid}, count={count}')
        if count<k:
            l=mid+1
        else:
            h=mid
    print('return')
    return h


mat=[[1,3,5],[6,7,12],[11,14,14]]
for i in mat:
    for j in i:
        print(j,'\t',end="")
    print()
print(kthSmallest(mat=mat, k = 4))
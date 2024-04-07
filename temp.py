# l1=[1]*5
# l2=[0]*5

# for i in range(5):
# 	l1[i],l2[i]=l2[i],l1[i]
# print(l1,l2)


# l=[[1],[1,2],[3],[2,3],[8]]

# if [2,3] in l:
# 	print(True)

# for i in range(ord('a'),ord('z')+1):
# 	print(chr(i))

# mat=[[1,5,9],[10,11,13],[12,13,15]]
# print(mat[0])
def countLesserThanMid(mat,mid):
	count =0
	j=0
	while j<len(mat) and mat[j]<=mid:
		j+=1
		count=count+1
	return count 

def kthsmallest(arr,k):
	l=arr[0]
	h=arr[len(arr)-1]
	while l<h:
		mid=(l+h)//2
		count=countLesserThanMid(arr,mid)
		if count==k:
			return mid
		elif mid>k-1:
			h=mid-1
		else:
			l=mid+1
		
	return -1
def findk(arr,num):
	l=0
	h=len(arr)-1
	

	while l<=h:
		mid=(l+h)//2
		if num <arr[mid] and num<arr[mid+1]:
			h=mid-1
		elif num>arr[mid] and num>arr[mid+1]:
			l=mid+1
		else:
			return mid+1



l=[1,3,3,3,3,3,4,5,7,9,11,11,17,19,39,50]

# print(kthsmallest(l,8))
# print(l[7])

print('find k',findk(l,5))

d={1:11,2:22,3:44}
for i in d.items():
	print(i)
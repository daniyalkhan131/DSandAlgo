

def next_permutation(arr):
	count=0
	i=len(arr)-1
	j=i-1
	while arr[i]<arr[j]:
		count+=1
		j-=1
	print(count,j)
l=[2,3,4,1]
next_permutation(l)
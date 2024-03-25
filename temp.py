l1=[1]*5
l2=[0]*5

for i in range(5):
	l1[i],l2[i]=l2[i],l1[i]
print(l1,l2)


l=[[1],[1,2],[3],[2,3],[8]]

if [2,3] in l:
	print(True)
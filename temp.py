l1=[1]*5
l2=[0]*5

for i in range(5):
	l1[i],l2[i]=l2[i],l1[i]
print(l1,l2)
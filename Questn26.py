def anagram(s,p):
    
    # n=len(s)
    # m=len(p)
    # res=[]
    # for i in range(n-m+1):
    #     ht={}
    #     for j in range(i,m+i):
    #         try:
    #             ht[s[j]]+=1
    #         except KeyError as error:
    #             ht[s[j]]=1
        
    #     for k in p:
    #         try:
    #             ht[k]+=1
    #         except KeyError as error:
    #             continue
    #     count=0
    #     for k in p:
    #         try:
    #             if ht[k]%2==0:
    #                 count+=1
    #         except KeyError as error:
    #             continue
            
    #     if count==m:
    #         res.append(i)
    # return res


#with one global hash table
    # ht={}
    # freq=[]
    # res=[]
    # for i in range(ord('a'),ord('z')+1):
    #     ht[chr(i)]=0
    # for i in range(len(p)):
    #     ht[p[i]]+=1
    # print(ht)
    # for i in range(len(s)-len(p)+1):
    #     sum=0
    #     temp=ht.copy()
    #     for j in range(i,len(p)+i):
    #         try:
    #             if temp[s[j]]!=0:
    #                 temp[s[j]]-=1
    #                 sum+=1
    #         except KeyError as error:
    #             break
    #     if sum==len(p):
    #         res.append(i)
    # return res


#optimised
    #convert both to binary rep. of array then move window
    res=[]
    pArr=[0]*26
    sArr=[0]*26
    if len(p)>len(s):
        return res
    for i in range(len(p)):
        pArr[ord(p[i])-ord('a')]+=1
        sArr[ord(s[i])-ord('a')]+=1
    start=0
    end=len(p)
    if pArr==sArr:
        res.append(start)
    while end<len(s):
        sArr[ord(s[start])-ord('a')]-=1
        sArr[ord(s[end])-ord('a')]+=1
        if pArr==sArr:
            res.append(start+1)
        start+=1
        end+=1
    return res


s="cbaebabacd"
p='abc'
print(s)
res=anagram(s,p)
print(res)
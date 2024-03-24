# Given n pairs of parentheses, write a function to generate all combinations 
#of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
res=[]
n=3
def para(l,r,s):
    if len(s)==2*n:
        res.append(s)
        #print(s)
        return
    if l<n:
        para(l+1,r,s+"(")
    if r<l:
        para(l,r+1,s+')')
    
    
    

para(0,0,'')
print(res)

#with iteration approach
def para(n):
    result = []
    left = right = 0
    q = [(left, right, '')]
    while q:
        left, right, s = q.pop()
        if len(s) == 2 * n:
            result.append(s)
        if left < n:
            q.append((left + 1, right, s + '('))
        if right < left:
            q.append((left, right + 1, s + ')'))
    return result
print(para(3))
# Given n pairs of parentheses, write a function to generate all combinations 
#of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

def para(n):
    strr=''
    print(strr)
    if n<=0:
        return
    
    para(n-1)
    strr+='('
    #print('(',end='')
    para(n-1)
    strr+=')'
    #print(')',end='')
    

para(3)
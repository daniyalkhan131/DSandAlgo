#https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#  


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l=[]
        # temp=[]
        # # if len(s)==1:
        # #     return 1
        # for i in s:
        #     if i not in l:
        #         l.append(i)
        #         print('if ',i)
        #     else:
        #         if len(temp)<=len(l):
        #             temp=l.copy()
        #         l=[]
        #         l.append(i)
        #         print('else ',i)
        #         t=len(temp)-1
        #         while temp[t]!=i:
        #             l.append(temp[t])
        #             t-=1
        #         print('temp ',temp)
        #         print('l ',l)
        # if len(temp)==0 or len(temp)<len(l):
        #     return len(l)
        # return len(temp)

        # l=[]
        # maxx=0
        # for i in s:
            
            
        #     if i not in l:
        #         l.append(i)
        #     else:
        #         temp1=[]
        #         temp2=[]
        #         while True:
        #             a=l.pop()
        #             if a==i:
        #                 break
        #             temp1.append(a)
        #         while len(temp1)!=0:
        #             temp2.append(temp1.pop())
        #         l=temp2.copy()
        #         l.append(i)
        #     print(l)

        #     if len(l)>maxx:
        #         maxx=len(l)

        # return maxx

        #sliding window with hash table
#not working but try to make this work properly
        l,h=0,0
        ht={}
        s=list(s)
        while h<len(s):
            if s[h] in ht:
                while s[l]!=s[h]:
                    l+=1
                l+=1
            else:
                ht[s[h]]=1
            h+=1
        return h-l
s=Solution()
print(s.lengthOfLongestSubstring('aujhvmca'))








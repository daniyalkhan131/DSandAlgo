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
        l=[]
        temp=[]
        # if len(s)==1:
        #     return 1
        for i in s:
            if i not in l:
                l.append(i)
            else:
                if len(temp)<len(l):
                    temp=l[:]
                l=[]
                l.append(i)
                t=len(temp)-1
                while temp[t]!=i:
                    l.append(temp[t])
                    t-=1
        if len(temp)==0 or len(temp)<len(l):
            return len(l)
        return len(temp)

s=Solution()
print(s.lengthOfLongestSubstring('ababd'))
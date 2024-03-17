# https://leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"


import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s)==0 or len(s)==1 or numRows==1:
            return s
        col=len(s)//2
        l = [['-' for i in range(2*col)] for j in range(numRows)]
        k=0
        t=0
        while t<len(s):
            i=0
            j=numRows-2
            while i < numRows and t<len(s):
                l[i][k]=s[t]
                t+=1
                i+=1
            while j>0 and t<len(s):
                k+=1
                l[j][k]=s[t]
                t+=1
                j-=1
            k+=1
        strr=""
        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j]!='-':
                    strr+=l[i][j]

        for i in l:
            print()
            for j in i:
                print(f' {j} ',end='')
        print()
        return strr

s=Solution()
print(s.convert("DANIYALKHAN",4))
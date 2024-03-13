# https://leetcode.com/problems/rotate-list/

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int)-> ListNode:

    	#this is the direct method I used that is O(n*k)

        # for i in range(k):
        #     if head==None:
        #         return None
        #     if head.next==None:
        #         return head
        #     ptr=head
        #     while ptr.next.next!=None:
        #         ptr=ptr.next
        #     ptr.next.next=head
        #     head=ptr.next
        #     ptr.next=None
        # return head

        #this i wrote but is it also giving time exceeding
        #as if LL is very big and t= len(LL)-1 then it also O(n^2)

        # if head==None:
        #     return None
        # if head.next==None or k==0:
        #     return head
        # while ptr.next.next!=None:
        #     count+=1
        #     ptr=ptr.next
        # if k>count:
        #     t=(k%count+1)%count
        # if count==k:
        #     return head
        # else:
        #     t=k
        # for i in range(t):
        #     ptr=head
        #     while ptr.next.next!=None:
        #         ptr=ptr.next
        #     ptr.next.next=head
        #     head=ptr.next
        #     ptr.next=None


        #rotation LL

        if head==None:
            return None
        ptr=head
        n=1
        while ptr.next!=None:
            ptr=ptr.next
            n+=1
        ptr.next=head

        if k>=n:
            k=k%n
        t=n-k
        for i in range(t):
            ptr=ptr.next
        head=ptr.next
        ptr.next=None
        return head

s=Solution()
#s.rotateRight()
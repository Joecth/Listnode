#!usr/bin/python
'''Hihi'''
'''Good Morning!'''
'''night already 0506'''
class Solution(object):
    def reverseList(self, head):
        prev,cur=None,head
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        return prev
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:return None
        prev=ListNode(-1)
        cur=prev
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        if l1:cur.next=l1
        else:cur.next=l2
        return prev.next
    def getIntersectionNode(self, headA, headB):
        if headA==None or headB==None:return None
        p,q=headA,headB
        while p!=q:
            p=p.next if p else headB
            q=q.next if q else headA
        return p
    def removeNthFromEnd(self, head, n):
        prev,prev.next=self,head
        slow,fast=prev,prev
        while fast.next:
            if n<=0:
                slow=slow.next
            fast=fast.next
            n-=1
        if slow.next:
            slwo.next=slow.next.next
        return prev.next
    def isPalindrome(self, head):
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        while slow:
            nex=slow.next
            slow.next=prev
            prev=slow
            slow=nex
            
        while prev:
            if prev.val!=head.val:return False
            prev=prev.next
            head=head.next
        return True
    def deleteDuplicates(self, head):
        cur=head
        while cur:
            while cur.next and cur.next.val==cur.val:
                cur.next=cur.next.next
            cur=cur.next
        return head
    def swapPairs(self, head):
        prev,prev.next=self,head
        while prev.next and prev.next.next:
            a=prev.next
            b=a.next
            prev.next,a.next,b.next=b,b.next,a
            prev=a
        return self.next
    def removeElements(self, head, val):
        prev=ListNode(-1)
        cur=prev
        prev.next=head
        while prev and prev.next:
            while  prev.next and prev.next.val==val:
                prev.next=prev.next.next
            prev=prev.next
        return cur.next
    def swapPairs(self, head):
        prev,prev.next=self,head
        while prev.next and prev.next.next:
            cur=prev.next
            nex=cur.next
            cur.next=nex.next
            nex.next=cur
            prev.next=nex
            prev=cur
        return self.next

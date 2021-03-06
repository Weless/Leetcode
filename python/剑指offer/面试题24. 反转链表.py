class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head,None
        while head:
            head = head.next
            cur.next = pre
            pre = cur
            cur = head
        return pre


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pass


def reverse(head: ListNode) -> ListNode:
    # null 1 -> 2 -> 3 -> 4 -> null
    p = head       # prev
    c = head       # curr
    n = head.next  # next
    c.next = None
    while n != None:
        c = n
        n = n.next
        c.next = p
        p = c
    head = c
    return head


def printLL(head: ListNode):
    output = ""
    while head != None:
        if head.next != None:
            output += str(head.val) + ' -> '
        else:
            output += str(head.val)
        head = head.next
    return output


LL = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(printLL(LL))
print(printLL(reverse(LL)))

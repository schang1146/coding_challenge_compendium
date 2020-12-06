class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """

        ____ Solution

        Time Complexity: O(_)
        Space Complexity: O(_)

        """

        # edge case: if k == 1, no switches occur
        if k == 1:
            return head

        # check how many windows will need to be reversed
        node_ct = 0
        c = head
        while c != None:
            node_ct += 1
            c = c.next

        # reverse windows
        start = head        # pointer @ start of window
        first_run = True
        for _ in range(node_ct // k):
            # initialize necessary pointers / counter
            ct = 0          # counter for how many nodes we are reversing
            p = start       # previous pointer
            c = start       # current pointer
            n = start.next  # next pointer

            # reverse current window
            while ct < k - 1:
                c = n
                n = n.next
                c.next = p
                p = c
                ct += 1     # increase counter

            start.next = n

            # if first run, reset head pointer
            if first_run == True:
                head = c
                first_run = False
                prev_end = start
            # else, connect reversed linked list to rest of list
            else:
                prev_end.next = c
                prev_end = start

            start = n  # move start to beginning of next window

        return head

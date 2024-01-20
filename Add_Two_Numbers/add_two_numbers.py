#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 20-01-2024
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(name: str, head: Optional[ListNode]):
    """prints a linked list"""
    print(f"{name}: [", end="")
    while head:
        if head.next is None:
            print(f"{head.val}]")
        else:
            print(f"{head.val}, ", end="")
        head = head.next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """adds two numbers in a linked list"""
    remainder = 0
    # temporary placeholder for the newest created node
    ltemp = None
    # head of returned linked list
    head = None
    while (l1 or l2):
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        res = val1 + val2 + remainder

        if (res > 9):
            remainder = (res - (res % 10)) // 10
            res = res % 10
        else:
            remainder = 0
        new = ListNode(res)
        if (ltemp):
            ltemp.next = new
        else:
            head = new
        ltemp = new
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if (remainder != 0):
        new = ListNode(remainder)
        ltemp.next = new
    return head


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    printList("l1", l1)
    printList("l2", l2)
    printList("lresult", addTwoNumbers(l1, l2))
    print()
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    printList("l1", l1)
    printList("l2", l2)
    printList("lresult", addTwoNumbers(l1, l2))

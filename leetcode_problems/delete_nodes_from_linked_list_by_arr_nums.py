from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: list[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        remove_set = set(nums)

        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val in remove_set:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next


head = ListNode(2)
head.next = ListNode(10)
head.next.next = ListNode(9)


def print_list(head) -> list:
    """Helper function to print the linked list."""
    arr = []
    current = head  # Use a separate pointer to avoid modifying the original list
    while current:
        arr.append(current.val)
        current = current.next
    return arr


print(print_list(Solution().modifiedList([9, 2, 5], head)))  # Output should be: [10]

class ListNode:
    """Simple linked list node."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def find_length(head: ListNode):
    """
    Find the length of a linked list.
    Time Complexity: O(n), Space Complexity: O(1)
    """
    # Approach 1:
    # arr = []
    # while head:
    #     arr.append(head)
    #     head = head.next
    # return len(arr)
    # Approach 2:
    count = 0
   
    while head:
        count += 1
        head = head.next
    return count

# write your code here


# Test the function# Create linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(7)

# print(head.next)
# print(head)
print(f"Length of linked list: {find_length(head)}")  # Output: 4

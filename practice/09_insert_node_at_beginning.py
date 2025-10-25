class ListNode:
    """Simple linked list node."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert_at_beginning(head, val):
    added = ListNode(val)
    added.next = head
    return added


def print_list(head):
    """Helper function to print the linked list."""
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


# Test the function# Original list: 2 -> 3 -> 4 -> None
head = ListNode(2)
head.next = ListNode(3)
head.next.next = ListNode(4)

print(f"Original list: {print_list(head)}")
head = insert_at_beginning(head, 1)
# print(head)
print(f"After inserting 1: {print_list(head)}")

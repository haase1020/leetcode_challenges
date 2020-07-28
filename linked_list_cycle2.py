# instructions:
# Given a linked list, return the node where the cycle begins.
# If there is no cycle, return null.

# To represent a cycle in the given linked list,
# we use an integer pos which represents the position (0-indexed) in the
# linked list where tail connects to. If pos is -1, then there is no cycle
# in the linked list.

# Note: Do not modify the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None

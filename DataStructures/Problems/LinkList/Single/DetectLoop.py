from DataStructures.Core.LinkList.Single import LinkedList, Node

"""
Leet code: https://leetcode.com/problems/linked-list-cycle/
Given a linked list, check if the linked list has loop or not. Below diagram shows a linked list with a loop. 
"""


def detectLoopwithHash(head: Node) -> bool:
    """
    Complexity Analysis:
        - Time complexity: O(n).
        Only one traversal of the loop is needed.
        - Auxiliary Space: O(n).
        n is the space required to store the value in hashmap.
    :param head: Node
    :return: boolean
    """
    s = set()
    temp = head
    while temp:
        if temp in s:
            return True
        temp = temp.next
        s.add(temp)
    return False


class NodeWithFlag(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.flag = 0


def detectLoopWithFlag(head: NodeWithFlag) -> bool:
    """
    Complexity Analysis:
        - Time complexity:O(n).
        Only one traversal of the loop is needed.
        - Auxiliary Space:O(1).
        No extra space is needed.
    :param head: Node
    :return: boolean
    """
    temp = head
    while temp:
        if temp.flag == 1:
            return True
        temp.flag = 1
        temp = temp.next
    return False


def detectLoopWithFloyCycle(head: Node) -> bool:
    """
    Complexity Analysis:
        -Time complexity: O(n).
        Only one traversal of the loop is needed.
        -Auxiliary Space:O(1).
        There is no space required.
    :param head: Node
    :return: boolean
    """
    slow = head
    fast = head
    while (slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    # Driver program for testing
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)

    # Create a loop for testing
    llist.head.next.next.next.next = llist.head

    if (detectLoopWithFloyCycle(llist.head)):
        print("Loop found")
    else:
        print("No Loop ")

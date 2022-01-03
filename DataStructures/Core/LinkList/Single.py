"""
Advantages over arrays
    1) Dynamic size
    2) Ease of insertion/deletion

Drawbacks:
    1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do
        binary search with linked lists efficiently with its default implementation. Read about it here.
    2) Extra memory space for a pointer is required with each element of the list.
    3) Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there
        in case of linked lists.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAfter(self, prev_node: Node, data) -> None:
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node

    def append(self, data) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def deleteNode(self, key) -> None:
        temp = self.head
        if temp:
            if temp.data == key:
                self.head = None
                return
        prev = self.head
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def deleteNodeWithPosition(self, position) -> None:
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        current = None

    def getCount(self) -> int:
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, key) -> bool:
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def getNth(self, index):
        # Time complexity: O(n)
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp.data
            temp = temp.next
            count += 1
        return 0


if __name__ == '__main__':
    llist = LinkedList()

    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    n = 3
    print("Element at index 3 is :", llist.getNth(n))
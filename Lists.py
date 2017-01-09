class LinkedList:
    """ Custom Linked List class"""
    val = "x"
    next = None

    def __init__(self, val):
        self.val = val


def printLinkedList(head):
    item = head
    while item is not None:
        print(item.val)
        item = item.next

def removeNth(head , ind):
    if ind == 0:
        return head.next

    prev = head
    item = head.next
    i = 1
    while item is not None:
        if i == ind:
            prev.next = item.next
            break
        i = i + 1
        prev = item
        item = item.next
    return head
        

A = LinkedList("A")
B = LinkedList("B")
C = LinkedList("C")
D = LinkedList("D")
E = LinkedList("E")
F = LinkedList("F")

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F


printLinkedList(A)
print("---")
HEAD = removeNth(A,1)
printLinkedList(HEAD)
print("---")

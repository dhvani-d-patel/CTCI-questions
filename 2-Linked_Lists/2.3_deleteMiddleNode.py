class Node:
    def __init__(self, d):
        self.next = None
        self.val = d

class Solution:

    def deleteMiddleNode(self,node):
        node.val = node.next.val
        node.next = node.next.next


def print_list(l):
    if not l:
        return "[]"
    result = ""

    while l.next:
        result += str(l.val) + " -> "
        l = l.next
    result += str(l.val)
    print(result)

def main():
    l = [4,5,1,9]
    head = Node(-1)
    ptr = head
    for x in l:
        ptr.next = Node(x)
        ptr = ptr.next
    head = head.next
    print("Question:")
    print_list(head)
    print("")
    print("Solution:")
    Solution().deleteMiddleNode(head.next)
    print_list(head)


if  __name__ == '__main__':
    main()
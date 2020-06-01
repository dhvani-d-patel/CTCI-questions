class Node:
    def __init__(self, d):
        self.next = None
        self.val = d

class Solution:

    def reveseLinkedList(self,head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


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
    l = [1,2,3,4,5]
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
    ans = Solution().reveseLinkedList(head)
    print_list(ans)


if  __name__ == '__main__':
    main()
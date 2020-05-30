class Node:
    def __init__(self, d):
        self.next = None
        self.val = d

class Solution:

    def partitionList(self,head, x):

        # # Not maintaining order
        # curr = head
        #
        # while curr:
        #     if curr.val >= x:
        #         forward = curr.next
        #         while forward:
        #             if forward.val < x:
        #                 temp = curr.val
        #                 curr.val = forward.val
        #                 forward.val = temp
        #                 break
        #             forward = forward.next
        #     curr = curr.next
        # return head

        # # Maintaining order and doing in place
        # curr = Node(-1)
        # curr.next = head
        # head = curr
        # while curr.next:
        #     if curr.next.val >= x:
        #         forward = curr.next
        #         while forward.next:
        #             if forward.next.val < x:
        #                 temp = curr.next
        #                 curr.next = Node(forward.next.val)
        #                 curr.next.next = temp
        #                 forward.next = forward.next.next
        #                 break
        #
        #             forward = forward.next
        #
        #     curr = curr.next
        # return head.next


        # Maintaining order and using additional space
        forward_ref = forward = Node(-1)
        backward_ref = backward = Node(-1)

        while head:
            if head.val < x:
                forward.next = Node(head.val)
                forward = forward.next
            else:
                backward.next = Node(head.val)
                backward = backward.next
            head = head.next

        forward.next = backward_ref.next
        return forward_ref.next



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
    l = [1,4,3,2,5,2]
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
    ans = Solution().partitionList(head,3)
    print_list(ans)


if  __name__ == '__main__':
    main()
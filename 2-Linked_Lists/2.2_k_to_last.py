class Node:
    def __init__(self, d):
        self.val = d
        self.next = None

class Solution:

    def kth_to_last(self, head, k):

        # # Find list size and then find the n-kth element
        # curr = head
        # size = 0
        # while curr:
        #     size += 1
        #     curr = curr.next
        #
        # k = size - k
        # for i in range(k):
        #     head = head.next
        # return head

        # Recursive - Backtracking
        if not head:
            return False, None, 0
        flag, curr, pos = self.kth_to_last(head.next, k)
        pos = pos + 1
        if not flag:
            if pos == k:
                return True, head, float("-inf")
            else:
                return False, None, pos
        else:
            return flag, curr, pos


        # Iterative using 2 pointer
        # if not head:
        #     return head
        #
        # curr = head
        # forward = head
        #
        # for i in range(k):
        #     forward = forward.next
        #
        # while forward:
        #     curr = curr.next
        #     forward = forward.next
        #
        # return curr


def print_list(l):
    if not l:
        return "[]"
    result = ""

    while l.next:
        result += str(l.val) + " -> "
        l = l.next
    result += str(l.val)
    print(result)

if __name__ == '__main__':
    l = [1,2,3,4,5]
    head = Node(-1)
    ptr = head
    for x in l:
        ptr.next = Node(x)
        ptr = ptr.next
    print("Question:")
    print_list(head.next)
    print("")
    print("Solution:")
    ans = Solution().kth_to_last(head.next, 2)
    print_list(ans[1])
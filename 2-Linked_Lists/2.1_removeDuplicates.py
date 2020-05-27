class Node:
    def __init__(self, d):
        self.next = None
        self.val = d

class Solution:

    def removeDuplicates(self,head):

        ############### Hash Set O(N) ##################
        if not head:
            return head
        curr = head
        hash_set = set()
        hash_set.add(head.val)
        while curr.next:
            if curr.next.val not in hash_set:
                hash_set.add(curr.next.val)
                curr = curr.next
            else:
                curr.next = curr.next.next

        return head


        ############# No additional space O(N^2) ##################
        # if not head:
        #     return head
        # curr = head
        #
        # while curr:
        #     runner = curr
        #     while runner.next:
        #         if runner.next.val == curr.val:
        #             runner.next = runner.next.next
        #         else:
        #             runner = runner.next
        #     curr = curr.next
        # return head

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
    l = [10,1,15,1,10,2,1,6]
    head = Node(-1)
    ptr = head
    for x in l:
        ptr.next = Node(x)
        ptr = ptr.next
    print("Question:")
    print_list(head.next)
    print("")
    print("Solution:")
    ans = Solution().removeDuplicates(head.next)
    print_list(ans)


if  __name__ == '__main__':
    main()
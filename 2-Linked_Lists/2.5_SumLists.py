class Node:
    def __init__(self, d):
        self.next = None
        self.val = d

class Solution:

    def sumLists(self,l1,l2):

        # # Iteration
        # head = ans = Node(-1)
        #
        # carry = 0
        # while l1 or l2:
        #     if l1:
        #         x = l1.val
        #         l1 = l1.next
        #     else:
        #         x = 0
        #
        #     if l2:
        #         y = l2.val
        #         l2 = l2.next
        #     else:
        #         y = 0
        #
        #     sum = x + y + carry
        #     carry = sum//10
        #     sum = sum%10
        #     ans.next = Node(sum)
        #     ans = ans.next
        #
        # if carry:
        #     ans.next = Node(carry)
        # return head.next

        # Recursion

        def helper(l1,l2,carry,ans):
            if not l1 and not l2 and not carry:
                return
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum//10
            sum = sum%10
            ans.next = Node(sum)
            ans = ans.next

            helper(l1,l2,carry,ans)

        ans = head = Node(-1)
        helper(l1,l2,0,ans)
        return head.next



def print_list(l):
    if not l:
        return "[]"
    result = ""

    while l.next:
        result += str(l.val) + " -> "
        l = l.next
    result += str(l.val)
    return result

def main():
    l1 = [9,7,8]
    list_1 = Node(-1)
    ptr1 = list_1
    for x in l1:
        ptr1.next = Node(x)
        ptr1 = ptr1.next
    list_1 = list_1.next

    l2 = [6,8,5]
    list_2 = Node(-1)
    ptr2 = list_2
    for x in l2:
        ptr2.next = Node(x)
        ptr2 = ptr2.next
    list_2 = list_2.next

    print("Question:")
    print(print_list(list_1) + "   +   " + print_list(list_2))
    print("")
    print("Solution:")
    ans = Solution().sumLists(list_1,list_2)
    print(print_list(ans))


if  __name__ == '__main__':
    main()
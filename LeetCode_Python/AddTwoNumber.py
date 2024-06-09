# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        new_list = ListNode()
        current = new_list
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            current.val = sum % 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or carry:
                current.next = ListNode()
                current = current.next
        return new_list

        # new_list = ListNode()
        # head_node = new_list
        # carry = 0
        # while l1 and l2:
        #     if l1.val + l2.val + carry > 9:
        #         new_list.val = (l1.val + l2.val + carry)%10
        #         carry = 1
        #     else:
        #         new_list.val = l1.val + l2.val + carry
        #         carry = 0
        #     l1 = l1.next
        #     l2 = l2.next
        #     if l1 or l2:
        #         next_node = ListNode()
        #         new_list.next = next_node
        #         new_list = new_list.next

        # while l1:
        #     if l1.val + carry > 9:
        #         new_list.val = (l1.val + carry)%10
        #         carry = 1
        #     else:
        #         new_list.val = l1.val + carry
        #         carry = 0
        #     l1 = l1.next
        #     if l1:
        #         next_node = ListNode()
        #         new_list.next = next_node
        #         new_list = new_list.next

        # while l2:
        #     if l2.val + carry > 9:
        #         new_list.val = (l2.val + carry)%10
        #         carry = 1
        #     else:
        #         new_list.val = l2.val + carry
        #         carry = 0
        #     l2 = l2.next
        #     if l2:
        #         next_node = ListNode()
        #         new_list.next = next_node
        #         new_list = new_list.next
        # if carry == 1:
        #     new_list.next = ListNode(carry)

        
        # return head_node




class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        new_node = node(0)
        temp = new_node
        total_sum = 0in
        carry = 0
        while l1 or l2 or carry:
            if l1.data is not None:
                total_sum += l1.data
            if l2.data is not None:
                total_sum += l2.data
            total_sum += carry
            temp.next = new_node(total_sum % 10)
            carry = total_sum // 10
            temp = temp.next
            total_sum = 0
        return new_node.next








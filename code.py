class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        while start.next:
            if start.next.val == val:
                start.next = start.next.next
            else:
                start = start.next         
        return dummy.next   

        '''
        When traverse, always look at the next element in list, because if we already at element with value equal to val, we can not delete it, we need to go back somehow.
Use dummy head to deal with case when head is equal to val.
So, basically our algorithm looks like this: we traverse our list and if value of next element is equal to val, we need to delete it, so we do start.next = start.next.next. Note, that in this case we do not move our pointers, because there can be more element equal to val. If value is not equal to val, we move to the next element.

Complexity: time complexity is O(n) with only one pass, space complexity is O(1), because we do not use any additional memory except couple of variable.
'''


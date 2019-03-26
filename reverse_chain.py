#翻转链表：注意细节：在修改指针时可能会出现节点断开，导致分成两个单链表，所以需要设置三个指针来完成交换任务：12345->54321
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(ListNode):
    def reverse_list(self,phead):
        if not phead:
            return False
        pre_node=None
        p_node=phead
        p_reverse_head=None
        while p_node is not None:
            p_next=p_node.next
            if p_next is None:
                p_reverse_head = p_node
            #交换位置
            p_node.next=pre_node
            pre_node=p_node
            p_node=p_next
        return p_reverse_head
#测试用例：（1）phead为空，直接不存在链表（2）链表中只有一个节点（3）链表中有多个节点
                
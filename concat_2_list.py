#有两个增序的单链表，将两个单链表合并成一个增序的链表：测试用例：（1）两个链表均为空链表（2）其中一个链表若为空，则输出另一个单链表
#（3）两个都不为空时，进行比较
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(ListNode):
    def Merge(self,phead1,phead2):
        if not (phead1 and phead2):
            return None
        if  not phead1:
            return phead2
        if not phead2:
            return phead1
        p_merge_head=None
        if phead1.val < phead2.val:
            p_merge_head=phead1
            p_merge_head.next = Merge(phead1.next,phead2)
        else:
            p_merge_head=phead2
            p_merge_head.next = Merge(phead1,phead2.next)
        return p_merge_head



'''
#求解链表中的倒数第k个值，首先需要判断三个边界条件：（1）如果是空指针（2）如果k=0（3）如果链表长度小于k.解法就是先让第一个
#节点走k-1步，然后第二个节点和第一个一起前进，当地一个节点到达尾节点时，第二个节点正好到达倒数第k个节点
#c++版：
struct ListNode{
    int m_nvalue;
    ListNode *next;

}
ListNode* find_last_k(ListNode *p_head,unsigned int k){
    if(p_head==nullptr || k<=0){
        return nullptr;
    }
    ListNode *p_start = p_head;
    ListNode *p_end = nullptr;
    for(int i=0;i<k-1;++i){
        if(p_start->next!==nullptr){
            p_start=p_start->next;
        }
        else{
            return nullptr;
        }
    }
    p_end=P_head;
    while(p_head->next!=nullptr){
        p_head=p_head->next;
        p_end=p_end->next;
    }
    return p_end;
}
'''
#python 版
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(ListNode):
    def last_k_node(self,pListnode,k):
        if not pListnode or k==0:
            return False
        p_head=pListnode
        p_end=None
        #先让第一个先走k-1步
        for i in range(k-1):
            if p_head.next is not None:
                p_head=p_head.next
            else:
                return False
       #此时后一个节点开始出发，前一个停止时，刚好后一个处在倒数第K个上
        p_end=pListnode
        while p_head.next is not None:
            p_head=p_head.next
            p_end=p_end.next
        return p_end


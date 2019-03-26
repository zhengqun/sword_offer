#找出环中的节点入口，首先设定两个指针，先让第一个指针走两步，然后慢的指针走一步，直到两个指针重合时，那么有环存在，然后再判定环中节点的个数
#再设置两个指针找出入口在哪：前指针先走环中节点的个数步，当前后两个指针相遇时既是入口点
'''
ListNode *meetNode(ListNode *phead){
    if (phead == nullptr){
        return nullptr;

    }
    #慢的走一步
    ListNode *p_slow=phead->m_next;
    if(p_slow == nullptr){
        return nullptr;
    }
    #快的走两步
    ListNode *p_fast=phead->m_next->m_next;
    while(p_fast!=nullptr &&p_slow!=nullptr){
        if(p_fast==p_slow){

            return p_fast;
}
        if(p_fast!=p_slow){

            p_fast=p_fast->m_next;
            p_slow=p_slow->m_next;
}
        if(p_fast!=nullptr){

            p_fast=p_fast->m_next;
}
}
}
#先找出列表中的环中节点的个数
ListNode *entrance_node(ListNode *phead){
    ListNode *meetnode=meetNode(phead);
    if(meetnode == nullptr){
        return nullptr;
}
    ListNode *p_node1=meetnode;
    int count=1;
    while(p_node1->m_next!=nullptr){
        p_node1=p_node1->m_next;
        count+=1;
}
    p_node1=p_head;
    for(int i=0;i<count;++i){
        p_node1=p_node1->m_next;
    }
    ListNode *p_node2=phead;
    if(p_node2!=nullptr){
        p_node2=p_node2->m_next;
    }
    while(p_node2!=p_node1){
        p_node2=p_node2->m_next;
        p_node1=p_node->next;
}
return p_node1;
}
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(ListNode):
    def meet_Node(self,phead):
        if not phead:
            return False
        p_slow=phead.next
        if not p_slow:
            return False
        p_fast=p_slow.next
        while p_fast is not None and p_slow is not None:
            if p_slow ==p_fast:
                return p_fast
            p_fast=p_fast.next
            p_slow=p_slow.next
            if p_fast is not None:
                p_fast=p_fast.next
        return None
    def entrance_Node(self,phead):
        meet_node=self.meet_Node(phead)
        if not meet_node:
            return  False
        p_node1=meet_node
        count=1
        while p_node1.next is not None:
            p_node1=p_node1.next
            count+=1
        p_node2=phead
        for i in range(count):
            p_node1=p_node1.next
        while p_node1 != p_node2:
            p_node1=p_node1.next
            p_node2=p_node2.next
        return p_node1


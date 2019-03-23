#删除链表中的重复节点：思想很简单，因为是排序好的链表所以，只需要遍历链表，查找多少个重复的链表值即可
#c++版:注意链表头结点的申请：ListNode  **phead
'''
void deleteNodeDulplication(ListNode **phead){
    if (phead==nullptr || *phead==nullptr){
        return;
    }
    ListNode *Pre_node = nullptr;
    ListNode *pnode=*phead;
    bool delete_node=false;
    while (pnode !==nullptr){
        ListNode *pnext=pnode->m_next;
        if(pnext != nullptr && pnext->m_nvalue=pnode->m_nvalue){
            deletenode =true;
        }
        if(!deletenode){
            ListNode *pre_node = pnode;
            pnode = pnode->m_next;
        }
        else{
            int value=pnode->m_nvalue;
            ListNode *p_delete_node =pnode;
            if(p_delete_node !==nullptr && p_delete_node->m_next !==nullptr && p_delete_node==value){
                pnext=pnode->m_next
                pnode->m_nvalue=pnext->m_nvalue;
                pnode->m_next=pnext->next;
                delete p_delete_node->next;
            }

        if(pre_node ==nullptr){
            *phead=pnode;
        }
        else
            pre_node->next=pnode;
        }
    }
}
'''
#python版双指针，单指针也可以实现：
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class delete_dulplicate_node(ListNode):
    def p_delete_node(self, p_head):
        if not p_head:
            return False
        p = p_head
        q = p_head.next
        while q:
            if q.val==p.val:
                p.next = q.next
                q = p.next
            else:
                p = p.next
                q = q.next
        return p_head



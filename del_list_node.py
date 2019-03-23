#删除链表中的节点，需要o（1）的时间，需要考虑此节点是不是头结点，或者是不是尾节点
'''
void Delete_Node(ListNode *p_head,ListNode *pDeleteNode){
    if (p_head==nullptr || pDeleteNode==||nullptr){
        return
    }
    #删除的不是尾节点
    if(pDeleteNode->m_next!=nullptr){
        #删除某个节点，把该节点的下一个节点值赋值给改删除节点，删除该节点的下个节点
        ListNode*p_next_node=pDeleteNode->m_next
        pDeleteNode->m_value=p_next_node->m_value
        pDeleteNode->m_next=p_next_node->m_next
        delete p_next_node
        p_next_node=nullptr
    }

    #删除的是头结点
    elseif(pDeleteNode == p_head){
        delete p_head
        pDeleteNode=nullptr;
        *p_head=nullptr
    }
    #删除的节点是尾节点，遍历所有节点
    else{
        ListNode*p_next=p_head
        if(p_next->m_next!=pDeleteNode){
            p_next=p_next->m_next
        }
        p_next->m_next=nullptr;
        delete pDeleteNode
        pDeleteNode=nullptr;
}
}
'''
#python版
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Del_node:
    def Del_Node(self,p_head,node):
        #以下三种情况讨论：删除节点为队列头节点，或者中间节点，或者尾节点
        if not node:
            return False
        #删除节点的下一个节点值赋值给删除节点，把删除节点的下一个节点的写一个节点指针赋值给删除节点
        elif node.next is not None:
            node.val=node.next.val
            node.next=node.next.next
            del_val=node.next.val
            return del_val
        #删除节点在队头,并且是只有一个节点的链表
        elif p_head == node:
            if p_head.next is not None:
                p_head.next = None
                p_head.val = None
                del_val = p_head.val
            return del_val

        #删除队尾节点
        else:
            if node.next is None:
                node.next =None
                node.val=None
                del_val = node.val
            return del_val













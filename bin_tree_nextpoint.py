#(1)寻找二叉树的下一个节点：给定任意一个二叉树节点，首先判断该节点是否存在右子树节点，如果存在右子树节点，那么判断是否存在左子树
#节点，如果存在左子树节点那么根据前序遍历的第一个节点即为中序遍历的下一个节点。（2）如果不存在右子树节点，如果存在左子树节点，那么
#他的下一个节点将指向他的父节点，情形比较复杂。
#给定节点指针为：pNode
#写的太乱了，懂思想吧。就是画个图看看父节点右子树节点是否存在且右子树的左子树节点是否存在
class Find_Bintree_Nextpoint:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        self.next = None #指向父节点

class Deal_Fun:
    def Fun_Deal(self,pNode):
        if not pNode :
            return
        #设置目标节点的指针
        pnext= None
        #判断给定节点是否存在右子树节点
        while (pNode and pNode.right):
            pNode=pNode.right
            if pNode.left:
                pNode=pNode.left
            pnext=pNode
        while pNode.next == nullptr and (pNode.right != None):
            pNode=pNode.right
            if pNode.right:
                pNode=pNode.left
                pnext=pNode
            else:
                pnext=pNode.right

        if pNode.next != nullptr: #父节点存在
                pNode=pNode.next #指向父节点
            pnext=pNode

        return pnext #返回父指针








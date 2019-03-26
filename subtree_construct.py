#有两颗二叉树，A，B，判断B是不是A的子结构，思想很简单就是初始化指向两棵树根节点的指针，然后遍历主树，与子树比较，如果相匹配
#则可以说B是A的子结构。否则return false。边界条件：（1）AB为空树（2）
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(TreeNode):
    def Subtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                result = self.HasSubtree(pRoot1,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.right,pRoot2)
        return result
    def HasSubtree(self,pRoot1,pRoot2):
        if not pRoot1:
            return False
        if not pRoot2:
            return True
        if pRoot1.val != pRoot2.val:
            return False
        return self.HasSubtree(pRoot1.left,pRoot2.left) and self.HasSubtree(pRoot1.right,pRoot2.right)




#重建二叉树
class build_Tree:
    def rebuild_tree(self,x):
        self.val = x
        self.left = None
        self.right = None

class Build_Tree_Fun:
    def fun_build_tree(self,preorder,inorder):
        if not preorder and not inorder:
            return None
        root_value = build_Tree(preorder[0])
        if set(preorder) != set(inorder):
            return None
        # 把根节点的下标值设置为i
        i = inorder.index(preorder[0])

        #前序遍历的下标值从1->i+1,设置为左子树，中序遍历的下标值从0->i，根节点设置为左子树
        root_value.left=self.fun_build_tree(preorder[1:i],inorder[:i])

        #前序遍历的右子树：下标值从i+1->结束设置为右子树的值，中序遍历的值从下标：i+1->结束
        root_value.right=self.fun_build_tree(preorder[i+1:],inorder[i+1:])
        return root_value
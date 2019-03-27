'''
#广度优先遍历：按层打印
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(TreeNode):
    def up_bottom_print(self, root):
        if root is None:
            return False
        queue=[]
        result=[]
        queue.append(root)
        while len(queue) > 0:
            current_root=queue.pop(0)
            result.append(current_root.val)
            if current_root.left:
                queue.append(current_root.left)
            if current_root.right:
                queue.append(current_root.right)
        return result
#(1)在不改变链表指针格式的条件下，只能先遍历整个链表的值，将这些值存放在栈中，利用栈的优点后进先出，所以性能比较好
#(2)使用Python的insert函数，list.insert(index,value)
#(3)实现方法三：使用递归（略，效率不高）
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class use_insert_fun:
    def end_start_print(self,listNode):
        if listNode == None:
            return []
        #接收传入的值
        result=[]
        while listNode:
            result.insert(0,listNode.val)  #使用insert函数下标为0，可以实现链表中的值反转，每次的值都排在第一个位置上
            listNode = listNode.next
        return result


#实现方法一：
class Listnode1:
    def __init__(self,x):
        self.val = x
        self.next=None
class Solution_fun:
    def end_start_list(self,listnode):
        if not listnode:
            return []
        #使用栈结构接收值
        stack =[]
        while listnode:
            stack.append(listnode.val)   #入栈操作
            listnode = listnode.next
        result = []
        result = stack.pop()    # 出栈操作
        return result










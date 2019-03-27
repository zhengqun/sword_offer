'''
#实现一个min函数：使得可以求出栈中最小元素。思路就是：首先要设置两个空栈，第一个存放压栈的数值，第二个作为辅助栈存放第一个栈中，相对较小的值
#如：第一个栈         第二个栈
       3               3
       3 4             3 3
       3 4 5           3 3 3
       3 4 5 1         3 3 3 1
#每次压入辅助栈的都是最小元素，要比辅助栈的top元素小的,否则拷贝一次顶栈元素，再压入栈中
'''
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self,value):
        self.stack.append(value)   #压入原栈中，判断该值和min_stack.top()的大小，小的话压栈，大的话,min_stack重新拷贝栈顶元素再压栈
        if self.min_stack == [] or value < self.min_stack.top():
            self.min_stack.append(value)
        #否则压入的还是它自己
        else:
            self.min_stack.append(self.min_stack.top())
    def pop(self):
        if self.stack == [] or self.min_stack ==[]:
            return None
        self.min_stack.pop()
        self.stack.pop()

    def top(self):
        if self.min_stack is not None and self.stack is not None:
            return self.min_stack[-1]

#思想很简单：就是考察栈和队列的特点，一个先进后出，另一个先进先出，使用两个栈正好可以实现先进先出，输出结果与队列输出结果一致
#同理也可以两个队列实现一个栈的操作
class Stack_2_Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self,x):
        self.stack1.append(x)

    def pop(self):
        result=[]
        if len(self.stack1)==0:
            return
        elif len(self.stack1)>0 and len(self.stack2)==0:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
        result=self.stack2.pop()
        return result

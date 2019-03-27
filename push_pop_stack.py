#考察栈的压入和弹出操作，与考研数据结构中栈的出栈有多少种可能性相关
class Solution:
    def is_pop_seq(self,pushV,popV):
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        else:
            return True
'''
#c++版比较复杂
bool ispopRecord(const int *p_push,const int *p_pop,int length){
    bool b_possible =false;
    if (p_push != nullptr && p_pop !=nullptr && length >0){
        const int *p_next_push=p_push;
        const int *p_next_pop=p_pop;
        std::stack<int>stackData;
        while(p_next_pop-p_pop<length){
                while(stackData.empty()||stackData.top()!==*p_next_pop){
                    if(p_next_push-p_push==length){
                        break;
                    }
                    stackData.push(*p_next_push);
                    p_next_push++;
                }
                if(stackData.top()!= *p_next_pop){
                    break;
                }
                stackdata.pop();
                p_next_pop++;
        }
            if(stackData.empty()&&p_next_pop-p_pop==length){
                b_posssinle=true;
            }
    }
    return b_possile;
}
'''


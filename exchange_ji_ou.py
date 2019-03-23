#交换数组中的奇数和偶数，使得数组的前半部分为奇数，后半部分为偶数，可以使用双指针，pbegin和pend.改编：移动奇数到偶数前面，或者按大小排列
'''
void change_odd_even(int *p_data,unsigned int length,(*func)(int)){
    if(p_data==nullptr ||length<=0){
        return;
    }
    #定义两个指向开头和结尾的指针
    int *p_begin=p_data;
    int *p_end=p_data+length-1;
    while(p_begin<p_end){#从前往后找偶数
        while(p_begin < p_end && !func(p_begin)){
            p_begin++;
        }
        #从后往前找奇数
        while(p_begin<p_end && func(*p_end)){
            p_end --;
        }
    if（p_begin <p_end）{
        int temp =*p_begin;
        *p_begin=*p_end;
        *p_end=temp;
    }
    }
}
#判断是偶数
bool isEven(int n ){
    return (n&1)==0;
}
void change_fun(int *p_data,unsigned int length){
    change_odd_even(p_data,length,isEven);
}
'''
#Python版
class change_odd_even:
    def change_fun(self,array):
        return sorted(array,key=lambda c:c%2,reverse=True)

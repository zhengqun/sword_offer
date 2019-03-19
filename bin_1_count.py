#本题考查位运算，一定要注意区分是正数还是负数：0100|0000：正数 1001|0000:负数
#可以左右移动，判断最低位是否为1，注意当是负数时，右移动可能会陷入死循环，因为每右移动一次，左边的最高位改为1，最终会导致陷入死循环：0XFFFFFFF....
#c++实现左移动
'''
int count_one(int number){
    int count=0;
    unsigned int flag=1;
    while(flag){
        if(number &flag){
            count++;
            flag=flag<<1   #经典：左移一位01->10，进行位位相乘，是1的还是1，不是1的变成0
        }
    }
    return count;
}
'''
'''
#面试官惊喜的算法:一个整数减1，其实就是这个整数的二进制数的最右边的1变成0，如果最右边的1后面还有0则0取反：0->1，然后将得到的
二进制数和原数做位与运算，即可得知里面1的个数：1100-1=1011 ---> 1100 * 1011=1000 ->1000-1=0111->1000*0111=0000,因此就可以
计算出为2个0
int count_1(int n){
    int count=0;
    while(n){
        ++count;
        n=(n-1)&n;
    }
    return count;
}

'''
#python版
class Solution:
    def Count_One(self,n):
        count =0
        if n<=0:
            return False
        while n:
            count+=1
            n=(n-1)&n
        return count


#该问题是典型的动态规划问题，使剪短的绳子的乘积最大值，求每小段的最优解累乘就可以得到最优解
#两种解法：动态规划+贪婪地解法（当绳子长度>=5时，剪成3或2的，n<5时剪成2的结果比3大）
#数学公式:2*(n-2) 与 3*(n-3)的大小（条件：n>=5||n<5）
#c++动态算法实现
'''
int max_length(int length){
    if(length<2){
        return 0 ;  #绳子长度为1，只能为一段
    }
    if(length==2){
        return 1;
    }
    if(length==3){
        return 2;
    }
    #声明一个数组接收剪短的长度：result[],尽量剪成长度为3的段
    int * result=new int[length+1];
    result[0]=0；
    result[1]=1；
    result[2]=2；
    result[3]=3；
    int max =0；
    for (int i=4;i<=length;++i){
        for (int j =1;j<=i/2;++j){
            get_result=result[j]*result[i-j]；  #收集乘积的最大值
            if (get_result> max){
                max=get_result；
            }
            result[i] = max
        }
    }
    max=result[length];
    delete[] result;
    return max;
}
'''

'''
#贪婪算法实现
int find_optimize(int length){
    if (length<2){
        return 0;
    }
    if(length==2){
        return 1;
    }
    if(length ==3){
        return 2;
    }
    #尽可能剪去长度为3的绳子
    int three_length =length/3;
    #如果剩余绳子长度为4时，不能再剪去长度为3的长度，需要改成长度为2的长度
    if（length-three_length*3==1）{
        three_length-=1;
    }
    int two_length=（length-three_length*3）/2;
    return (int)(pow(3,three_length))*(int)(pow(2,two_length));#长度为三的所有长度*长度为2的所有段数
}

'''
#python版
class Fun_Solution:
    def Find_Max_Value(self,length):
        if length < 2:
            return 0
        if length ==2:
            return 1
        if length ==3:
            return 2
        result={}
        result[1]=1
        result[2]=2
        result[3]=3
        max_multi_result=[]
        for i in range(4,length+1):
            for j in range(1,int(i//2)+1):
                max =0
                temp=result[j]*result[i-j]
                if temp>max:
                    max=temp
                max_multi_result.append(max)
        return max_multi_result[-1]  #数组中最后一个值即为最大乘积

'''
#或者80行之后改成：
                result[i]=max
        max=result[length]
        return max
'''




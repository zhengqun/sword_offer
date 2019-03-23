#本题目求解基数的整数次方，不需要考虑大数，但需要考虑指数是0，负数，<0的情况
#c++版：
'''
#可以满足要求的写法
bool get_invalid_input=false;
double get_result(double base,int exponent){
    get_invalid_input=false;
    if(equal(base,0.0)&&exponent<0){
        get_invalid_input=true;
        return 0.0
    }
    unsigned int absExponent=(unsigned int)(exponent);
    if(exponent<0){
        absExponent=(unsigned int)(-exponent);
    }
    double pow_result=computing_fun(base,absExponent);
    if(exponent<0){
        pow_result=1 / pow_result;
        return pow_result;
    }
}
double computing_fun(double base,unsigned int exponent){
    default pow_result=1.0;
    for (int i =i;i<=exponent;++i){
        pow_result*=base;
    }
    return pow_result;
}
'''
'''
#比较牛的写法：代替computing_fun(),并且采用了位运算代替乘除法
数学公式：a^n={
                a^(n/2)*a^(n/2)   n为偶数
                a^(n-1)/2*a^(n-1)/2*a  n为奇数
}
double computing_fun(double base,unsigned int exponent){
    if(exponent ==0){
        return 1;
    }
    if(exponent==1){
        return base;
    }
    #采用位运算符判断是奇数偶数
    double pow_result=computing_fun(base,exponent>>1);
    pow_result*=pow_result;  #判断偶数
    if(exponent & 0x1 ==1){#判断奇数
        pow_result*=base;
    }
    return pow_result;
}
'''
#python 版
class solution_fun:
    def get_value(self,base,exponent):
        try:
            result = pow_val(base,abs(exponent))
            if exponent<0:
                result=1.0/result
        except ZeroDivisionError:
            print("invalid_input_base")
        else:
            return result
    def pow_val(self,base,exponent):
        if exponent==0:
            return 1
        elif exponent==1
            return base
        result = pow_val(base,exponent>>1)  #判断奇数偶数
        result*=result
        if exponent & 1==1:
            result*=base
        return result


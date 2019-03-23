#思路：判断字符串是否表示数值：比如：'123.45e+6'：123：整数，45：小数部分，+6：指数部分，从头到尾扫描一遍
'''
#c++版
bool is_number(const char *str){
    if(str==nullptr){
        return false;
    }
    #判断整数部分
    bool numeric=scan_integer(&str);
    #判断小数部分
    if(*str=='.'){
        ++str;    #指向小数部分的下一个位置
        numeric= scanUnsignedinteger(&str)||numeric;   #小数点后面可以是：（1）.123（2）233.（3）233.66
    }
    #判断指数部分
    if(*str==e ||*str==E){
        ++str;
        numeric=numeric && scan_integer(&str); #判断e/E前后面有无数字，没有则不能表示
    }
    return numeric && *str=='\0';
}

bool scanUnsignedinteger(const char **str){
    const char *before= *str;
    while(**str!='\0'&& **str>='0' && **str<='9'){
        ++(*str);
    return *str > before;
    }
}
bool scan_integer(const char **str){
    if(**str=='+'||**str=='-'){
        ++(*str);
    }
    return scanUnsignedinteger(str);
}
'''
#python版：需要判断小数点，符号，e的出现位置。小数点智能出现一次，且必须前面必须是数字。符号可出现两次，但是第二次必须前面是e/E
。e/E出现的位置必须只能出现一次，而且不能出现在字符串的最后一位，后面需要接数字
class Solution:
    def isnumeric(self,s):
        if len(s)<0:
            return False
        has_sign=False
        has_point=False
        has_e=False
        for i in range(len(s)):
            if s[i]=='e'or s[i]=='E':
                if has_e:   #不能同时出现两个e/E
                    return False
                else:
                    has_e=True
                    if i==len(s)-1:
                        return False
            elif s[i]=='+'or s[i]=='-':
                if has_sign:
                    if s[i-1]!='e'or s[i-1]!='E':
                        return False
                    else:
                        #如果这是第一次出现符号位，则必须在e/E后面
                        has_sign=True
                        if i>0 and s[i-1]!='e'or s[i-1]!='E':
                            return False
            elif s[i]=='.':
                #如果出现过了小数点或者e，则不对
                if has_point or has_e:
                    return False
                else:#第一次出现小数点
                    has_point=True
                    if i>0 and(s[i-1]=='e'or s[i-1]=='E'):
                        return False
            else:
                if s[i]<0 or s[i]>9:
                    return False
        return True

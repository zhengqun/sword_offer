#实现一个函数：把字符串中的空格换成ASCII码：%20,最直白的思路就是：把每遇到的空格进行替换，但是会增加很多额外的移动时间，因为'——'只占一个空间
#位置，而"%","2","0"则占有三个位置，因此每遇到一个空格都需要多移动两个空格，并且后面的元素会多移动倍次，这样时间复杂度在O（n^2）
#换种思路：从后向前移动元素位置，时间复杂度：O(n)：首先遍历字符串，找出有多少个空格，这样新申请的长度为:len(原有字符串)+2*count（' '）

class Replace_Blank:
    def find_Blank(self,target_string):
        #判断下字符串是空，还是不合法
        if not isinstance(target_string,str) or len(target_string) <= 0 or target_string == None:
            return ''
        space_num = 0  #空格的个数
        for i in target_string:
            if i == " ":
                space_num += 1
        #新的字符串长度，目标字符串长度
        new_string_len = len(target_string) + space_num * 2
        target_string_len=len(target_string)
        new_string_str=target_string * [None]
        #原字符串下标，新字符串下标
        index_og,new_og=target_string_len-1, new_string_len-1  #反向遍历
        while index_og >= 0 and new_og > index_og:
            if target_string[index_og] != ' ':
                new_string_str[new_og] = target_string[index_og]
                index_og-=1
                new_og-=1
            else:
                new_string_str[new_og-2 : new_og +1] = ["%","2","0"]
                new_og-=3
                index_og-=1
            return ''.join(new_string_str)






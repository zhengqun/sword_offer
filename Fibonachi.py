#数学公式：f(n)=f(n-1)+f(n-2)
#最简单就是递归求解：Fibonacii(n-1)+Fibonacii(n-2)
#使用交换两数也可以达到此效果
class Fibonachhi:
    def  fun_F(self,temp,n):
         result=[0,1]
         if n<2:
             return result[n]
         else:
             pre=0
             end=1
             fi=0
             for i in range(2,n):
                 fi = pre + end
                 end=pre
                 pre=fi
         return fi
#顺时针打印矩阵：由5x5的矩阵可得出如下规律：最后一圈只有一个数字，坐标为（2，2），5>2x2，同理6x6的矩阵，最后一圈是四个数字
#左上角仍是2x2，6>2x2，然后顺时针打印，从左到右，上到下，右到左，下到上
class Solution:
    def Print_Matrix(self,matrix):
        if matrix ==None:
            return None
        start =0
        rows=len(matrix)
        cols=len(matrix[0])
        result=[]
        if cols > start*2 and rows > start*2:
            print_matrix_circle(matrix,cols,rows,start,result)
            start+=1
        return result
    def prit_matrix_circle(self,matrix,cols,rows,start,result):
        #下标从（0，0）计数：而且X,Y相反
        end_x=cols-1-start
        end_y=rows-1-start
        #从左到右打印,i走的列号
        for i in range（start,end_x + 1）:
            result.append(matrix[start][i])
        #从上到下打印,需要列数大于初始数，列数>1
        if start < end_y:
            for i in range(start+1,end_y+1):
                result.append(matrix[i][end_x)
        #从右到左打印
        if start<end_x and start<end_y:
            for i in range(end_x-1,start-1,-1)
                result.append(matrix[end_y][i])
        #从下往上打印
        if start < end_x and start < end_y-1:
            for i in range(end_y-1,start,-1):
                result.append(matrix[i][start])
#自己写法：版二：
class Soultion:
    def print_matrix(self,number,rows,cols):
        if number ==None or rows<=0 or cols<=0:
            return None
        start =0     #(0,0)开始
        result=[]
        cols=len(number[0])
        rows=len(number)
        if rows > start *2 and cols > start*2:
            self.print_number_circle(number,rows,cols,start,result)
            start+=1
    def print_number_circle(self,number,rows,cols,start,result):
        end_x=rows-1-start
        end_y=cols-1-start
        #从左到右打印一行
        for i in range(start,end_y + 1):
            result.append(number[start][i])
        #从上到下打印
        if start<end_x:
            for i in range(start+1,end_x+1):
                result.append(number[i][end_y])
        #从右到左打印,倒着打印，
        if start < end_x and start < end_y:
            for i in range(start,end_y,-1):
                result.append(number[end_x][i])
        #从下到上打印
        if start < end_x and start < end_y:
            for i in range(start+1,end_x,-1):
                result.append(number[i][end_y])



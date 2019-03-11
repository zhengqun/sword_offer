class find_array_solution:
    def find(self,array,target):
        #首先判断数组array是否为空
        if array ==[]:
            return False
        #定义有多少行，列
        num_row=len(array)
        num_col=len(array[0])
        #i:代表行，j代表列
        i=0
        j=num_col-1

        while j>=0 and i<num_row:
            if target > array[i][j]:
                i = i+1
            elif target < array[i][j]:
                j -= 1
            else:
                return True







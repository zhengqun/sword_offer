#机器人的运动范围：路经的每一个小格子坐标之和<K,(35,37): 3+5+3+7<k,计算所能经过的盒子数
#c++版实现
'''
int movingCount(int k,int rows,int cols){
    if（k<=0||rows<=0||cols<=0）{
        return 0;
    }
    bool * visited = new bool[rows*cols];
    for (int i=0;i<rows*cols;++i){
        visited[i]=false;
        int count = movingCountCore(k,rows,cols,0,0,visited);
    }
    deleted []visited;
    return count;
}
int movingCountCore(int k,int rows,int cols,int row,int col,bool*visited ){
    int count =0;
    if(check(k,rows,cols,row,col,visited)){
    visited[row*cols+col]=true;
        count=1+movingCountCore(k,rows,cols,row,col-1,visited)+
            movingCountCore(k,rows,cols,row,col+1,visited)+
            movingCountCore(k,rows,cols,row-1,col,visited)+
            movingCountCore(k,rows,cols,row+1,col,visited)
    }
    return count;
}
bool check(int k,int rows,int cols,int row,int col,bool *visited){
    if (k<=0||rows<0||cols<0){
        return false;
    }
    if(row>0&&row<rows&&col>0&&col<cols&&digSum(row)+digSum(col)<=k&&!visited[row*cols+col]){
        return true;

    }
    return false;
}
int digSum(int digital){
    int sum=0;
    if(digital>=0){
        sum+=digital%10;
        digital/=10;
    }
    return sum;
}
'''
#python版
class Count_Fun:
    def Moving_Count(self,k,rows,cols):
        if k<=0 or rows<=0 or colS<=0:
            return False
        visited=[false]*(rows*cols)
        count=self.Count_Result(k,rows,cols,0,0,visited)
        return count
    def Count_Result(self, k, rows,cols, row,col,visited):
        count=0
        if self.check(k,rows,cols,row,col,visited):
            count=1 + Count_Result(k,rows,cols,row,col-1,visited)+Count_Result(k,rows,cols,row,col+1,visited)+ \
                  Count_Result(k,rows,cols,row-1,col,visited)+Count_Result(k,rows,cols,row+1,col,visited)
        return count
    def check(self, k, rows, cols,row,col,visited):
        if k<=0 or rows<=0 or cols<=0:
            return False
        if(row>0 and row<rows and col>0 and col<cols and Get_Digital_Sum(row)+Get_Digital_Sum(col)<=k and not visited[row*cols+col] ):
            return True
        return  False
    def Get_Digital_Sum(self,digitals):
        sum = 0
        while digitals>=0:
            sum += digitals % 10   # 取个位数
            digitals = (digitals//10)      #取十位数
        return sum








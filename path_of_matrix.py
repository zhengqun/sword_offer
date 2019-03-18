#矩阵中的路径：回朔法遍历树形结构，每个格子只许进入一次，每一步的坐标变化：（row,col-1）（row,col+1）（row-1,col）（row+1,col）
#进入格子打标记防止再次进入，声明成布尔矩阵
#c++实现
'''
bool hasPath(char*matrix,int rows,int cols,char*str){
    if(matrix==nullptr||rows<0||cols<0||str==nullptr){
        return false;
    }
    #声明布尔值矩阵：
    bool*visted=new bool[rows,cols];
    memset(visited,0,rows*cols);
    int path_length=0
    for(int row=0;row<rows;++row){
        for(int col=0;col<cols;++col){
            if(hasPath(matrix,rows,cols,row,col,str,path_length,visited)){
                return true;
            }
        }
    }
    delete[]visited;
    return false;
}
bool hasPathCore(const char*matrix,int rows,int cols,int row,int col,char*str,int&path_length,bool*visited){
    if (str[path_length]='\o'){
        return true;
    }
    bool hasPath = false;
    if(row>0&&row<rows&&col>0&&col<cols&&matrix[row*cols+col]==str[path_length]&&!visited[row*cols+col]){
        ++path_length;
        visited[row*cols+col]=true;
        hasPath=hasPathCore(matrix,rows,cols,row,col-1,str,path_length,visited)||hasPathCore(matrix,rows,cols,row,col+1,str,path_length,visited)
                ||hasPathCore(matrix,rows,cols,row-1,col,str,path_length,visited)||hasPathCore(matrix,rows,cols,row+1,col,str,path_length,visited);
    if(!hasPath){
        --path_length;
        visited[row*cols+col]=false;
    }
    }
    return hasPath;
}
'''
#python版
class Fun_Solution:
    def hasPath(self,matrix,rows,cols,path):
        if matrix==None or rows<0 or cols<0 or path==None:
            return False
        visited=[0]*](rows*cols)
       path_length=0
       for row in range(rows):
           for col in range(cols):
                if self.hasPathCore(matrix,rows,cols,row,col,path,path_length,visited):
                    return True
       return False
    def hasPathCore(self,matrix,rows,cols,row,col,path,path_length,visited):
        if len(path)==path_length:
            return True
        hasPath = False
        if row>=0 and row<rows and col>=0 and col<cols and matrix[row*cols+col]==path[path_length] and not visited[row*cols+col]:
            path_length+=1
            visited[row*cols+col]=True
            #固定一个点，查询该点上下左右路径
            hasPath=hasPathCore(matrix,rows,cols,row,col-1,path,path_length,visited) or \
                    hasPathCore(matrix,rows,cols,row,col+1,path,path_length,visited) or \
                    hasPathCore(matrix,rows,cols,row-1,col,path,path_length,visited) or \
                    hasPathCore(matrix,rows,cols,row+1,col,path,path_length,visited)
        elif not hasPath:
            path_length-=1
            visited[row*cols+col]=False
        return hasPath






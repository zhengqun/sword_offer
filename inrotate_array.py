#实现快速排序的算法：首先随机选一个值，作为目标然后比较两边数组的值得大小，如果左边的比他大就移到右边去，相反右边的移到左边去
#c++代码实现快速排序
'''
int Partition(int data[],int start,int end,int length){
    if(data==nullptr||length<=0||start<0||end>length){
       throw new std::exception("invaild error")

}
    int index=RandomInRange(start,end)
    swap(&data [index],&data[end])
    int small = start -1
    for (index=start;index<end;++index){
        if(data[index]<data[end]){
            ++small
            if(small != index){
                swap(&data[index],&data[small])
    }
    }
    }
    ++small
    swap(&data[small],&data[end])
    return small ;
}
使用快速排序：index=quicksort（data,length,start,end）
if(index>start){quicksort(data,length,start,end-1)}
if(index<start){quicksort(data,length,start+1,end)}
return index
'''
'''
#面试题11：旋转数组：{12345}-->{34512}:这样的数组称为旋转数组
#旋转数组需要考虑旋转之后的样子，data[start]==data[end]条件
int Min(int *number,int length){
    if (number==nullptr||length<=0){
        throw new std::exception("invaild paramters");
    }
    int index1=0;
    int index2=length -1;
    int indexmin=index1
    while(number[index1]>=number[index2]){
        if(index2-index1=1){
            indexmin=index2;
            break;
        }
    }
    #找中点下标
    indexmid=(index1+index2)/2
    if(number[indexmid]>=number[index1]){
        index1=indexmid
    }
    elseif(number[indexmid]<=number[index2]){
        index2=indexmid
    }
    elseif(number[indexmid]==number[index1]&&number[index1]==number[index2]){
        return find_min(number,index1,index2)
    }
    elseif(number[indexmid]<number[index2]){
        index2=indexmid
    }
}
int find_min(int *number,int index1,index2){
    int result = number[index1]
    for (int i=0;i<index2;++i){
        if(result>number[i]){
            result=number[i]   #返回的第一个比它小的，正好是最小值，因为这个值是第二个数组中的开始元素，也是最小值
        }
    }
    return result;
}
'''
#python版
class Roate_Array:
    def inRoate_Array(self,number):
        if not number:
            return
        index1=0
        index2=len(number)-1
        minVal=0
        if (number[index1]<number[index2]):
            minVal=number[index1]
            return minVal
        else:
            while(index2-index1)>1:
                indexmid = (index1+index2)/2
                if number[indexmid]>=number[index1]:
                    index1=indexmid
                elif number[indexmid]<=number[index2]:
                    index2=indexmid
                elif number[indexmid]==number[index2]==number[index1]:
                    #找最小值
                    for i in range(index1,index2):
                        if number[i]<number[index1]:  #找第一个小于number[index],即为右数组最小值开始值
                            minVal=number[i]
                            index2=i
            return minVal



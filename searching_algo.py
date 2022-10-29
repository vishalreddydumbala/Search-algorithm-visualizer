import time

from sort import sort_the_data


def linearSearch(data,value,drawData,timeTick):
    j=(-1)
    for i in range(len(data)):
        if(data[i]==value):
            j=i
            drawData(data, ['gray' if x==j else 'orange' for x in range(len(data))])
            time.sleep(timeTick)
            break
        elif(data[i]!=value and i!=len(data)-1):
            j=i
            drawData(data, ['gray' if x==j else 'orange' for x in range(len(data))])
            time.sleep(timeTick)
        else:
            j=-1
            drawData(data, ['gray' if x==i else 'orange' for x in range(len(data))])
            time.sleep(timeTick)
    drawData(data, ['green' if x==j else 'red' for x in range(len(data))])
    time.sleep(timeTick)
    
def binarySearch(data,value,drawData,timeTick,popup):
    response=popup("Data is not sorted \nDo you want to sort it?","?")
    if(response == "yes"):
        sort_the_data(data,drawData,timeTick)
        popup('Data is sorted','msg',)
        start = 0
        end=len(data)-1
        while(start<end):
            mid=int((start+end)/2)
            drawData(data,['gray' if ((x==start) or (x==end)) else 'orange' for x in range(len(data))])
            if(data[mid]>value):
                start=mid
            elif(data[mid]<value):
                end=mid
            else:
                drawData(data,['green' if x==mid else 'red' for x in range(len(data))])
    else:
        popup("binary search can't be done without sorting","error")
        drawData(data, ['orange' for x in range(len(data))])
        
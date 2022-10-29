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
        data=sort_the_data(data,drawData)
        popup('Data is sorted','msg',)
        l = 0
        r=len(data)-1
        while (l <= r):
            m = int(l + (r - l) / 2)
            drawData(data, ['gray' if x==m else 'orange' for x in range(len(data))])
            time.sleep(timeTick)
            if (data[m] == value):
                drawData(data, ['green' if x==m else 'red' for x in range(len(data))])
                time.sleep(timeTick)
                return
            if (data[m] < value):
                l = m + 1
            elif(data[m] > value):
                r = m - 1
        drawData(data, ['red' for x in range(len(data))])
        time.sleep(timeTick)
    else:
        popup("binary search can't be done without sorting","error")
        
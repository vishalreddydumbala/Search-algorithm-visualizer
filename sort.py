import time

def sort_the_data(data, drawData,timeTick):
    n = len(data) 
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j] 
                # if swapped then color becomes orange else stays gray
                drawData(data, ['orange' if x == j + 1 else 'gray' for x in range(len(data))])
                time.sleep(timeTick)      
    # sorted elements generated with orange color
    drawData(data, ['orange' for x in range(len(data))])

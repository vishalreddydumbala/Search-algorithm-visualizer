import random
from tkinter import *
from tkinter import messagebox, ttk

from tkmacosx import *

from searching_algo import binarySearch, linearSearch

root = Tk()
# Variables
selected_algo = StringVar()
data = []
value = -1
colorarr = []

# functions
def popup(str1,querry):
    if(querry=="error"):
        response = messagebox.showerror("This is messagebox", str1)
    else:
        response = messagebox.askquestion("This is messagebo", str1)
        return response

def start():
    global data
    global value
    global colorarr
    if(selected_algo.get()=="Linear Search"):
        linearSearch(data,value,drawData,speedscroll.get())
    elif(selected_algo.get()=="Binary Search"):
        binarySearch(data,value,drawData,speedscroll.get(),popup)

    j=-1
    for x in colorarr:
        if x == 'green':
            j=1
    if(j<0):
        popup("No number found","error")

def drawData(data,colorArray):  # for bar graph
    global colorarr 
    colorarr = colorArray
    canv_height = 380
    canv_width = 780
    x_width = canv_width / (len(data) + 1)
    offset = 30
    spacing = 10
    # normalized data
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = canv_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = canv_height

        Ui_Canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        Ui_Canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]),fill="black")
    root.update_idletasks()

def generate():
    global data
    global value

    Ui_Canvas.delete("all")
    # print("Search Algorithum:" + selected_algo.get())
    try:
        minVal = int(MinEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(MaxEntry.get())
    except:
        maxVal = 10
    try:
        sizeVal = int(SizeEntry.get())
    except:
        sizeVal = 10
    try:
        value = int(ValEntry.get())
        data = []
        for _ in range(sizeVal):
            data.append(random.randrange(minVal, maxVal + 1))
        drawData(data,['orange' for x in range(len(data))])
    except:
        value = -1
        popup("Enter the value","error")

    # data = []
    # for _ in range(sizeVal):
    #     data.append(random.randrange(minVal, maxVal + 1))
    # drawData(data,['orange' for x in range(len(data))])


# Window Properties
root.title("Search Algorithm Visulation")
root.config(bg="black")
root.maxsize(800, 600)

# User Frame
Ui_Frame = Frame(root, width=780, height=200, bg="gray")
Ui_Frame.grid(row=0, column=0, padx=5, pady=5)
# bar Frame
Ui_Canvas = Canvas(root, width=780, height=380, bg="white")
Ui_Canvas.grid(row=1, column=0, padx=5, pady=5)

# UI Area
# row0
AlgoLabel = Label(Ui_Frame, text="Algorithum: ", bg="gray", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky=W)
AlgMenu = ttk.Combobox(Ui_Frame, textvariable=selected_algo, values=["Linear Search", "Binary Search"],width=10)
AlgMenu.grid(row=0, column=1, padx=5, pady=5, sticky=E)
AlgMenu.current(0)

#Buttons
AlgButton = Button(Ui_Frame, text="Generate", bg="orange", fg="white", command=generate).grid(row=0, column=2, padx=5, pady=5, sticky=W)
StartButton = Button(Ui_Frame, text="Start", bg="green", fg="white", command=start).grid(row=0, column=3, padx=5, pady=5, sticky=E)
ExitButton = Button(Ui_Frame, text="Exit", bg="red", fg="white", command=exit).grid(row=0, column=4, padx=5, pady=5, sticky=E)

#speed of animation
speedscroll = Scale(Ui_Frame,from_=0.1,to=2.0,length=200,digits=2,resolution=0.1,orient=HORIZONTAL,label="Select speed")
speedscroll.grid(row=0,column=5,columnspan=3,padx=5,pady=5)

# row1
SizeLabel = Label(Ui_Frame, text="Size: ", bg="gray", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky=E)
SizeEntry = Entry(Ui_Frame, width=10)
SizeEntry.grid(row=1, column=1, padx=3, pady=5, sticky=W)

ValLabel = Label(Ui_Frame, text="Value: ", bg="gray", fg="white").grid(row=1, column=2, padx=5, pady=5, sticky=E)
ValEntry = Entry(Ui_Frame, width=10)
ValEntry.grid(row=1, column=3, padx=3, pady=5, sticky=E)

MinLabel = Label(Ui_Frame, text="Min: ", bg="gray", fg="white").grid(row=1, column=4, padx=5, pady=5, sticky=E)
MinEntry = Entry(Ui_Frame, width=5)
MinEntry.grid(row=1, column=5, padx=3, pady=5, sticky=W)

MaxLabel = Label(Ui_Frame, text="Max: ", bg="gray", fg="white").grid(row=1, column=6, padx=5, pady=5, sticky=E)
MaxEntry = Entry(Ui_Frame, width=5)
MaxEntry.grid(row=1, column=7, padx=3, pady=5, sticky=E)

root.mainloop()

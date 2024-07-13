from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('Sorting Algorithms Visualizer')
root.geometry('900x600+200+80')#width x height + x + y
root.config(bg='#082A46')#background color
data=[]

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    cavas_width = 870
    x_width = cavas_width/(len(data)+1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i/max(data) for i in data]

    for i ,height in enumerate(normalised_data):
        x0 = i*x_width + offset + spacing_bet_rect
        y0 = canvas_height - height*400  #we have multiplied 400 bcoz we will normalised our values with one formula so that our data won't ecxceed the canvas
        x1 = (i+1)*x_width
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),font=("new roman",15,"italic bold"),fill="orange")
    
    root.update_idletasks()

def StartAlgorithm():
    global data
    if not data: 
        return
    if algo_menu.get() == 'Quick Sort':
        quick_sort(data,0,len(data)-1,drawData,speedscale.get())
    
    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(data,drawData,speedscale.get())
    
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data,drawData,speedscale.get())
        drawData(data,['green' for x in range(len(data))])

    
def generate():
    global data
    print("selected algorithm :" + selected_algorithm.get())
    min_value = int(minvalue.get())
    max_value = int(maxvalue.get())
    size_value = int(sizevalue.get())
    
    data = []
    for _ in range(size_value):
        data.append(random.randrange(min_value, max_value + 1))
    drawData(data, ['#A90042' for x in range(len(data))])

selected_algorithm = StringVar()#This instance can hold a string value and be used to track and update the value of a widget.
#label, button, speed scale

mainLabel = Label(root,text='Algorithm :',font = ('new roman',16,'italic bold'),bg='#05897A',width=10,fg="black",relief=GROOVE ,bd=5)
mainLabel.place(x=0,y=0)

algo_menu=ttk.Combobox(root,width=15 ,font=('new roman',19,'italic bold'),textvariable=selected_algorithm,values=['Bubble Sort','Merge Sort','Quick Sort']) #combobox is a dropdown menu(widget)
algo_menu.place(x=145,y=0)
algo_menu.current(0)#by default bubble sort

random_generate = Button(root,text='Generate',font=('arial',12,'italic bold'),bg='#2DAE9A',activebackground="#05945B",activeforeground="white",relief=SUNKEN,bd=5,width=10,command=generate)
random_generate.place(x=750,y=60)

sizevaluelabel= Label(root,text='Size :',font = ('new roman',12,'italic bold'),bg='#0E6DA5',width=10,fg="black",height=2,relief=GROOVE ,bd=5)
sizevaluelabel.place(x=0,y=60)

sizevalue = Scale(root,from_=0,to=30,resolution=1,orient=HORIZONTAL,font=('arial',14,'italic bold'),relief=GROOVE,bd=2,width =10)
sizevalue.place(x=120,y=60)

minvaluelabel= Label(root,text='Min Value :',font = ('new roman',12,'italic bold'),bg='#0E6DA5',width=10,fg="black",height=2,relief=GROOVE ,bd=5)
minvaluelabel.place(x=250,y=60)

minvalue = Scale(root,from_=0,to=10,resolution=1,orient=HORIZONTAL,font=('arial',14,'italic bold'),relief=GROOVE,bd=2,width =10)
minvalue.place(x=370,y=60)

maxvaluelabel= Label(root,text='Max Value :',font = ('new roman',12,'italic bold'),bg='#0E6DA5',width=10,fg="black",height=2,relief=GROOVE ,bd=5)
maxvaluelabel.place(x=500,y=60)

maxvalue = Scale(root,from_=0,to=100,resolution=1,orient=HORIZONTAL,font=('arial',14,'italic bold'),relief=GROOVE,bd=2,width =10)
maxvalue.place(x=620,y=60)

start= Button(root,text='Start',font=('arial',12,'italic bold'),bg='#C45B09',activebackground="#05945B",activeforeground="white",relief=SUNKEN,bd=5,width=10 ,command=StartAlgorithm)
start.place(x=750,y=0)

speedlabel1=Label(root,text='Speed :',font = ('new roman',12,'italic bold'),bg='#0E6DA5',width=10,fg="black",relief=GROOVE ,bd=5)
speedlabel1.place(x=400,y=0)

speedscale = Scale(root,from_=0.1,to=5.0,resolution=0.1,length=200,digits=2,orient=HORIZONTAL,font=('arial',14,'italic bold'),relief=GROOVE,bd=2,width =10)
speedscale.place(x=520,y=0)

canvas = Canvas(root,width=870,height=450,bg='black')
canvas.place(x=10,y=130)
root.mainloop()

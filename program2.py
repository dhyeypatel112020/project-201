from tkinter import *
import tkinter

window=Tk()

window.geometry("800x500")
window.title("Intrest calculator")
window.configure(bg="white")

heading_label=Label(window,text="Intrest calculator",fg="#363795",bg="white",font=("Calibri",30),bd=4.5)
heading_label.place(x=0,y=30)

principe_label=Label(window,text="principle",fg="#004ff9",bg="white",font=("Calibri",20),bd=4)
principe_label.place(x=0,y=100)

principe_value=Entry(window,text="",bd=1,width=25,)
principe_value.place(x=25,y=150)

rate_label=Label(window,text="rate",fg="#004ff9",bg="white",font=("Calibri",20),bd=4)
rate_label.place(x=300,y=100)

rate_value=Entry(window,text="",bd=1,width=25,)
rate_value.place(x=325,y=150)

time_label=Label(window,text="time",fg="#004ff9",bg="white",font=("Calibri",20),bd=4)
time_label.place(x=600,y=100)

time_value=Entry(window,text="",bd=1,width=25,)
time_value.place(x=625,y=150)



def culculate_intrest():
   # p = float(principe_label.get())
    #r = float(rate_label.get())
    #t = float(time_label.get())
    p=float(principe_value.get())
    r = float(rate_value.get())
    t = float(time_value.get())
    i = (p*r*t)/100
    intrest = round(i,2)

    result.destroy()
    
    #massage_lable=LabelFrame(result_frame,text=intrest,fg="#004ff9",bg="grey",font=("Calibri",20),width=44)    
    #massage_lable.place(x=200,y=300)

    #massage_lable.pack()
    message=Label(result_frame,text="Interest is Rs."+str(intrest), bg = "grey", font=("Calibri", 12), width=55)
    message.place(x=20,y=40)
    message.pack()

button1=Button(window,text="Calculate",fg="#004ff9",bg="white",font=("Calibri",20),bd=4,command=culculate_intrest)
button1.place(x=50,y=200)


#result_frame=LabelFrame(window,text="result",fg="#004ff9",bg="#4bc0c8",font=("Calibri",20),bd=4)
#result_frame.place(x=300,y=100)


result_frame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=40,y=380)

result=Label(result_frame,text="Your SI is : ", bg = "grey", font=("Calibri", 12), width=55)
result.place(x=100,y=90)
result.pack()


window.mainloop()#last line
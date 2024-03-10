from tkinter import *

#### Read The Value Of Button ####
def Button_Click(number):
    global val
    val=val+ str(number)
    data.set(val)

#### Clear The Value Of DIsplay ####   
def Button_Clear():
    global val
    val=""
    data.set("")

#### Show the Result Equal ####
def Button_equals():
    global val
    result=str(eval(val))
    data.set(result)

root=Tk()
root.title("My Calculator")  ###### Define Project name
root.geometry("361x381+500+200")  ##### size of the whole Display Screen
val=""

#### MAKING DISPLAY ####

data=StringVar()
display=Entry(root,bd=29,bg="powder blue",font=("ariel",20),justify=RIGHT,textvariable=data)
display.grid(row=0,columnspan=4)

#### Making BUTTONS ####
### Position Row=0 and Column 1,2,3,4 ###
button_7=Button(root,text=7,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(7))
button_7.grid(row=1,column=0)
button_8=Button(root,text=8,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(8))
button_8.grid(row=1,column=1)
button_9=Button(root,text=9,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(9))
button_9.grid(row=1,column=2)
button_Add=Button(root,text="+",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click("+"))
button_Add.grid(row=1,column=3)

#### Making BUTTONS ####
### Position Row=2 and Column 1,2,3,4 ###
button_4=Button(root,text=4,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(4))
button_4.grid(row=2,column=0)
button_5=Button(root,text=5,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(5))
button_5.grid(row=2,column=1)
button_6=Button(root,text=6,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(6))
button_6.grid(row=2,column=2)
button_Sub=Button(root,text="-",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click("-"))
button_Sub.grid(row=2,column=3)

#### Making BUTTONS ####
### Position Row=3 and Column 1,2,3,4 ###
button_1=Button(root,text=1,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(1))
button_1.grid(row=3,column=0)
button_2=Button(root,text=2,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(2))
button_2.grid(row=3,column=1)
button_3=Button(root,text=3,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(3))
button_3.grid(row=3,column=2)
button_Multiply=Button(root,text="*",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click("*"))
button_Multiply.grid(row=3,column=3)

#### Making BUTTONS ####
### Position Row=4 and Column 1,2,3,4 ###
button_0=Button(root,text=0,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click(0))
button_0.grid(row=4,column=0)
button_Clear=Button(root,text="CLEAR",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=Button_Clear)
button_Clear.grid(row=4,column=1)
button_Equal=Button(root,text="=",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=Button_equals)
button_Equal.grid(row=4,column=2)
button_Division=Button(root,text="/",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:Button_Click("/"))
button_Division.grid(row=4,column=3)

root.mainloop()
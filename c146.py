from tkinter import *

root=Tk()
root.title("Fibonacci sum")
root.geometry("400x400")

textinput=Entry(root) 
fibonacciseries=Label(root,text=" Fibonacci Series:")
fibonaccisum=Label(root,text=" Fibonacci Sum :")

def lokesh():
 sum=0
input1=textinput.get()
first_no=0
second_no=1
counter=1
sum2=0
while(counter ==  input1):
     fibonacciseries["text"] += str(sum) + ""
     counter = counter + 1
     first_no = second_no
     second_no = sum
     sum = first_no + second_no
     fibonaccisum["text"]="Fibonacci Sum :" + str(sum)
     sum2 = sum2 + sum
     fibonacciseries["text"]="Fibonacci series" + str(sum2)

button=Button(root, text="Show Fibonacci series", command=lokesh , bg="skyblue" ,fg="black")
button.place(relx=0.5 , rely=0.2 , anchor=CENTER)

textinput.place(relx=0.5 , rely=0.1 , anchor=CENTER)
fibonacciseries.place(relx=0.5 , rely=0.3, anchor=CENTER)
fibonaccisum.place(relx=0.5 , rely=0.4 , anchor=CENTER)
root.mainloop()


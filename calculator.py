import tkinter as tk
import tkinter.font as tkfont

root = tk.Tk()
root.title("Calculator")
root.geometry("450x600")
root.resizable(0,0)

frame = tk.Frame(root,bg='gray', highlightbackground='black', highlightthickness=2)
frame.place(relx=0.06, rely=0.1, relheight=0.85, relwidth=0.9)

# TITLE
titleFont = tkfont.Font(family="Fixedsys", size=30)
title = tk.Label(frame, text="CALCULATOR", font=titleFont, bg="gray", fg="white")
title.place(relx=0.2, rely=0.25)
loadingfont = tkfont.Font(family="Fixedsys", size=18)
loading = tk.Label(frame, text="Loading...", font=loadingfont)
loading.place(relx=0.3, rely=0.6)

# HEADING
headingFont = tkfont.Font(family="Lucida Grande", size=20)
heading = tk.Label(root, text="CALCULATOR", fg="red", font=headingFont)

# INPUT BOX
inputBox = tk.Entry(frame, bg='black', width=40, fg = 'white', selectbackground="gray",  font=20)

#----------------------------------------------------------------------------

calculations = ""
# BUTTON FUNCTIONS
def input_num (event):
    global calculations
    text = inputBox.get()
    btn_text = event.widget['text']
    inputBox.insert(len(text), btn_text)
    calculations += btn_text
    try:
        calculations = str(eval(calculations))
    except ZeroDivisionError:
        inputBox.delete(0, 'end')
        inputBox.insert(0, "Division By Zero is not defined")
        root.after(1500, lambda: inputBox.delete(0, 'end'))

def operate(event):
    global calculations
    inputBox.delete(0,'end')
    calculations += event.widget['text']
    print(calculations)

def clear():
    global calculations
    calculations = ""
    inputBox.delete(0, 'end')
    print(calculations)

def equals():
    global calculations
    print("Result:", eval(calculations))
    inputBox.delete(0, 'end')
    inputBox.insert(0,str(eval(calculations)))
    calculations=""

#----------------------------------------------------------------------------
# NUMBER BUTTONS
#1
Button1 = tk.Button(frame, width=10, height=3, text="1", font=20, bg="coral")
Button1.bind('<Button-1>', input_num)
#2
Button2 = tk.Button(frame, width=10, height=3, text="2", font=20, bg="coral")
Button2.bind('<Button-1>', input_num)
#3
Button3 = tk.Button(frame, width=10, height=3, text="3", font=20, bg="coral")
Button3.bind('<Button-1>', input_num)
#4
Button4 = tk.Button(frame, width=10, height=3, text="4", font=20, bg="coral")
Button4.bind('<Button-1>', input_num)
#5
Button5 = tk.Button(frame, width=10, height=3, text="5", font=20, bg="coral")
Button5.bind('<Button-1>', input_num)
#6
Button6 = tk.Button(frame, width=10, height=3, text="6", font=20, bg="coral")
Button6.bind('<Button-1>', input_num)
#7
Button7 = tk.Button(frame, width=10, height=3, text="7", font=20, bg="coral")
Button7.bind('<Button-1>', input_num)
#8
Button8 = tk.Button(frame, width=10, height=3, text="8", font=20, bg="coral")
Button8.bind('<Button-1>', input_num)
#9
Button9 = tk.Button(frame, width=10, height=3, text="9", font=20, bg="coral")
Button9.bind('<Button-1>', input_num)
#0
Button0 = tk.Button(frame, width=10, height=3, text="0", font=20, bg="coral")
Button0.bind('<Button-1>', input_num)

# OPERATOR BUTTONS
# ADD
addBtn = tk.Button(frame, width=10, height=3, text="+", font=20, bg="black", fg="white")
addBtn.bind('<Button-1>', operate)
# SUBTRACT
subtractBtn = tk.Button(frame, width=10, height=3, text="-", font=40, bg="black", fg="white")
subtractBtn.bind('<Button-1>', operate)
# DIVIDE
divideBtn = tk.Button(frame, width=10, height=3, text="/", font=40, bg="black", fg="white")
divideBtn.bind('<Button-1>', operate)
# MULTIPLY
multiplyBtn = tk.Button(frame, width=10, height=3, text="*", font=40, bg="black", fg="white")
multiplyBtn.bind('<Button-1>', operate)
# EQUALS
equalsBtn = tk.Button(frame, width=10, height=3, text="=", font=40, bg="black", fg="white", command=equals)
# CLEAR
clrBtn = tk.Button(frame, width=10, height=3, text="Clear", font=40,bg="black", fg="white", command=clear)


def calculator():
    title.destroy()
    loading.destroy()    
    
    heading.grid(row=0, columnspan=3, padx=140, pady=10)

    inputBox.grid(row=1,columnspan=3, padx=15, pady=22, ipady=6)
    Button1.grid(column=0, row=2, sticky="N", )
    Button2.grid(column=1, row=2, sticky="N")
    Button3.grid(column=2, row=2, sticky="N")
    Button4.grid(column=0, row=3, sticky="N")
    Button5.grid(column=1, row=3, sticky="N")
    Button6.grid(column=2, row=3, sticky="N")
    Button7.grid(column=0, row=4, sticky="N")
    Button8.grid(column=1, row=4, sticky="N")
    Button9.grid(column=2, row=4, sticky="N")
    Button0.grid(column=1, row=5, sticky="N")
    addBtn.grid(column=0, row=5, sticky="N")
    subtractBtn.grid(column=2, row=5, sticky="N")
    divideBtn.grid(column=0, row=6, sticky="N")
    multiplyBtn.grid(column=2, row=6, sticky="N")
    clrBtn.grid(column=1, row=6, sticky="N")
    equalsBtn.grid(column=1, row=7, sticky="N")

root.after(2000, calculator)

root.mainloop()

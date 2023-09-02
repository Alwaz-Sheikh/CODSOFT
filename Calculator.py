import tkinter as tr

def button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tr.END)
            display.insert(tr.END, result)
        except Exception as e:
            display.delete(0, tr.END)
            display.insert(tr.END, "Error")
    elif text == "C":
        display.delete(0, tr.END)
    else:
        display.insert(tr.END, text)

#main window
root = tr.Tk()
root.title("Calculator")
root.configure(bg="black")

#display
display = tr.Entry(root, font=("calibri", 25), bg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)
buttons = ["7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+" ]
row_val = 1
col_val = 0

for button_text in buttons:
    button = tr.Button(root, text=button_text, font=("calibri", 22),width=6, height=2)
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    button.bind("<Button-1>", button_click)
    button.configure(bg="light grey")  
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1



root.mainloop()

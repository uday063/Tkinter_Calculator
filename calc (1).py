import tkinter as tk

def click(x):
    entry.insert(tk.END, x)

def clear():
    entry.delete(0, tk.END)

def backspace():
    curr = entry.get()
    entry.delete(len(curr)-1, tk.END)

def calc():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")
root.resizable(False, False)
root.configure(bg="blue")

entry = tk.Entry(root, width=16, font=("Arial", 24),
                 borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

r = 1
c = 0
for b in buttons:
    if b == "=":
        cmd = calc
    else:
        cmd = lambda x=b: click(x)

    tk.Button(root, text=b, command=cmd, font=("Arial", 14),
              height=2, width=5,
              bg="orange" if b in "+-/*=" else "gray",
              fg="white", bd=0).grid(row=r, column=c, pady=6, padx=6)

    c += 1
    if c == 4:
        r += 1
        c = 0

tk.Button(root, text="Clear", font=("Arial", 14),
          command=clear, bg="red", fg="white",
          bd=0, width=12, height=2).grid(row=r, column=0, columnspan=2, pady=6)

tk.Button(root, text="Backspace", font=("Arial", 14),
          command=backspace, bg="gray", fg="white",
          bd=0, width=12, height=2).grid(row=r, column=2, columnspan=2, pady=6, padx=6)

root.mainloop()

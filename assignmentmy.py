import tkinter as tk

# Functions
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: 0")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)  # Simply clear the entry box

# main window ake code eka
root = tk.Tk()
root.title("Hashini - Calculator")
root.config(bg='light gray')
root.geometry('320x380+0+0')  # Size eka
root.resizable(False, False)  # Disable resizing eka

# Display box ake code eka
entry = tk.Entry(root, width=19, font=('Arial bold', 20), bd=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons tika
button_7 = tk.Button(root, text="7", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(7))
button_7.grid(row=1, column=0, padx=5, pady=5)

button_8 = tk.Button(root, text="8", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(8))
button_8.grid(row=1, column=1, padx=5, pady=5)

button_9 = tk.Button(root, text="9", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(9))
button_9.grid(row=1, column=2, padx=5, pady=5)

button_4 = tk.Button(root, text="4", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(4))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = tk.Button(root, text="5", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(5))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = tk.Button(root, text="6", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(6))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_1 = tk.Button(root, text="1", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(1))
button_1.grid(row=3, column=0, padx=5, pady=5)

button_2 = tk.Button(root, text="2", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(2))
button_2.grid(row=3, column=1, padx=5, pady=5)

button_3 = tk.Button(root, text="3", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(3))
button_3.grid(row=3, column=2, padx=5, pady=5)

button_0 = tk.Button(root, text="0", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click(0))
button_0.grid(row=4, column=0, padx=5, pady=5)

button_plus = tk.Button(root, text="+", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click("+"))
button_plus.grid(row=1, column=3, padx=5, pady=5)

button_minus = tk.Button(root, text="-", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click("-"))
button_minus.grid(row=2, column=3, padx=5, pady=5)

button_multiply = tk.Button(root, text="x", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click("*"))
button_multiply.grid(row=3, column=3, padx=5, pady=5)

button_divide = tk.Button(root, text="/", font=('Arial bold', 15), width=5, height=2, command=lambda: button_click("/"))
button_divide.grid(row=4, column=3, padx=5, pady=5)

button_equal = tk.Button(root, text="=", font=('Arial bold', 15), bg="pink", width=5, height=2, command=calculate)
button_equal.grid(row=4, column=2, padx=5, pady=5)

button_clear = tk.Button(root, text="C", font=('Arial bold', 15), bg="yellow", width=5, height=2, command=clear)
button_clear.grid(row=4, column=1, padx=5, pady=5)

#main eka
root.mainloop()
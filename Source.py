import tkinter as tk
from tkinter import messagebox

# Declaration of global variable
temp_Val = "Celsius"

# Getting drop-down value
def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp

# Conversion of temperature
def call_convert(rlabel1, inputn):
    try:
        temp = float(inputn.get())
        if temp_Val == 'Celsius':
            # Conversion of Celsius temperature to Fahrenheit
            f = (temp * 9 / 5) + 32
            rlabel1.config(text="%.1f Fahrenheit" % f)
        if temp_Val == 'Fahrenheit':
            # Conversion of Fahrenheit temperature to Celsius
            c = (temp - 32) * 5 / 9
            rlabel1.config(text="%.1f Celsius" % c)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Creating Tk window
root = tk.Tk()
root.geometry('300x150+600+200')
root.title('Temperature Converter')

inputNumber = tk.StringVar()
var = tk.StringVar()

# Label and entry field
input_label = tk.Label(root, text="Enter temperature")
input_entry = tk.Entry(root, textvariable=inputNumber)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)
result_label = tk.Label(root)
result_label.grid(row=3, columnspan=4)

# Drop-down setup
dropDownList = ["Celsius", "Fahrenheit"]
drop_down = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
drop_down.grid(row=1, column=2)

# Button widget
result_button = tk.Button(root, text="Convert", command=lambda: call_convert(result_label, inputNumber))
result_button.grid(row=2, columnspan=2)

# Infinite loop to run the tkinter program
root.mainloop()

from tkinter import *


# All Converting Functions
def mile_to_km():
    result = float(input.get()) * 1.609
    converted_num["text"] = result


def km_to_mile():
    result = float(input.get()) / 1.609
    converted_num["text"] = result


def celsius_to_fahrenheit():
    result = (int(input.get()) * 9.5) + 32
    converted_num["text"] = result


def foot_to_cm():
    result = int(input.get()) * 30.48
    converted_num["text"] = result


# All Program Components and Functionality
def func(event):
    converted_num["text"] = 0
    func_name = menu.get(menu.curselection())
    start_unit["text"] = func_name.split('_')[0]
    end_unit["text"] = func_name.split('_')[2]
    button["command"] = functions_dict[func_name]


functions = ["Mile_to_Km", "Km_to_Mile", "Cls_to_Fnt", "Foot_to_Cm"]
functions_dict = {"Mile_to_Km": mile_to_km, "Km_to_Mile": km_to_mile, "Cls_to_Fnt": celsius_to_fahrenheit, "Foot_to_Cm": foot_to_cm}

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50, bg="#364547")

menu = Listbox(height=len(functions), bd=0, bg="#364547", fg="#ffb037", font=("Arial", 13, "bold"))
for item in functions:
    menu.insert(functions.index(item), item)
menu.bind("<<ListboxSelect>>", func)
menu.grid(column=3, row=3)

start_unit = Label(text="", font=("Arial", 18, "bold"), fg="#f58634", bg="#364547")
start_unit.grid(column=2, row=0)

end_unit = Label(text="", font=("Arial", 18, "bold"), fg="#f58634", bg="#364547")
end_unit.grid(column=2, row=1)

label = Label(text="is equal to", font=("Arial", 18, "bold"), fg="#f58634", bg="#364547")
label.grid(column=0, row=1)

converted_num = Label(text=0, font=("Arial", 18, "bold"), fg="#81b214", bg="#364547")
converted_num.grid(column=1, row=1)

input = Entry(width=10, fg="#81b214", bg="#364547", font=("Arial", 15, "bold"))
input.insert(END, string=0)
input.grid(column=1, row=0)

button = Button(text="Calculate", bd=0, font=("Arial", 10, "bold"), fg="white", bg="#81b214", command='')
button.grid(column=1, row=2)


window.mainloop()

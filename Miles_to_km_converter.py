from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Miles to Km converter")
##
switch=False
factor=1.6
def read_user_input(miles_input):
    user_input=miles_input.get()
    return user_input
def check_user_input(miles_input):
    window.update()
    try:
        user_input=float(read_user_input(miles_input))
    except ValueError:
            messagebox.showinfo(title="error",message=f"invalid input, enter a number")
            return False
    else:
        return user_input
def convert(miles_input,text_result):
    global factor
    user_input=check_user_input(miles_input)*factor
    if user_input!=False:
        text_result["text"]=round(user_input, 2)
def clear(miles_input,text_result):
    miles_input.delete(0, END)
    miles_input.insert(0, "")
    text_result["text"]=0
def switch_value_of_swith_variable():
    global switch
    if switch:
        switch=False
    elif switch==False:
        switch=True
def Switch(text_miles,text_km):
    global switch,factor
    switch_value_of_swith_variable()
    if switch:
        factor=0.62137
        print(factor)
        text_miles["text"]="Km"
        text_km["text"]="Miles"
    if switch==False:
        factor=1.6
        print(factor)
        text_miles["text"]="Miles"
        text_km["text"]="Km"
    window.update()
##
def create_main_page():
    main_page_list=[]
    miles_input=Entry(window)
    text_miles=Label(window,text="Miles")
    text=Label(window,text="is equal to")
    text_result=Label(window,text=0)
    text_km=Label(window,text="Km")
    convert_button=Button(window,text="convert",command=lambda:convert(miles_input,text_result))
    clear_button=Button(window,text="clear",command=lambda:clear(miles_input,text_result))
    switch_button=Button(window,text="switch",command=lambda:Switch(text_miles,text_km))
    main_page_list.extend([miles_input,text_miles,text,text_result,text_km,
    convert_button,clear_button,switch_button])
    return main_page_list
def grid_main_page():
    main_page_list=create_main_page()
    row=0
    column=1
    for element in main_page_list:
        element.grid(row=row,column=column)
        column+=1
        if column==3:
            column=0
            row+=1
        if row==1 and column==3:
            column=0
            row+=1
grid_main_page()
window.mainloop()
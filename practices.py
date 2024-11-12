import tkinter as tk
mywindow = tk.Tk()
mywindow.title("first_button")
mywindow.geometry("500x500")
frame = tk.Frame(mywindow, width="500", height="500")
frame.pack()

canvas = tk.Canvas(frame, width="500", height="300")
canvas.pack()

def whatnew():
    rec1=canvas.create_rectangle(100,100,200,200, fill="pink")
    print("Hello!!!!!!!!!!!!")
button = tk.Button(frame, text="click me!" ,command=whatnew)
button.pack()

mywindow.mainloop()
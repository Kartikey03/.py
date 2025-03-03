import tkinter as tk

root=tk.Tk()

root.geometry("500x500")
tk.Label(root, text="Hello World!", font=('Calibri', 18)).pack(padx=20, pady=40)

def dabao():
    root2=tk.Toplevel()
    root2.geometry("300x300")

    label2=tk.Label(root2, text="doodh!", font=("Arial", 20)).pack(padx=20, pady=40)
    
button=tk.Button(root, text="mujhe dabao!", font=('Arial', 30), command=dabao).pack()
root.mainloop()
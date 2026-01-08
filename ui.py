import tkinter as tk

root = tk.Tk()
root.title("To-Do App")
root.geometry("400x300")

label = tk.Label(root,text="Welcome to To-Do App")
label.pack()

entry = tk.Entry(root)
entry.pack()
root.mainloop()
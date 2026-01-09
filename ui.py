import tkinter as tk

tasks = []

root = tk.Tk()
root.title("To-Do App")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to To-Do App")
label.pack()

entry = tk.Entry(root)
entry.pack()

def add_task():
    task = entry.get()

    if task.strip() == "":
        return

    tasks.append(task)
    task_listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

def delete_task():
    selected = task_listbox.curselection()

    if not selected:
        return

    index = selected[0]
    task_listbox.delete(index)
    tasks.pop(index)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

task_listbox = tk.Listbox(root)
task_listbox.pack()

root.mainloop()

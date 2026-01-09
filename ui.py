import tkinter as tk

# -------------------
# Application State
# -------------------
tasks = []

# -------------------
# Main Window
# -------------------
root = tk.Tk()
root.title("To-Do App")
root.geometry("400x300")

# -------------------
# Widgets
# -------------------
label = tk.Label(root, text="Welcome to To-Do App")
label.pack()

entry = tk.Entry(root)
entry.pack()

def add_task():
    task = entry.get()

    if task.strip() == "":
        return  # ignore empty input

    tasks.append(task)
    task_listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root)
task_listbox.pack()

# -------------------
# Event Loop
# -------------------
root.mainloop()

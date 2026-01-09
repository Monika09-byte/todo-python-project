import tkinter as tk
import todo   # import logic module

# --------------------
# Main Window
# --------------------
root = tk.Tk()
root.title("To-Do App")
root.geometry("400x350")

# --------------------
# Widgets
# --------------------
label = tk.Label(root, text="Welcome to To-Do App")
label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# --------------------
# Functions (UI → Logic)
# --------------------
def add_task_ui():
    task = entry.get()

    if task.strip() == "":
        return

    todo.add_task(task)
    task_listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

def delete_task_ui():
    selected = task_listbox.curselection()

    if not selected:
        return

    index = selected[0]
    todo.delete_task(index)
    task_listbox.delete(index)

# --------------------
# Buttons
# --------------------
add_button = tk.Button(root, text="Add Task", command=add_task_ui)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task_ui)
delete_button.pack(pady=5)

# --------------------
# Task Display
# --------------------
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# --------------------
# Event Loop
# --------------------
root.mainloop()

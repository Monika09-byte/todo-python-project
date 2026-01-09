# todo.py
# Core logic for the To-Do App

tasks = []

def add_task(task):
    tasks.append(task)

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def get_tasks():
    return tasks

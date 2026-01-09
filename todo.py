# todo.py
# Core logic with safe file persistence

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks.txt")

tasks = []

def load_tasks():
    global tasks
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks.append(task)
    save_tasks()

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()

def get_tasks():
    return tasks

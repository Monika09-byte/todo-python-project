import streamlit as st
import todo

# Load tasks once
todo.load_tasks()

st.title("📝 To-Do App (Streamlit)")

# --------------------
# Add Task Section
# --------------------
task_input = st.text_input("Enter a new task")

if st.button("Add Task"):
    if task_input.strip():
        todo.add_task(task_input)
        st.success("Task added!")
        st.rerun()
    else:
        st.warning("Task cannot be empty")

# --------------------
# View Tasks Section
# --------------------
st.subheader("Your Tasks")

tasks = todo.get_tasks()

if not tasks:
    st.info("No tasks available")
else:
    for i, task in enumerate(tasks):
        col1, col2 = st.columns([4, 1])

        col1.write(task)

        if col2.button("❌", key=i):
            todo.delete_task(i)
            st.rerun()

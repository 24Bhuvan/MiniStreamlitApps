import streamlit as st

# Title
st.title("📝 To-Do List App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input for new task
new_task = st.text_input("➕ Add a new task:")

# Add Task Button
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"✅ Task added: {new_task}")
    else:
        st.warning("⚠️ Please enter a task before adding.")

st.markdown("---")

# Display Current Tasks
st.subheader("📌 Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.8, 0.2])  # Layout for task & delete button
        col1.write(f"🔹 {task}")
        if col2.button("❌", key=f"remove_{i}"):  
            st.session_state.tasks.pop(i)
            st.rerun()  # Refresh the app after deletion
else:
    st.info("No tasks added yet. Start by adding a new task!")

# Footer
st.markdown("---")
st.write("📌 A simple to-do list app built with **Streamlit**. 🚀")


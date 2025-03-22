import streamlit as st

st.session_state.tasks = st.session_state.get("tasks", [])

task = st.text_input("Add task:")
if st.button("Add") and task:
    st.session_state.tasks.append(task)

for i, t in enumerate(st.session_state.tasks):
    if st.button(f"❌ {t}", key=i):
        st.session_state.tasks.pop(i)
        st.experimental_rerun()

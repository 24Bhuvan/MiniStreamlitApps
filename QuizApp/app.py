import streamlit as st
import pandas as pd
import random
df = pd.read_csv('QuizApp/quiz_questions.csv')
df1=df.to_dict(orient="records")

if "quiz" not in st.session_state:
    st.session_state.quiz = df1
    st.session_state.current_question = 0
    st.session_state.score = 0
    random.shuffle(st.session_state.quiz)
st.title("📚 Fun Quiz Game")
if st.session_state.current_question < len(st.session_state.quiz):
    question = st.session_state.quiz[st.session_state.current_question]
    st.subheader(f"Q{st.session_state.current_question + 1}: {question['Question']}")
    choices = [question[f"Option{i}"] for i in range(1, 5)]
    selected_answer = st.radio("Choose an answer:", choices)
    if st.button("Submit Answer"):
        if selected_answer == question["Answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {question['Answer']}")
        st.session_state.current_question += 1
        st.rerun()
else:
    st.subheader(f"🎉 Quiz Completed! Your Score: {st.session_state.score}/{len(st.session_state.quiz)}")
    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        random.shuffle(st.session_state.quiz)
        st.rerun()
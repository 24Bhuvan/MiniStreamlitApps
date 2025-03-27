import streamlit as st
import pandas as pd
import random

# Load quiz data
df = pd.read_csv('QuizApp/quiz_questions.csv')
quiz_data = df.to_dict(orient="records")

# Initialize session state
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz" not in st.session_state:
    st.session_state.quiz = quiz_data
    st.session_state.current_question = 0
    st.session_state.score = 0
    random.shuffle(st.session_state.quiz)

st.title("📚 Fun Quiz Game 🎯")
st.markdown("### Test your knowledge with this fun and interactive quiz!")

# Start button
if not st.session_state.quiz_started:
    if st.button("🚀 Start Test"):
        st.session_state.quiz_started = True
        st.rerun()
    st.stop()

# Progress bar
progress = st.session_state.current_question / len(st.session_state.quiz)
st.progress(progress)

# Quiz logic
if st.session_state.current_question < len(st.session_state.quiz):
    question = st.session_state.quiz[st.session_state.current_question]
    st.subheader(f"Q{st.session_state.current_question + 1}: {question['Question']}")

    # Shuffle answer choices
    choices = [question[f"Option{i}"] for i in range(1, 5)]
    random.shuffle(choices)
    selected_answer = st.radio("Choose an answer:", choices, key=st.session_state.current_question)

    col1, col2 = st.columns(2)
    if col1.button("✅ Submit Answer"):
        if selected_answer == question["Answer"]:
            st.success("🎉 Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! The correct answer is: {question['Answer']}")
        
        st.session_state.current_question += 1
        st.rerun()

    if col2.button("⏩ Skip"):
        st.session_state.current_question += 1
        st.rerun()

else:
    # Quiz Completion UI
    st.subheader(f"🎉 Quiz Completed! Your Score: {st.session_state.score}/{len(st.session_state.quiz)}")
    percentage = (st.session_state.score / len(st.session_state.quiz)) * 100
    st.write(f"📊 **Score Percentage: {percentage:.2f}%**")

    # Restart Button
    if st.button("🔄 Restart Quiz"):
        st.session_state.quiz_started = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        random.shuffle(st.session_state.quiz)
        st.rerun()

import streamlit as st
import random

# Initialize session state for score tracking
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# Title
st.title("Rock - Paper - Scissors")

# Display Scoreboard
st.subheader(f"🏆 You: {st.session_state.user_score} | 🤖 Computer: {st.session_state.computer_score}")
st.divider()

# Create buttons for user choices
col1, col2, col3 = st.columns(3)
r = col1.button("Rock ✊")
p = col2.button("Paper 📄")
s = col3.button("Scissors ✂️")

# Game choices
choices = ["Rock", "Paper", "Scissors"]

if r or p or s:
    user_choice = "Rock" if r else "Paper" if p else "Scissors"
    computer_choice = random.choice(choices)

    # Show choices
    st.write(f"🧑 You chose: **{user_choice}**")
    st.write(f"🤖 Computer chose: **{computer_choice}**")

    # Determine winner
    if user_choice == computer_choice:
        st.info("😐 It's a Draw!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.session_state.user_score += 1
        st.success("🎉 You Won!")
    else:
        st.session_state.computer_score += 1
        st.error("💀 You Lost!")

    # Refresh button
    if st.button("🔄 Play Again"):
        st.rerun()

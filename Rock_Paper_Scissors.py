import streamlit as st
import random
st.title("Rock Paper Scissors")

col1,col2,col3=st.columns(3,gap="small")
r=col1.button("ROCK")
p=col2.button("PAPER")
s=col3.button("SCISSOR")

game_outs=["Rock", "Paper", "Scissors"]

if r or p or s:
    user_choice = "Rock" if r else "Paper" if p else "Scissors"
    computer_choice = random.choice(game_outs)
    st.write(f"Computer chose: **{computer_choice}**")
    if user_choice == computer_choice:
        st.info("It's a Draw!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.success("You Won!")
    else:
        st.error("You Lost!")

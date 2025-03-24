import streamlit as st
import random
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = lowercase_letters
    if use_uppercase :
        characters+=uppercase_letters
    if use_numbers :
        characters +=numbers
    if use_symbols:
        characters +=symbols
    return "".join(random.choice(characters) for i in range(length)) 
user_password_length= st.slider("Enter password length: ", value=8, min_value=8,max_value=30)
box=st.multiselect("Select password features: " ,options=("Numbers", "Symbols","Uppercase Letters") , default=("Numbers",))
use_numbers = False
use_symbols = False
use_uppercase = False
if "Numbers" in box:
    use_numbers= True
if "Symbols" in box:
    use_symbols=True
if "Uppercase Letters" in box:
    use_uppercase= True
length = user_password_length
button=st.button(label="Generate Password")
if button:
   
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    st.success(f"Generated Password: `{password}`")
    
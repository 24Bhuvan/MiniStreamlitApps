import streamlit as st
import random

# Set Streamlit page configuration (Must be the first Streamlit command)
st.set_page_config(page_title="Secure Password Generator", page_icon="🔐", layout="centered")

# Define character sets for password generation
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    """Generates a random password based on user preferences."""
    characters = LOWERCASE_LETTERS
    if use_uppercase:
        characters += UPPERCASE_LETTERS
    if use_numbers:
        characters += NUMBERS
    if use_symbols:
        characters += SYMBOLS
    
    return "".join(random.choice(characters) for _ in range(length))

# Title and Description
st.title("🔐 Secure Password Generator")
st.write("Generate strong and secure passwords based on your preferences.")

# User Inputs
length = st.slider("Select password length:", min_value=8, max_value=30, value=12)
options = st.multiselect("Select password features:", 
                         options=["Numbers", "Symbols", "Uppercase Letters"], 
                         default=["Numbers"])

# Set password feature flags
use_numbers = "Numbers" in options
use_symbols = "Symbols" in options
use_uppercase = "Uppercase Letters" in options

# Generate password button
if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    st.success(f"**Generated Password:** `{password}`")
    st.write("💡 Tip: Copy and store your password securely!")

# Footer
st.markdown("---")
st.caption("🔒 Developed by Bhuvan Ummidisetti!")

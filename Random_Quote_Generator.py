import random
import streamlit as st

# Title
st.title("🌟 Magic Quote Generator 🌟")

# Button to generate a random quote
if st.button("✨ Click to generate a magic quote ✨"):
    quotes = [
        "The only way to do great work is to love what you do. – *Steve Jobs*",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. – *Winston Churchill*",
        "Believe you can and you're halfway there. – *Theodore Roosevelt*",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Success doesn’t just find you. You have to go out and get it.",
        "The harder you work for something, the greater you’ll feel when you achieve it.",
        "Don’t stop when you’re tired. Stop when you’re done.",
        "Do something today that your future self will thank you for.",
        "Little things make big days.",
        "It’s going to be hard, but hard does not mean impossible.",
        "Don’t wait for opportunity. Create it.",
        "Sometimes later becomes never. Do it now."
    ]
    
    # Display random quote
    st.markdown(f"> {random.choice(quotes)}")

# Add a separator
st.markdown("---")
st.write("💡 Click the button again for a new quote!")

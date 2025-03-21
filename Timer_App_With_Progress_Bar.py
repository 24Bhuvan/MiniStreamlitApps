import streamlit as st
import time as ts
from datetime import time

# Title
st.title("⏳ Timer App with Progress Bar")

# Function to convert time input into total seconds
def convert_to_seconds(value):
    """
    Converts Streamlit's time input format (HH:MM:SS) to total seconds.
    
    Args:
        value (datetime.time): Time input from the user.
    
    Returns:
        float: Total seconds, including milliseconds.
    """
    minutes, seconds, _ = str(value).split(":")
    total_seconds = int(minutes) * 60 + int(seconds)
    return total_seconds

# User Input: Time Picker
time_input = st.time_input("⏰ Set Timer", value=time(0, 0, 0))

# Validation: Ensure user sets a valid timer
if str(time_input) == "00:00:00":
    st.warning("⚠️ Please set a timer greater than 00:00:00")
else:
    total_seconds = convert_to_seconds(time_input)

    # Initialize progress bar and percentage display
    progress_bar = st.progress(0)
    progress_text = st.empty()  # Placeholder for updating progress percentage
    interval = total_seconds / 100  # Time interval for each progress step

    # Progress bar loop
    for i in range(100):
        progress_bar.progress(i + 1)  # Update progress bar
        progress_text.write(f"🔵 {i + 1}%")  # Display percentage
        ts.sleep(interval)  # Wait for the calculated interval

    # Completion Message
    st.success("✅ Timer Completed! 🎉")

# Footer
st.markdown("---")
st.write("📌 This is a simple countdown timer with a progress bar. Enjoy! 😊")

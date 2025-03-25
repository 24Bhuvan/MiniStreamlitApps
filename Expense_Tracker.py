import streamlit as st

# Initialize session state for storing expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# App Title
st.title("💰 Expense Tracker")

# Expense Input Form
with st.form("expense_form"):
    col1, col2 = st.columns([3, 2])

    # Input Fields
    expense_name = col1.text_input("📌 Expense Name")
    expense_amount = col2.number_input("💵 Expense Amount (₹)", min_value=0.0, format="%.2f")

    # Expense Categories
    categories = [
        "Food & Dining", "Transport", "Groceries", "Shopping",
        "Entertainment", "Healthcare", "Rent & Bills", "Education",
        "Travel", "Savings & Investments", "Miscellaneous"
    ]
    expense_category = st.selectbox("📂 Select Expense Category:", categories)

    # Add Expense Button
    if st.form_submit_button("➕ Add Expense"): 
        if expense_name and expense_amount > 0: 
            new_expense = {
                "Name": expense_name,
                "Amount": f"₹{expense_amount:.2f}",
                "Category": expense_category
            }
            st.session_state.expenses.append(new_expense)  
            st.success("✅ Expense added successfully!")
            st.rerun()  # Refresh to update the list
        else:
            st.error("❌ Please enter a valid expense name and amount.")

# Display Expenses
if st.session_state.expenses:
    st.subheader("📊 Expense Summary")

    # Create a structured layout
    for i, expense in enumerate(st.session_state.expenses):
        col1, col2, col3 = st.columns([3, 2, 1])

        # Show Expense Name & Category
        col1.write(f"**{expense['Name']}** ({expense['Category']})")
        # Show Expense Amount
        col2.write(f"**{expense['Amount']}**")
        # Delete Button
        if col3.button("❌", key=f"del_{i}"):
            st.session_state.expenses.pop(i)
            st.rerun()  # Refresh to reflect changes

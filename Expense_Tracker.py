import streamlit as st
if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.title('Expense Tracker')

form = st.form("Expense Form")

col1, col2 = form.columns(2, gap="small")
expense_name = col1.text_input("Expense Name")
expense_amount = col2.number_input("Expense Amount")
options= (
    "Food & Dining",
    "Transport",
    "Groceries",
    "Shopping",
    "Entertainment",
    "Healthcare",
    "Rent & Bills",
    "Education",
    "Travel",
    "Savings & Investments",
    "Miscellaneous"
)
expense_category=form.selectbox("Select Expense Category: ", options=options)

if form.form_submit_button("Add Expense"): 
    if expense_name and expense_amount > 0: 
        new_expense = {
            "Name": expense_name,
            "Amount": expense_amount,
            "Category": expense_category
        }
        st.session_state.expenses.append(new_expense)  
        st.success("Expense added successfully!")
    else:
        st.error("Please enter a valid expense name and amount.")

if st.session_state.expenses:
    st.subheader("Expense Summary")
    for i, expense in enumerate(st.session_state.expenses):
        col1, col2, col3 = st.columns([3, 2, 1])  # Create layout
        col1.write(f"**{expense['Name']}** ({expense['Category']})")
        col2.write(f"₹{expense['Amount']:.2f}")
        if col3.button("❌", key=f"del_{i}"):
            st.session_state.expenses.pop(i)
            st.rerun()
import streamlit as st

st.title("Boba Order Form")
st.markdown(
    """
    <style>
    body {
        background-color: beige;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Add a header
st.header("Please enter your order details:")

# Add a text input for the customer's name
customer_name = st.text_input("Name:")

# Add a multi-select dropdown for the sizes
sizes = st.selectbox("Size:", ["Small", "Medium", "Large"])

# Add a radio button for the flavors
flavor = st.selectbox("Flavor:", ["Honeydew", "Matcha", "Strawberry"])

# Add a checkbox for toppings
toppings = st.checkbox("Boba")

# Add a button to submit the form
if st.button("Submit"):
    result = f"Name: {customer_name} | Size: {sizes} | Flavor: {flavor} | Toppings: {toppings}"
    st.success(result)
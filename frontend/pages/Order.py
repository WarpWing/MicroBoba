import streamlit as st
st.title('Order Page')
st.subheader('Place your Boba order below!')

def form_callback():
    st.write(st.session_state.name)
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)
    

with st.form(key='order_form',clear_on_submit=True):
    name = st.text_input('Name', value="",key="name")
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
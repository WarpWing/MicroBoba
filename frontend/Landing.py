import streamlit as st
st.title('MicroBoba: A Microservice Boba Shop')

for key in st.session_state.keys():
    print(st.session_state[key])
    print(key)

if 'count' not in st.session_state:
    st.session_state.count = 0
    

def increment_counter(increment_value=0):
    st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
    st.session_state.count -= decrement_value

st.button('Increment', on_click=increment_counter,
    kwargs=dict(increment_value=1))

st.button('Decrement', on_click=decrement_counter,
    kwargs=dict(decrement_value=1))

st.write('Count = ', st.session_state.count)

def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
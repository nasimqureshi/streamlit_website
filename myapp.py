import streamlit as st


fname = st.text_input("Enter your first name:")
lname = st.text_input("Enter my last name")
message = st.text_area("Enter your text")
data_class = st.selectbox("Enter data class:", (1,2,3,4,5,6))

button = st.button("Submitted")
if button :
  st.markdown(f"""
              First Name : {fname}
              Last Name : {lname}
              Message : {message}
              Data_Class : {data_class}""")
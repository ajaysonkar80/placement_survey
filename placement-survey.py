import streamlit as st
name = st.text_input('Your name')
dob=st.date_input("When is your birthday?")
phone=st.text_input("Your Phone number")
email=st.text_input("Your Email ID")
vikshit_bharat=st.text_input("How can you contribute to Vikshit bharat")
future_plan=st.text_input("Your future plan")
submit=st.button("Submit")
student_dict={}
if submit:
    student_dict['name']=name
    student_dict['dob']=dob
    student_dict['phone']=phone
    student_dict['email']=email
    student_dict['vikshit_bharat']=vikshit_bharat
    student_dict['future_plan']=future_plan
    st.write("saved succesfully now you can exit.")
    st.write("send this to ajay",student_dict)

    
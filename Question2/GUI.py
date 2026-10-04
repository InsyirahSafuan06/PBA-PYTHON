import streamlit as st

#build in function title
st.title('Student Information System')

student_type = st.selectbox("Please Select Student Type:", ["Undergraduate", "Postgraduate", "Part-Time Student"])

with st.form("Student Information Form"):
    #control structure selection for student type
    if student_type == "Undergraduate":
        name_student = st.text_input("Name")
        age_student = st.number_input("Age", min_value = 19, max_value=100)
        student_id = st.text_input("Student ID")
        year_level = st.number_input("Year Level", min_value=1, max_value=5)
    elif student_type == "Postgraduate":
        name_student = st.text_input("Name")
        age_student = st.number_input("Age", min_value = 19, max_value=100)
        student_id = st.text_input("Student ID")
        year_level = st.number_input("Year Level", min_value=1, max_value=5)
        research_topic = st.text_input("Research Topic")
    else:
        name_student = st.text_input("Name")
        age_student = st.number_input("Age", min_value = 19, max_value=100)
        student_id = st.text_input("Student ID")
        year_level = st.number_input("Year Level", min_value=1, max_value=5)
        research_topic = st.text_input("Research Topic")
        work_hours = st.number_input("Work Hours", min_value=1, max_value=40)

    submitted = st.form_submit_button("Submit")

if submitted:
    #validate numeric inputs and display student information
    try:
        age_student = int(age_student)
        
        if student_type == "Part-Time Student":
            work_hours = int(work_hours)

        st.header("Student Information")
        st.write("Name: ", name_student)
        st.write("Age: ", age_student)
        st.write("Student ID: ", student_id)
        st.write("Student Type: ", student_type)    

        if student_type == "Undergraduate":
            st.write("Year Level: ", year_level)
        elif student_type == "Postgraduate":
            st.write("Year Level: ", year_level)
            st.write("Research Topic: ", research_topic)
        else:
            st.write("Year Level: ", year_level)
            st.write("Research Topic: ", research_topic)
            st.write("Work Hours: ", work_hours)

    #validate numeric inputs and display error message for invalid inputs
    except ValueError:
        st.error("Please enter valid numeric values for Age and Work Hours.") 

#caption and info for integrity declaration
st.caption("Integrity Declaration")
st.info("I declare that this application is my original work and complies with ethical programming standards.")
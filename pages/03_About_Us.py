from utility import check_password
import streamlit as st
import llm_functions # <--- This is the helper function that we have created 🆕
import prep_data

# # Do not continue if check_password is not True.  
# if not check_password():  
#     st.stop()


st.title("About Us 🌟")

st.header("Project Scope")
st.write("""
This project aims to develop a user-friendly app to guide Singapore employers in understanding and fulfilling their CPF obligations. The app will combine a chatbot and a CPF contribution calculator to provide:

Informative guidance: Clear explanations of CPF rules and regulations.
         
Practical tools: A calculator to accurately determine CPF contributions.
""")

st.header("Objectives")
st.markdown("""
**Provide clear guidance**: Explain CPF rules and regulations.
**Offer a CPF contribution calculator**: Help determine accurate CPF contributions.
**Provide instant answers**: Use AI to answer user queries.
**Stay up-to-date**: Ensure the information is always accurate.
""")

st.header("Data Sources")
st.write("""
    To ensure the accuracy and reliability of the information provided, we utilize data from the following sources:
""")
st.markdown("""
- **CPF Board**
- **Ministry of Manpower**
- **Associated partners** 

""")

st.header("Features")
st.markdown("""
Informative guidance: Clear explanations of CPF rules and regulations.
         
Practical tools: A calculator to accurately determine CPF contributions.
""")



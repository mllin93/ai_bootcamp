from utility import check_password
import streamlit as st
import llm_functions # <--- This is the helper function that we have created 🆕
import prep_data

# # Do not continue if check_password is not True.  
# if not check_password():  
#     st.stop()

st.title("Ask me anything about CPF contributions for your employees!")
form = st.form(key="form")

user_prompt = form.text_area("Enter your query regarding your CPF obligations as an employer here:", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = prep_data.ask_tax_relief_qn(user_prompt)
    st.write(response) 
    print(f"User Input is {user_prompt}")

with st.expander("IMPORTANT NOTICE"):
    st.write("""

This web application is a prototype intended for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions related to CPF contributions or employer obligations.

Please note that the information provided may be incomplete or inaccurate. It is crucial to consult the official CPF website or seek advice from a qualified tax advisor or accountant for accurate and up-to-date guidance.

The developer of this application assumes no liability for any actions taken based on the information provided.

""")
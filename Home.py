from utility import check_password
# Set up and run this Streamlit App
import streamlit as st

st.set_page_config(
    layout="centered",
    page_title="My Streamlit App",
    initial_sidebar_state="collapsed"
)

import prep_data

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()


st.sidebar.write("This guide provides clear and concise information on CPF regulations, deadlines, and penalties, ensuring compliance and avoiding unnecessary financial burdens. Whether you’re a small business owner or a large corporation, this app is your go-to tool for accurate CPF calculations and informed decision-making.")


# Add some content to the main app
col1, col2, col3 = st.columns([1, 1.8, 1])
with col2:
    st.image("pictures/employer_homepage.png", use_column_width=True)
st.html("<h1 style='text-align:center'>CPF Contribution Guide for Employers</h1>")
st.html("<p style='text-align:center; font-size: 1rem;'>Your go-to app for all things related to calculating and paying CPF contributions as an employer.</p>")
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <a href="Ask_Me_Anything" target="_self">
            <button style="padding: 10px 20px; border-radius: 10px; background-color: #0E5A40; border: 0px;">Get started →</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



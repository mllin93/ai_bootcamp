from utility import check_password
import streamlit as st  

# # Do not continue if check_password is not True.  
# if not check_password():  
#     st.stop()

st.title("Methodology")

# Display image
st.image("pictures/methodology.png")

st.subheader("How the app was created:")

st.markdown("""
This section outlines the steps used to build and structure the data for our CPF Contribution Guide for Employers application. Below is a detailed breakdown of the methodology:

Collect CPF Information
The initial step involves gathering relevant information on CPF contributions, rates, and regulations from official CPF Board sources. This data is extracted from publicly accessible documents and guidelines.

Organise and Structure Data
The collected data is meticulously organised and structured into a clear and accessible format. This includes categorising information by topics such as employer obligations, employee contributions, and tax relief.

Generate Embeddings and Create Vector Store
To enable efficient search and retrieval, each piece of text within the structured data is converted into vector embeddings using a suitable language model. These embeddings capture the semantic meaning of the text. The generated vectors are then stored in a vector database, enabling rapid similarity searches based on user queries.
""")

from utility import check_password
import streamlit as st
import llm_functions # <--- This is the helper function that we have created 
import prep_data
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

# Do not continue if check_password is not True.  
# if not check_password():  
#     st.stop()
    
# flyer_otters_path = "pictures/flyer_otters.png"  
# iras_logo_path = "pictures/iras logo.png"  

# st.sidebar.write("Your personal income tax relief calculator")

# # Display the logo at the top of the sidebar
# st.sidebar.image(iras_logo_path, use_column_width=True)  # `use_column_width` makes the logo fit the sidebar's width
# st.sidebar.image(flyer_otters_path, use_column_width=True) 

st.header("Calculate the CPF contributions payable to your employees")


with st.container(border=True):

    def add_field():
        st.session_state.fields_size += 1

    def delete_field(index):
        st.session_state.fields_size -= 1
        del st.session_state.fields[index]
        del st.session_state.deletes[index]

    def reset():
        st.session_state.clear()

    
    if "fields_size" not in st.session_state:
        st.session_state.fields_size = 0
        st.session_state.fields = []
        st.session_state.deletes = []
        add_field()
    

    # fields and types of the table
    for i in range(1,st.session_state.fields_size+1):
        c1, c2 = st.columns([9,1])
        with c1:
            ind, ca, cb, cc = st.columns([1,4,2,2])
            with ind:
                st.write(f'#{i}')
            with ca:
                st.session_state.fields.append(st.selectbox("Citizenship", ["Singaporean / 3rd Year PR", "2nd Year PR","1st Year PR"], key = f"citizenship_{i}"))
            with cb:
                st.session_state.fields.append(st.number_input(f"Monthly Wage ($)", key=f"wage_{i}", min_value = 500, step = 50))
            with cc:
                st.session_state.fields.append(st.number_input(f"Age as of month", key=f"age_{i}",step=1, min_value = 0))

        with c2:
            st.session_state.deletes.append(st.button("🗑", key=f"delete_{i}", on_click=delete_field, args=(i,)))

    left, _, _, right = st.columns(4)
    with left:
        st.button("＋ Add employee", on_click=add_field, use_container_width = True)
    with right:
        st.button("↺ Reset", on_click = reset, use_container_width = True)



# Calculate
def extract_df(data_dict):
    # Initialize a list to hold each entry as a dictionary
    entries = []
    
    # Loop through the dictionary and collect relevant fields
    i = 1
    while f'age_{i}' in data_dict:
        entry = {
            'age': data_dict[f'age_{i}'],
            'citizenship': data_dict[f'citizenship_{i}'],
            'wage': data_dict.get(f'wage_{i}', None),  # Use .get() to avoid KeyError
        }
        entries.append(entry)
        i += 1
    
    # Create a DataFrame from the list of entries
    return pd.DataFrame(entries)

# Extract the DataFrame
df = extract_df(st.session_state)

def match_age_to_rate(citizenship, age):
    if citizenship == 'Singaporean / 3rd Year PR':
        if age <= 55:
            return 0.17
        elif 55 < age <= 60:
            return 0.15
        elif 60 < age <= 65:
            return 0.115
        elif 65 < age <= 70:
            return 0.09
        else:
            return 0.075
    elif citizenship == '2nd Year PR':
        if age <= 55:
            return 0.09
        elif 55 < age <= 60:
            return 0.06
        elif 60 < age <= 65:
            return 0.035
        else:
            return 0.035
    elif citizenship == '1st Year PR':
        if age <= 55:
            return 0.04
        elif 55 < age <= 60:
            return 0.04
        elif 60 < age <= 65:
            return 0.035
        else:
            return 0.035

def calculate_cont(row):
    # Cap assessable wage
    wage = min(6000, row['wage'])
    rate = match_age_to_rate(row['citizenship'], row['age'])
    payable = wage * rate
    return pd.Series([f"{rate * 100:.1f}%", payable]) 

df[['rate','payable']] = df.apply(calculate_cont, axis=1)
total_payable = df['payable'].sum()
df['wage'] = df['wage'].apply(lambda x: f"${x:,.2f}")
df['payable'] = df['payable'].apply(lambda x: f"${x:,.2f}")
df.columns = [col.title() for col in df.columns]


st.header("Results")
st.success(f"The total amount of CPF contribution payable for your employees: ${total_payable:,.2f}", icon='💰')
with st.expander("View breakdown by employee"):
    st.dataframe(df, use_container_width=True, hide_index=True)


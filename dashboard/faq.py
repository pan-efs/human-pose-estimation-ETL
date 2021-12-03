import streamlit as st

def FAQ():
    sidebar = st.sidebar.selectbox(
        "FAQ",
        ("What is 'Browsing tool'?", "How it works?", "Upload files", "Delete files", "Do I lose my data?"),
    )
    
    if sidebar == "What is 'Browsing tool'?": st.sidebar.write("This app is...TODO")
    elif sidebar == 'How it works?': st.sidebar.write("This app works as...TODO")
    elif sidebar == 'Upload files': st.sidebar.write("You can upload only images...TODO")
    elif sidebar == 'Delete files': st.sidebar.write("You can delete files...TODO")
    elif sidebar == "Do I lose my data?": st.sidebar.write("No, you do not lose your data...TODO")
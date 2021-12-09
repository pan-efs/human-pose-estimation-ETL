#!/usr/bin/env python3
import streamlit as st

def FAQ():
    """
    A function which includes frequently asked questions.
    """
    sidebar = st.sidebar.selectbox(
        "FAQ",
        ("What is 'Browsing tool'?", 
         "Upload files", 
         "Delete files", 
         "Type of images", "Do I lose my data?", 
         "Can I interact with the DB?"
        ),
    )
    
    if sidebar == "What is 'Browsing tool'?": st.sidebar.write(
        """'Browsing tool' is a user friendly dashboard where helps users navigating in their local filesystem
            uploading, deleting and vizualizing image files.
        """)

    elif sidebar == 'Upload files': st.sidebar.write(
        """Navigate in your local filesystem and upload the desired images which you like to process with.
           JPG is the only acceptable extension and the limit size is 200MB per file.
        """)

    elif sidebar == 'Delete files': st.sidebar.write(
        """Delete all files that already exists in the platform. The files are deleted permanently.
           If you are not sure, you could take an advice pressing the 'Should I delete?' button.
        """)
    
    elif sidebar == 'Type of images': st.sidebar.write(
        """1) 'Preprocessed images': are those where exists in the platform but they have not been processed yet
           and they have not been inserted into the database.
           2) 'Processed images': are those where have been processed and all details have been inserted into the database.
        """)

    elif sidebar == 'Do I lose my data?': st.sidebar.write(
        """You do not lose your data after shutting down the docker.
           Your data is stored in the database permanently.
        """)
    
    elif sidebar == 'Can I interact with the DB?': st.sidebar.write(
        """'Browsing tool' does not provide direct interaction with your DB.
        """
        )
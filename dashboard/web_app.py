#!/usr/bin/python
import os
import pandas as pd
import random

from PIL import Image
import streamlit as st

from faq import FAQ


# Configuration of dashboard
st.set_page_config(
    page_title="Browsing tool",
    page_icon=":whale2:",
    layout='wide',
    initial_sidebar_state="expanded",
    menu_items={'Report a bug': 'https://github.com/pan-efs/AutomatedETL_3DHPE'}
)

# Constants
PATH_TO_ORIGINALS = '/app/imgs/originals'
PATH_TO_RENDERED = '/app/imgs/rendered'


# Title
st.title("Automated pipeline for 3D human pose estimation!")


# Sidebar 
# Helper display function
def display_rendered_image_in_platform(path_to_folder: str):
    images = []
    for img in os.listdir(path_to_folder): images.append(img)
    
    if images:
        n = random.randint(0, len(images) - 1)
        img = Image.open(f'{path_to_folder}/{images[n]}')
        st.sidebar.image(img, caption=images[n], width=300)
    else:
        st.sidebar.warning("There is no available image.")


if st.sidebar.button('Display a rendered image'): display_rendered_image_in_platform(PATH_TO_RENDERED)

# Main sidebar
FAQ()


# Helper functions
def display_images(files: list):
    if files:
        for file in files:
            img = Image.open(file)
            st.image(img, caption=file.name, width=500)


def save_images(files: list):
    with st.spinner('Please, wait a few seconds :)'):
        if files:
            for file in files:
                img = Image.open(file)
                img.save(f'{PATH_TO_ORIGINALS}/{file.name}')

    st.success('Ready!')


def delete_images_from_platform(path_to_folder: str, img_type: str):
    for img in os.listdir(path_to_folder):
        try:
           img_path = os.path.join(path_to_folder, img)
           os.remove(img_path)
    
        except OSError as e:
            st.error(f"Error: {img_path} : {e.strerror}")
    
    st.success(f'All {img_type} images have been deleted from the platform.')


def count_images_in_system(path_to_folder: str):
    counter = 0
    for _ in os.listdir(path_to_folder): counter += 1
    
    return counter


def display_images_in_platform(path_to_folder: str):
    images = []
    for img in os.listdir(path_to_folder): images.append(img)
    
    df = pd.DataFrame(images, columns=['Images'])
    st.dataframe(df)


# Split screen into two columns
col1, col2 = st.columns([1.5, 1])

# Col_1
with col1:
    files = st.file_uploader(
    "Pick one or more images files...",
    type = ['jpg'], 
    accept_multiple_files=True,
    key = 'file_uploader')
    
    display_images(files)

    if st.button('Save files') and files:
        save_images(files)
    

# Col_2
with col2:
    st.write("Here you can see what already exist in the platform...")

    display_images_in_platform(PATH_TO_ORIGINALS)
    count_preprocessed_imgs = count_images_in_system(PATH_TO_ORIGINALS)
    count_processed_imgs = count_images_in_system(PATH_TO_RENDERED)


    if st.button('Delete files') and count_preprocessed_imgs>0:
        delete_images_from_platform(PATH_TO_ORIGINALS, 'originals')
        delete_images_from_platform(PATH_TO_RENDERED, 'rendered')
    
    if st.button('Should I delete?'):
        st.info(f"Preprocessed images: {count_preprocessed_imgs} | Processed images: {count_processed_imgs}")

        if count_preprocessed_imgs == count_processed_imgs and count_processed_imgs == 0 and count_preprocessed_imgs == 0:
            st.success("Yes! But, table is empty!:)")
        elif count_preprocessed_imgs == count_processed_imgs:
            st.success("Yes!")
        else:
            st.warning(f"{count_preprocessed_imgs - count_processed_imgs} left! There is a risk to lose the remained images if you delete them now!")
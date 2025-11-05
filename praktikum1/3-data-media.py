#import liberary
import streamlit as st
import pandas as pd #untuk mengelolah data dalam bentuk frame tabel (dataframe)
import numpy as np # untuk memmbuat data numerik
import altair as alt # untuk membuat chart interaktif

st.header("Praktikum1 Visualisasi Data")
st.subheader("Bagian 1: Data element")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)
import streamlit as st
st.image(r"D:\titip\VISUALSISASI DATA\ASET\ayam.jpg")
# Image Courtesy by unplash
st.write("Image Courtesy: unplash.com")

# --- Bagian 2: Menampilkan Beberapa Gambar ---
st.write("Diplaying Multiple Images")
# Listing out animal images
animal_images = [
    r'D:\titip\VISUALSISASI DATA\ASET\ayam.jpg',
    r'D:\titip\VISUALSISASI DATA\ASET\beruang.jpg',
    r'D:\titip\VISUALSISASI DATA\ASET\kuda.jpg',
    r'D:\titip\VISUALSISASI DATA\ASET\burung.jpg',
    r'D:\titip\VISUALSISASI DATA\ASET\monyet.jpg',
] # <-- Pastikan list ditutup

# Panggilan fungsi st.image() untuk list gambar harus ditambahkan
st.image(animal_images, width=200) # Anda bisa atur width sesuai kebutuhan
# Image Courtesy
st.write("Image Courtesy: Unplash")

#Background Image Streamlit 
# tidak menyediakan dukungan bawaan untuk menambahkan background image ke dalam aplikasi. 
# Namun, Anda tetap dapat menambahkan background image dengan menggunakan CSS kustom. 
# Streamlit memungkinkan Anda untuk menyisipkan elemen HTML dan CSS melalui fungsi st.markdown, yang dapat digunakan untuk menyetel background image. 
import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    
    st.write("Image Courtesy: unplash")
    
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

st.write("Background Image")
# Calling Image in function
add_local_background_image(r'D:\titip\VISUALSISASI DATA\ASET\monyet.jpg')

# Resizing an Image 
# Resizing an Image di Streamlit berarti mengubah ukuran gambar yang ditampilkan 
# menggunakan fungsi st.image. Streamlit menyediakan parameter bawaan untuk mengontrol 
# ukuran gambar agar sesuai dengan kebutuhan tampilan aplikasi Anda. 
import streamlit as st
from PIL import Image

original_image = Image.open(r'D:\titip\VISUALSISASI DATA\ASET\monyet.jpg')

# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))
# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)


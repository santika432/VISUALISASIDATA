import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Padding")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)

#Columns with Padding dalam Streamlit adalah cara untuk menambahkan jarak atau ruang  di sekitar kolom agar tampilan elemen menjadi lebih rapi dan enak dilihat. Padding  digunakan untuk memastikan konten tidak terlalu rapat, memberikan kesan visual yang lebih profesional. 

import streamlit as st
from PIL import Image
img = Image.open("../../ASET/burung.jpg")
st.title("Padding")
#Defining Padding with columns
coll, padding, col2 = st.columns((10,2,10))
with coll:
    coll.image(img)
with col2:
    col2.image(img)
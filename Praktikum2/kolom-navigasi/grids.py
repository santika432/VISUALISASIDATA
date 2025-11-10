import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Grids")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)
#Grids dalam Streamlit adalah teknik pengaturan tata letak berbasis kolom yang  memungkinkan Anda untuk mengatur elemen antarmuka secara lebih terstruktur dalam pola 

import streamlit as st
from PIL import Image
img = Image.open("../../ASET/burung.jpg")
st.title("Grid")
#Defining no of Rows
for a in range(4):
# Defining no. of columns with size
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)
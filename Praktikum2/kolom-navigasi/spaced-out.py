import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Speaced - OutColumn")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)
import streamlit as st
from PIL import Image

# Membuka gambar
img = Image.open("../../ASET/burung.jpg")

st.title("Spaced-Out Columns")
# Membuat 2 baris
for _ in range(2):
    # Membuat 4 kolom dengan rasio lebar berbeda (3:1:2:1)
    cols = st.columns((3, 1, 2, 1))
    # Menempatkan gambar di setiap kolom
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)





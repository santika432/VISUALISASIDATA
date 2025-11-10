import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Column")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)
#menambahkan element dikolom 1
col1, col2 =  st.columns(2)
col1.write("ini adalah kolom pertama")
col1.image("../../ASET/burung.jpg")
# Menambahkan elemen gambar di kolom 2
col2.write("ini adalah kolom ke 2")
col2.image("../../ASET/kuda.jpg")
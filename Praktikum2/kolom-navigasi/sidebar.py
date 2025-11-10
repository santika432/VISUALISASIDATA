import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Sidebar")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)
#Sidebar adalah panel yang ditampilkan di sisi aplikasi. Ini memungkinkan pengguna tetap  fokus pada konten utama. Kita akan menggunakan fungsi st.sidebar() untuk mendefinisikan  sidebar di aplikasi kita. 

import streamlit as st
#Sideban
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)
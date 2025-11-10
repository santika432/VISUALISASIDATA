import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Containers")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)

#Sesuai dengan namanya, container tersebut kosong, dan kita dapat memasukkan hanya satu  elemen ke dalamnya. Untuk mendefinisikan container kosong, kita dapat menggunakan  sintaks st.empty(). 
import streamlit as st
import time
#Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f"{seconds} seconds have passed")
        time.sleep(1)
    st.write("Times up!")
import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Accordions")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)
#Ketika kita ingin menyembunyikan informasi tambahan dari pengguna atau tidak ingin  informasi selalu muncul di aplikasi kita, kita dapat menggunakan accordion. Ini juga dikenal  sebagai expander, karena saat pengguna mengganti expander ke keadaan terbuka, ia akan  berkembang dan menampilkan informasi tambahan. 


import streamlit as st
st.title('Exapanders')
with st.expander("Streamlit with Python"):
    st.write("Develop ML Applications in Minutes!!!!")

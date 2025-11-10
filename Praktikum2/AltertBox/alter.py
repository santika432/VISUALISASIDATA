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
#Streamlit tidak memiliki elemen Alert Box bawaan, tetapi Anda dapat menggunakan fungsi  st.warning(), st.success(), st.error(), dan st.info() untuk menampilkan pesan peringatan atau  pemberitahuan dengan gaya yang berbeda. Ini sering digunakan untuk memberikan umpan balik  kepada pengguna secara visual dalam aplikasi Streamlit. 


import streamlit as st
st.success("Successful")
st.warning("Warning")
st.info("Info")
st.error("Error")
st.exception("It is an exception")
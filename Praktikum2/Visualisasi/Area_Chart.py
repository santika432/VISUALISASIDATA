import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Area Chart")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)

df=pd.DataFrame(
    #menampilkan 40  baris 4 kolom 
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)
#memanggil Areachart dengan data yg sudah di buat di atas
st.area_chart(df)
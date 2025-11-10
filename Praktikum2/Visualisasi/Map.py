import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Map")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)
df=pd.DataFrame(
    #menampilkan 50  baris 2 kolom 
    np.random.randn(50, 2)/(10,10)+[15.4589, 75.0078],
    #lintang dan bujur
    columns=["latitude","longitude"]
)
st.map(df)
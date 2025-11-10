import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np
import graphviz as gv


st.title("Grafis")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)

st.graphviz_chart("""
digraph {
        "Traning Data" ->"ML Algoritnm"
        "ML Algoritnm" -> "Model"
        "Model" -> "Result forecasting"
        "New Data" -> "Model"
    }
""")
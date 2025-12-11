#import
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#header
st.caption("Praktikum - 6")
st.write("Kelompok : 9")
st.markdown("""
- Santika Sintia Larasati - 0110122045  
- Saepulloh - 0110222183  
- Muhammad Ammar - 0110122308  
""")

#dataset
stores =['Stores A','Stores B', 'Stores C']
male = [150,200, 180]
female= [120,230,170]

#data transaksi penjualan
stores =['Stores A','Stores B', 'Stores C']
produk_a = [200,250, 300]
produk_b= [150,300,200]

#dataquarter
q1_male=[150, 180, 160]
q1_female = [140, 190,280]

q2_male=[170, 190, 175]
q2_female=[130,210, 160]

#1 grfik staced vertical bar chart
st.subheader ("1.Stacked Vertical Barchart")
fig,ax =plt.subplots()
x = np.arange(len(stores))
ax.bar(x,male, label='Male', color='blue')
ax.bar(x,female, bottom = male, label='female', color='red')

ax.set_title('population by gender and store')
ax.set_xlabel('stores')
ax.set_ylabel('population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()
st.pyplot(fig)

#Fgrafik stacked vertical bar
st.subheader ("2.Stacked Vertical Barchart dengan matplotlip")
fig,ax =plt.subplots()
x = np.arange(len(stores))
ax.bar(x,produk_a, label='produk A', color='green')
ax.bar(x,produk_b, bottom = produk_a, label='produk b', color='blue')

ax.set_title('sales transaction by store')
ax.set_xlabel('stores')
ax.set_ylabel('sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()
st.pyplot(fig)

# 3. grafik kustomisasi stacked bar chart

st.subheader("3. grafik kustomisasi stacked bar chart")

for i in range(len(x)):
    plt.text(x[i], produk_a[i]/2, str(produk_a[i]), ha='center', color='white')    
    plt.text(x[i], produk_a[i]+produk_b[i]/2, str(produk_b[i]), ha='center', color='black')

st.pyplot(fig)

# 4 grafik multiple stacked vertical bar chart 
st.subheader ("4.grafik multiple stacked vertical bar chart ")
fig, ax =plt.subplots()
width =0.4
x=np.arange(len(stores))

#quarter 1
ax.bar(x-width/2, q1_male, label='Q1 Male', color='green', width= width)
ax.bar(x-width/2, q1_female, bottom= q1_male , label='Q1_female', color='red', width= width)
#quarter 2
ax.bar(x+width/2, q2_male, label='Q2 Male', color='blue', width= width)
ax.bar(x+width/2, q2_female, bottom= q2_male , label='Q2_female', color='pink', width= width)

ax.set_title('population by gender and store(multiple quarters)')
ax.set_xlabel('stores')
ax.set_ylabel('population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()
st.pyplot(fig)
# =====================
# IMPORT
# =====================
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# =====================
# HEADER
# =====================
st.caption("Praktikum - 7")
st.subheader("Horizontal Bar Chart & Stacked Horizontal Bar Chart")
st.write("Kelompok : 9")
st.markdown("""
- Santika Sintia Larasati - 0110122045  
- Saepulloh - 0110222183  
- Muhammad Ammar - 0110122308  
""")

# =====================
# DATASET (SUDAH BENAR)
# =====================
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [230, 300, 400, 350]
sales_2024 = [300, 340, 200, 420]

y = np.arange(len(brands))
bar_width = 0.4

# =====================
# FILTER
# =====================
kategori = st.selectbox(
    "Pilih kategori visualisasi",
    ['basic chart', 'kustomisasi grafik', 'multiple chart']
)

# =====================
# BASIC CHART
# =====================
if kategori == "basic chart":
    st.subheader("Horizontal Bar Chart Sederhana")

    fig1, ax1 = plt.subplots()
    ax1.barh(y, sales_2023)
    ax1.set_yticks(y)
    ax1.set_yticklabels(brands)
    ax1.set_xlabel("Total Sales")
    ax1.set_title("Sales 2023")
    st.pyplot(fig1)

    st.subheader("Stacked Horizontal Bar Chart")

    fig2, ax2 = plt.subplots()
    ax2.barh(y, sales_2023, label='2023')
    ax2.barh(y, sales_2024, left=sales_2023, label='2024')
    ax2.set_yticks(y)
    ax2.set_yticklabels(brands)
    ax2.set_xlabel("Total Sales")
    ax2.set_title("Stacked Sales")
    ax2.legend()
    st.pyplot(fig2)

# =====================
# KUSTOMISASI GRAFIK
# =====================
elif kategori == "kustomisasi grafik":
    st.subheader("Customized Horizontal Bar Chart")

    fig3, ax3 = plt.subplots()
    ax3.barh(y, sales_2023, edgecolor='black')
    ax3.set_yticks(y)
    ax3.set_yticklabels(brands)
    ax3.set_xlabel("Total Sales")
    ax3.set_title("Customized Sales 2023")
    ax3.grid(axis='x', linestyle='--', alpha=0.6)

    for i, v in enumerate(sales_2023):
        ax3.text(v + 5, i, str(v), va='center')

    st.pyplot(fig3)

# =====================
# MULTIPLE CHART
# =====================
elif kategori == "multiple chart":
    st.subheader("Multiple Horizontal Bar Chart")

    fig5, ax5 = plt.subplots()
    ax5.barh(y - bar_width/2, sales_2023, height=bar_width, label='2023')
    ax5.barh(y + bar_width/2, sales_2024, height=bar_width, label='2024')

    ax5.set_yticks(y)
    ax5.set_yticklabels(brands)
    ax5.set_xlabel("Total Sales")
    ax5.set_title("Multiple Horizontal Bar Chart")
    ax5.legend()
    st.pyplot(fig5)

    st.subheader("Multiple Stacked Horizontal Bar Chart")

    fig6, ax6 = plt.subplots()
    ax6.barh(y, sales_2023, label='2023')
    ax6.barh(y, sales_2024, left=sales_2023, label='2024')

    ax6.set_yticks(y)
    ax6.set_yticklabels(brands)
    ax6.set_xlabel("Total Sales")
    ax6.set_title("Multiple Stacked Horizontal Bar Chart")
    ax6.legend()
    st.pyplot(fig6)

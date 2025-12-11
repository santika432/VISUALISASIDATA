import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Data dummy
suhu = [20, 22, 24, 39, 21, 32, 34, 36, 36]
penjualan = [50, 60, 70, 90, 199, 110, 130, 150, 160]
penjualan_weekdays = [69, 70, 30, 150, 100, 60, 70, 80, 90]
penjualan_weekends = [50, 60, 70, 90, 109, 110, 130, 150, 160]

# Data untuk analisis
data = {
    'suhu': [20, 22, 24, 39, 21, 32, 34, 36, 36],
    'penjualan_coklat': [50, 60, 70, 80, 90, 97, 110, 115, 120],
    'penjualan_vanila': [40, 50, 60, 70, 80, 85, 90, 95, 100],
    'penjualan_strobery': [40, 50, 55, 65, 70, 75, 110, 115, 120],
    'kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100],
}
df = pd.DataFrame(data)

# Title
st.title('Analisis Penjualan Es Krim Berdasarkan Suhu')

# Sidebar pilihan grafik
option = st.sidebar.selectbox(
    "Pilih jenis scatter plot",
    ("Basic", "Kustom", "Multiple", "Analisis")
)

st.caption("Praktikum - 5")
st.write("Kelompok : 9")
st.markdown("""
- Santika Sintia Larasati - 0110122045  
- Saepulloh - 0110222183  
- Muhammad Ammar - 0110122308  
""")

# Fungsi plotting
def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title("Hubungan Penjualan Es Krim dan Suhu")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Penjualan Es Krim")
    st.pyplot(fig)

def custom_scatter():
    st.subheader("2. Custom Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolors='black', alpha=0.7)
    ax.set_title("Hubungan Penjualan Es Krim dan Suhu")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Penjualan Es Krim")
    ax.grid(True)
    st.pyplot(fig)

def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='green', s=80, label='Hari Kerja')
    ax.scatter(suhu, penjualan_weekends, color='red', s=80, label='Akhir Pekan')
    ax.set_title("Perbandingan Penjualan Hari Kerja vs Akhir Pekan")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Penjualan Es Krim")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def scatter_3_variabel():
    st.subheader("4. Analisis 3 Variabel")
    jenis = st.selectbox('Pilih jenis es krim', ['coklat', 'vanila', 'strobery'])
    
    if jenis == 'coklat':
        y = df['penjualan_coklat']
    elif jenis == 'vanila':
        y = df['penjualan_vanila']
    else:
        y = df['penjualan_strobery']

    st.dataframe(df)

    fig, ax = plt.subplots()
    scatter = ax.scatter(df['suhu'], y, c=df['kelembapan'], s=100, cmap='coolwarm', alpha=0.7)
    ax.set_title(f'Hubungan Penjualan {jenis} terhadap Suhu & Kelembapan')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel(f'Penjualan Es Krim {jenis}')
    fig.colorbar(scatter, label='Kelembapan (%)')
    st.pyplot(fig)

    st.write(f"Grafik menunjukkan pengaruh **suhu** dan **kelembapan** terhadap penjualan es krim **{jenis}**.")

# Routing
if option == "Basic":
    basic_scatter()
elif option == "Kustom":
    custom_scatter()
elif option == "Multiple":
    multiple_scatter()
elif option == "Analisis":
    scatter_3_variabel()

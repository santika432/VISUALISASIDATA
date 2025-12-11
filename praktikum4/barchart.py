import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


data = {
    'Jurusan': [
        'Teknik informatika',
        'Sistem informasi',
        'Bisnis digital',
    ],
    'Jumlah_Mahasiswa': [120, 150, 80]
}

df = pd.DataFrame(data)
print(df)

#streamlit App
st.title ("Basic Bar Chart - Jumlah Mahasiswa per jurusan")
st.bar_chart (df.set_index('Jurusan'))

#streamlit App
st.title ("Basic Bar chart menggunakan matloplip")
fig, ax = plt.subplots()   # ⬅️ BUKAN plt.subplot()
ax.bar(data['Jurusan'], data['Jumlah_Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

st.pyplot(fig)

#kutomisasi bar chart
st. title("Kustomisasi basic bar chart")
fig, ax = plt.subplots()
colors = ['blue', 'orange', 'red']
bars = ax.bar( data['Jurusan'], data['Jumlah_Mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa per jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Menambahkan nilai pada batang
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, str(bar.get_height()), ha='center')

st.pyplot(fig)

# Judul Dashboard
st.title("Multiple Basic Bar Chart")

# Data tambahan
data_2023 = [120, 150, 100]
data_2024 = [140, 160, 110]

jurusan = data['Jurusan']  # pastikan jumlahnya = 4

x = list(range(len(jurusan)))
width = 0.4

fig, ax = plt.subplots()
bars_2023 = ax.bar(x, data_2023, width=width, label='2023', color='skyblue')
bars_2024 = ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')

ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(jurusan)
ax.legend()

# Menampilkan nilai pada batang 2023 & 2024
for bar in bars_2023:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3, str(bar.get_height()), ha='center')

for bar in bars_2024:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3, str(bar.get_height()), ha='center')

st.pyplot(fig)

#pola dan trend dengan bar chart


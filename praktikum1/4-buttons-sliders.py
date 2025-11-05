#import liberary
import streamlit as st
import pandas as pd #untuk mengelolah data dalam bentuk frame tabel (dataframe)
import numpy as np # untuk memmbuat data numerik
import altair as alt # untuk membuat chart interaktif

st.header("Praktikum1 Visualisasi Data")
st.subheader("Bagian 1: Data element")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)

# Buttons and Sliders 
# Buttons and Sliders dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna untuk 
# berinteraksi dengan aplikasi. Elemen-elemen ini digunakan untuk mengumpulkan input dari 
# pengguna atau mengontrol parameter secara langsung dalam aplikasi Streamlit. 
 
#  Buttons 
# Buttons dalam Streamlit adalah elemen interaktif yang digunakan untuk memicu suatu aksi 
# ketika pengguna mengklik tombol tersebut. Streamlit menyediakan fungsi st.button() untuk 
# membuat tombol.

import streamlit as st
st.title('Creating a Button')
# Defining a Button (Mendefinisikan Tombol)
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

# Radio Buttons 
# Radio Buttons dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna 
# memilih salah satu opsi dari beberapa pilihan yang tersedia. Fungsi st.radio() digunakan 
# untuk membuat radio buttons dalam aplikasi.
import streamlit as st

st.title('Creating Radio Buttons')
# Defining Radio Button (Mendefinisikan Tombol Radio)
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others')
)

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")
#     Check Boxes 
# Check Boxes dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna 
# untuk memilih atau tidak memilih opsi tertentu. Fungsi ini diimplementasikan melalui 
# st.checkbox() dan mengembalikan nilai Boolean (True jika dipilih, False jika tidak dipilih).

import streamlit as st

st.title('Creating Checkboxes')
st.write('Select your Hobies:')
# Defining Checkboxes (Mendefinisikan Kotak Centang)
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

# Drop-Downs 
# Drop-Downs dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna 
# memilih satu opsi dari daftar pilihan yang tersedia. Elemen ini dibuat menggunakan fungsi 
# st.selectbox().
import streamlit as st

st.title('Creating Dropdown')
# Creating Dropdown (Membuat Kotak Pilihan)
hobby = st.selectbox('Choose your hobby: ', 
                     ('Books', 'Movies', 'Sports'))
# Multiselects  
# Modul 1: Streamlit - 1 
# Multiselects dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna 
# memilih beberapa opsi dari daftar yang tersedia. Elemen ini dibuat menggunakan fungsi 
# st.multiselect().
import streamlit as st

st.title('Multi-Select')
# Defining Multi_Select with Pre-Selection (Mendefinisikan Multi-Select dengan Pilihan Awal)
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
)
# Download Buttons 
# Download Buttons dalam Streamlit adalah elemen yang memungkinkan pengguna untuk 
# mengunduh file langsung dari aplikasi. Elemen ini dibuat menggunakan fungsi 
# st.download_button(), yang memberikan tombol unduhan dengan opsi file yang dapat 
# disesuaikan.
import streamlit as st

st.title("Download Button")
# Creating Download Button (Membuat Tombol Unduh)
down_btn = st.download_button(
    label="Download Image",
    # Perbaikan: Hapus tanda kutip tunggal ekstra di akhir path
    data=open(r'D:\titip\VISUALSISASI DATA\ASET\monyet.jpg', "rb"),
    file_name="tiger.jpg",
    mime="image/jpg"
)


# Progress Bars 
# Progress Bars dalam Streamlit adalah elemen visual yang digunakan untuk menunjukkan 
# progres atau kemajuan dari suatu proses di aplikasi Anda. Elemen ini dibuat menggunakan 
# fungsi st.progress().
import streamlit as st
import time

st.title('Progress Bar')
# Defining Progress Bar (Mendefinisikan Bilah Kemajuan)
download = st.progress(0)

# Loop untuk mensimulasikan kemajuan
for percentage in range(100):
    time.sleep(0.1)  # Menunggu 0.1 detik untuk simulasi
    download.progress(percentage + 1) # Memperbarui bilah kemajuan
    
st.write('Download Complete') # Pesan setelah kemajuan selesai
# Spinners  
# Modul 1: Streamlit - 1 
# Spinners dalam Streamlit adalah elemen visual yang digunakan untuk memberikan indikasi 
# bahwa suatu proses sedang berlangsung. Spinners membantu pengguna memahami bahwa 
# aplikasi sedang bekerja dan bukan berhenti atau mengalami masalah. Elemen ini dibuat 
# menggunakan fungsi st.spinner(). 
import streamlit as st
import time

st.title('Spinner')
# Defining Spinner (Mendefinisikan Spinner)
with st.spinner('Loading...'):
    time.sleep(5)
    
st.write('Hello Data Scientists')

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

#  Forms 
# Forms dalam Streamlit adalah elemen yang memungkinkan pengguna untuk mengelompokkan 
# berbagai input (seperti teks, angka, checkbox, dan lainnya) dalam satu unit. Elemen ini berguna 
# untuk mengelola pengumpulan data yang melibatkan beberapa input, di mana semua data 
# dikirimkan sekaligus saat formulir diajukan. 

# Text Box 
# Text Box dalam Streamlit adalah elemen input yang memungkinkan pengguna untuk 
# memasukkan teks. Elemen ini dibuat menggunakan fungsi st.text_input(), yang cocok untuk 
# menerima input berupa string dari pengguna.
import streamlit as st
st.title("Text Box")
#creating text box
name=st.text_input("Enter your Name")
st.write("Your Name is",name)
# Creating Text box with 10 as character limit 
name = st.text_input("Enter your Name", max_chars=10) 
password = st.text_input("Enter your password", type='password') 

# Text Area 
# Text Area dalam Streamlit adalah elemen input yang digunakan untuk menerima masukan 
# teks panjang dari pengguna. Elemen ini sangat mirip dengan Text Box (st.text_input()), 
# tetapi dirancang untuk menangani teks yang lebih besar, seperti paragraf, catatan, atau 
# deskripsi panjang. Text Area dibuat menggunakan fungsi st.text_area().

import streamlit as st 
#creating text area
input_text=st.text_area("Enter your Review") 
#printing entered text
st.write(""" you entered: \b""", input_text)

# Number Input 
# Number Input dalam Streamlit adalah elemen input yang memungkinkan pengguna untuk 
# memasukkan angka. Elemen ini dibuat menggunakan fungsi st.number_input(), yang sangat 
# fleksibel dan dapat digunakan untuk angka bulat, desimal, dan rentang nilai tertentu.

import streamlit as st 
#create number input
st.number_input("Ente Your Number")
import streamlit as st 
#create number input
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min value is 0, dn Max value is 10")
st.write("Default value is 5, \n step size value is 2")
st.write("total value after adding number entered with step value is:", num)

# Time 
# Time Input dalam Streamlit adalah elemen input yang memungkinkan pengguna untuk 
# memilih waktu tertentu (jam dan menit). Elemen ini dibuat menggunakan fungsi 
# st.time_input(), yang dirancang untuk mengumpulkan data waktu dengan cepat dan intuitif.
import streamlit as st
st.title("Time")
st.time_input("Select Your Time")

# Date 
# Date Input dalam Streamlit adalah elemen yang memungkinkan pengguna untuk memilih 
# tanggal tertentu melalui antarmuka interaktif. Elemen ini dibuat menggunakan fungsi 
# st.date_input(), yang sangat berguna untuk aplikasi berbasis jadwal, kalender, atau 
# pengumpulan data dengan tanggal. 
import streamlit as st
import datetime
st.title("Date")
# Menampilkan input waktu
st.time_input("Select Time")
# Menampilkan input tanggal
st.date_input(
    "Select Your Date",
    value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),  
    max_value=datetime.date(2005, 12, 1)
)


# Color
# Color Input dalam Streamlit adalah elemen yang memungkinkan pengguna memilih warna 
# melalui antarmuka pemilih warna (color picker). Elemen ini dibuat menggunakan fungsi 
# st.color_picker(), yang mengembalikan nilai warna yang dipilih dalam format HEX. 
import streamlit as st

st.title("Select Color")
# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

# Dataset Upload 
# Dataset Upload dalam Streamlit adalah fitur yang memungkinkan pengguna mengunggah 
# file (seperti dataset) ke aplikasi Streamlit untuk diproses atau dianalisis. Elemen ini dibuat 
# menggunakan fungsi st.file_uploader(), yang sangat fleksibel dalam mendukung berbagai 
# format file.

import streamlit as st
import pandas as pd

st.title("CSV Data")
data_file = st.file_uploader("Upload CSV",type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,
                        "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)   
else:
    st.write("No CSV File is Uploaded")
#     Submit Button 
# Submit Button dalam Streamlit adalah elemen yang digunakan untuk mengirimkan atau 
# memproses data dalam sebuah formulir (form). Submit Button bekerja secara eksklusif di 
# dalam elemen Form Streamlit, yang memastikan bahwa data dari semua input yang ada 
# dalam form hanya akan diproses saat pengguna mengklik tombol submit.

import streamlit as st
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')
st.write(a)
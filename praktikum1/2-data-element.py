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
#DATAFRAME : struktur data berbentuk tabel (baris dan kollom) yang dissediakan oleh liberary pandas
st.subheader("DataFrame")
df=pd.DataFrame(
    np.random.randn(30,10), 
    columns=('col_no %d' % i for i in range (10))
)
#menampilkan dataframe
st.dataframe(df)

#highlight nilai minimum 
st.subheader("Highligt Minimum Value di DataFrame")
#highlight nilai terkecil disetiiap kolom dataframe 
#axis=0 bekerja per kolom 
st.dataframe(df.style.highlight_min(axis=0))

#tabel ststis
st.subheader("Tabel Statis")
df= pd.DataFrame(
   np.random.randn(30,10), 
    columns=('col_no %d' % i for i in range (10))
)
st.table(df)
# METRICS : komponen tampilan angka penting
st.subheader("metrics")
#menampilkan metrik tunggal ( nilai utama+ perubahan nilai)
st.metric(label= "temperature", value = "31 C,", delta="1,2,3 C") #kenaikan 1.2.C

#METRIC sesuai dengan delta_color
#delta_color digunakan untuk warna sesuai perubahan : 
#-normal (default) : naik  -> label warna hijau, turun -> label merah
# "invers" : kebalikan (naik-> turun)

#definisi variabel metrics
#Menampilkan indikator
col1, col2, col3 = st.columns(3)

col1.metric("Curah Hujan", "100 cm", "10 cm")
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar",
            delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta=10,
            delta_color="off")

#Menampilkan  metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0)
#karena di setting default
st.metric("Trees", "91456","-1132649") # penurunan

#The write() Fungticion The write( )as a Superfunction 
import streamlit as st 
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns= ('col_no %d'% i for i in range (10)))
#mendefinisikan banyak argumen dalam fungsi tulis
st.write('Ini data kami')
st.write(df)
st.write('Data dalam format dataframe.\nTulis adalah fungsi super.')
#import perpustakaan yang di perlukan

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# Membuat data acak
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)
# Membuat chart batang
chart = alt.Chart(df).mark_bar().encode(
    x='a',
    y='b',
    tooltip=['a', 'b']
)
# Menampilkan chart di Streamlit
st.write(chart)
#Magic adalah Magic dalam Streamlit adalah fitur unik yang memungkinkan Anda menambahkan elemen teks atau kode secara langsung ke dalam file Python tanpa memerlukan fungsi eksplisit seperti st.write(). 
# Dengan kata lain, Magic membuat kode lebih bersih dan sederhana karena Streamlit secara otomatis menangani perintah untuk menampilkan elemen.
# Math calculations with no functions defined
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Magic - perhitungan sederhana
"Adding 5 & 4"
5 + 4
# Memajang variabel 'a'
a = 5
"a"
a
# Magic Markdown
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""
# DataFrame menggunakan Magic
df = pd.DataFrame({'col': [1, 2]})
"DataFrame"
df
# Membuat chart menggunakan Magic
s = np.random.logistic(10, 5, size=100)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
"Chart"
chart

import streamlit as st
import pandas as pd
#membuat data acak
import numpy as np


st.title("Containers")
st.write("Kelompok : 9")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)

#Untuk memasukkan lebih dari satu elemen, kita dapat menggunakan container dalam  Streamlit. Container bersifat tidak terlihat secara alami dan dapat didefinisikan dengan  st.container(). 

import streamlit as st
import numpy as np
st.title("Container")
with st.container():
    st.write("Element Inside Contianer")
#Defining Chart Element
st.line_chart(np.random.randn(40, 4))
st.write("Element Outside Container")
#Kita dapat memasukkan elemen-elemen dalam container tanpa urutan, yang dapat dilakukan  dengan menggunakan fungsi container.write().
import streamlit as st
import numpy as np
st.title("Out of Order Container")
#Defining Contianers
container_one = st.container()
container_one.write("Element One Inside Contianer")
st.write("Element Outside Contianer")
#Now insert few more elements in the container_one
container_one.write("Element Two Inside Contianer")
container_one.line_chart(np.random.randn(48, 4))
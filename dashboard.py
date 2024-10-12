import streamlit as st
from PIL import Image

# Set judul atau heading
st.title("Permintaan Maaf untuk Fadiyah Nur Aulia Sari")

# Navbar heading (opsional)
# Sidebar
with st.sidebar:
    st.title("Maafkan Akbar ya, yang egois ini dan suka marah-marah")
    image_path = "8.jpg"
    st.image(image_path, use_column_width=True)
    st.write("07 Maret 2023-Now. Berlanjut lagi mungkin?🤷‍♂️")
    

# Tambahkan deskripsi atau pesan
st.write("""
Fadiyah Nur Aulia Sari yang termanis dan cantik, Seleb timika dengan 2k followers, seleb tiktok, pintar masak, suka semua makanan.  
Akbar mau minta maaf ya, perihal kamu mau tunggu saya berubah atau tidak itu hak ta beb, tapi mauja minta maaf.
Semua hal sudah dilewati beb, makan, mandi, tidur, pergi keluar kota, kemanapun sudah banyak yang dilalui sama-sama. 
Bukannya mau ku paksa ki untuk pertahankan tapi ya mauja minta maaf. 
Karena biarpun bagaimana, kau masih tetap orang yang paling ku sayang saat ini. I love You Pia ❤❤😊
""")

# Nama file gambar
image1 = "1.jpg"
image2 = "16.jpg"
image3 = "17.jpg"
image4 = "4.jpg"
image5 = "5.jpg"
image6 = "6.png"
image7 = "7.jpg"
image9 = "9.jpg"
image10 = "10.jpg"
image11 = "11.jpg"
image12 = "12.jpg"
image13 = "13.jpg"


# Tambahkan gambar dengan kolom
col1, col2, col3 = st.columns(3)
with col1:
    st.image(image1, use_column_width=True)
with col2:
    st.image(image2, use_column_width=True)
with col3:
    st.image(image3, use_column_width=True)
    
col4, col5, col6 = st.columns(3)
with col4:
    st.image(image4, use_column_width=True)
with col5:
    st.image(image5, use_column_width=True)
with col6:
    st.image(image6, use_column_width=True)

col7, col8, col9 = st.columns(3)
with col7:
    st.image(image7, use_column_width=True)
with col8:
    st.image(image9, use_column_width=True)
with col9:
    st.image(image10, use_column_width=True)

col10, col11, col12 = st.columns(3)
with col10:
    st.image(image11, use_column_width=True)
with col11:
    st.image(image12, use_column_width=True)
with col12:
    st.image(image13, use_column_width=True)
    
# Tambahkan footer
st.write("""
Maafkan Akbar ya, yang egois ini dan suka marah-marah
""")

#Membuat festack dengan menggunakan linked list
import streamlit as st
import stack 

# Konfigurasi halaman
st.set_page_config(page_title="📊 Stack Visualization", layout="wide")

st.title("📊 Visualisasi Stack")

# Inisialisasi Stack dalam session state
if 'stack' not in st.session_state:
    st.session_state.stack = stack.Stack()

# Layout Kolom
col1, col2 = st.columns(2)

# Form input
with col1:
    st.subheader("Input Data")
    data_input = st.text_input("Masukkan Data")
    if st.button("Push"):
        if data_input:
            st.session_state.stack.push(data_input)
            st.success(f"Data '{data_input}' berhasil ditambahkan")
        else:
            st.warning("Masukkan data terlebih dahulu")


# Tombol Pop
with col2:
    st.subheader("Operasi Stack")

    if st.button("Pop"):
        popped_data = st.session_state.stack.pop()
        if popped_data:
            st.success(f"Data '{popped_data}' berhasil dihapus")
        else:
            st.warning("Stack kosong")
    
    if st.button("Peek"):
        peeked_data = st.session_state.stack.peek()
        if peeked_data:
            st.success(f"Data teratas: '{peeked_data}'")
        else:
            st.warning("Stack kosong")

# Menampilkan Visualisasi Stack
st.subheader("Visualisasi Stack")
if st.session_state.stack.is_empty():
    st.info("Stack kosong")
else:
    # Mengambil data untuk visualisasi
    stack_data = []
    current = st.session_state.stack.top
    while current:
        stack_data.append(current.data)
        current = current.next

    # Render kotak visualisasi
    cols = st.columns(len(stack_data))
    for i, data in enumerate(stack_data):
        with cols[i]:
            st.markdown(f"""
                <div style='border: 2px solid #4CAF50; padding: 10px; 
                text-align: center; background-color: #f0f9fe; border-radius: 5px;'>
                    {data}
                </div>
                """, unsafe_allow_html=True)
            if i == 0:
                st.markdown("<div style='text-align: center; margin-top: 5px;'><b>TOP</b></div>", unsafe_allow_html=True)
    
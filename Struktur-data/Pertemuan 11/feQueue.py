# Membuat feQueue dari linked list
# pancingan hijau github
from gtts import gTTS
import streamlit as st

# 1. Membuat Struktur Node untuk Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 2. Membuat Struktur Queue Menggunakan Linked List
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def get_all_items(self):
        items = []
        current = self.front
        while current:
            items.append(current.data)
            current = current.next
        return items

# 3. Implementasi ke Aplikasi Antrian Klinik Streamlit
st.title("Aplikasi Antrian Klinik Sederhana")
st.write("Menggunakan Struktur Data Queue Berbasis Linked List")

if "klinik_queue" not in st.session_state:
    st.session_state.klinik_queue = LinkedQueue()

input_antrian = st.text_input("Masukkan nama pasien:")
if st.button("Tambah Antrian"):
    if input_antrian.strip() != "":
        st.session_state.klinik_queue.enqueue(input_antrian)
        st.success(f"Pasien '{input_antrian}' berhasil ditambahkan ke antrian!")
    else:
        st.warning("Nama pasien tidak boleh kosong!")

st.subheader("Daftar Antrian Saat Ini")
daftar_pasien = st.session_state.klinik_queue.get_all_items()

if len(daftar_pasien) == 0:
    st.info("Belum ada antrian pasien.")
else:
    for indeks, nama in enumerate(daftar_pasien, start=1):
        st.write(f"Antrian ke-{indeks} : {nama}")

st.subheader("Panggil Pasien")
if st.button("Panggil Antrian Berikutnya"):
    pasien_dipanggil = st.session_state.klinik_queue.dequeue()
    if pasien_dipanggil:
        st.success(f"Memanggil Antrian: {pasien_dipanggil}")
        teks_panggilan = f"Memanggil pasien, {pasien_dipanggil}. Silakan menuju ruang periksa."
        tts = gTTS(text=teks_panggilan, lang="id")
        tts.save("panggilan_klinik.mp3")
        st.audio("panggilan_klinik.mp3", autoplay=True)
        st.rerun()
    else:
        st.error("Antrian sudah kosong!")

        # pancingan kode baru biar github menyala hijau cerah penuh
print("Sistem Antrian Klinik Nahdiya Sukses Terupdate!")
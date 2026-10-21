import streamlit as st
import pandas as pd

# Konfigurasi Halaman (Prinsip HCI: Tampilan bersih dan rapi)
st.set_page_config(page_title="Dashboard Penjualan", layout="centered")

st.title("📊 Dashboard Eksekutif Penjualan Bulanan")
st.write("Contoh penerapan Analitik, Data Visualization, dan HCI menggunakan Python.")

# 1. Menyiapkan Data Mentah (Simulasi Data)
data = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni'],
    'Penjualan (Juta Rp)': [65, 59, 80, 81, 56, 109],
    'Keuntungan (Juta Rp)': [20, 15, 30, 32, 18, 45]
}
df = pd.DataFrame(data)

# 2. Ringkasan Utama di Bagian Atas (Prinsip HCI: Informasi penting terlihat sekilas)
st.markdown("### Ringkasan Eksekutif")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Penjualan Semester Ini", value="450 Juta Rp")
with col2:
    st.metric(label="Penjualan Tertinggi", value="109 Juta Rp (Juni)")

st.markdown("---")

# 3. Visualisasi Data (Grafik Bawaan Streamlit)
st.subheader("Grafik Tren Penjualan Bulanan")
st.write("Menggunakan grafik garis untuk melihat kenaikan dan penurunan dari bulan ke bulan.")
st.line_chart(df.set_index('Bulan')['Penjualan (Juta Rp)'])

# 4. Fitur Interaktif (Filter Data sesuai kebutuhan pengguna/HCI)
st.subheader("Detail Data Tabel")
pilihan_bulan = st.selectbox("Pilih Bulan untuk Melihat Detail:", df['Bulan'])

# Menampilkan baris data yang dipilih pengguna
data_terpilih = df[df['Bulan'] == pilihan_bulan]
st.dataframe(data_terpilih)
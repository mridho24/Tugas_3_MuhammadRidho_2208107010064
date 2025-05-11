# Rock-Paper-Scissors Classification Project 🪨📄✂

---

## 📚 Deskripsi Proyek

Proyek ini bertujuan untuk membangun sistem klasifikasi gambar sederhana menggunakan _Deep Learning_ dengan arsitektur _Transfer Learning_ (menggunakan MobileNetV2).  
Gambar yang diklasifikasikan terdiri dari tiga kategori: _Rock, **Paper, dan **Scissors_.

Model yang dilatih kemudian akan diintegrasikan ke dalam aplikasi backend berbasis _FastAPI_, sehingga bisa menerima gambar dan memberikan hasil prediksi secara real-time.

---

## 🛠 Teknologi yang Digunakan

- _TensorFlow / Keras_ — Untuk membangun dan melatih model klasifikasi gambar.
- _FastAPI_ — Untuk membangun backend REST API.
- _Uvicorn_ — Sebagai ASGI server untuk menjalankan FastAPI.
- _PIL (Pillow)_ — Untuk memproses gambar.
- _NumPy_ — Untuk manipulasi data numerik.
- _scikit-learn_ — Untuk evaluasi model (classification report, confusion matrix).

---

## 📂 Struktur Folder Proyek

project-root/
├── backend/
│ └── main.py # Kode backend FastAPI
├── model/
│ └── best_transfer.h5 # Model hasil training yang disimpan
├── dataset/
│ ├── rock/
│ ├── paper/
│ └── scissor/
├── README.md
└── requirements.txt

---

## 🚀 Langkah Penggunaan

### 1. Clone Repository

git clone https://github.com/furqanx/Tugas-Pembelajaran-Mesin.git <br>
cd Tugas-Pembelajaran-Mesin

### 2. Siapkan Environment Python

Disarankan menggunakan _Python 3.9–3.11_.

Buat environment baru, lalu install dependencies:

pip install -r requirements.txt

### 3. Download Dataset

Unduh dataset Rock-Paper-Scissors dari Kaggle:  
🔗 [Rock-Paper-Scissors Dataset – Kaggle](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors)

Setelah download dan ekstrak:

- Susun dataset ke dalam folder:

dataset/
rock/
paper/
scissor/

### 4. Jalankan Backend FastAPI

Masuk ke folder frontend/, lalu jalankan:

streamlit run app.py

Streamlit akan berjalan di http://localhost:8501/

Kemudian, masuk ke folder backend/, lalu jalankan:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Server akan berjalan di http://localhost:8000/.

### 5. Mengerjakan Tugas Praktikum

Praktikan diminta untuk:

- Melengkapi beberapa bagian kode yang kosong (TODO) sesuai dengan instruksi di notebook dan file main.py.
- Memastikan bahwa preprocessing saat inferensi _konsisten_ dengan preprocessing saat training.
- Melakukan eksperimen kecil (augmentasi, tuning hyperparameter) untuk meningkatkan performa model.

---

## 🎯 Tujuan Pembelajaran

- Memahami alur kerja training dan deployment model machine learning.
- Membiasakan diri mengintegrasikan model ke dalam aplikasi backend nyata.
- Melatih kerapihan penyusunan struktur proyek dan dokumentasi.

---

## 📋 Catatan Penting

- Pastikan struktur dataset rapi dan sesuai.
- Pastikan preprocessing konsisten antara training dan backend inference.
- Jangan lupa untuk mengisi seluruh bagian TODO yang ada dalam kode.

---

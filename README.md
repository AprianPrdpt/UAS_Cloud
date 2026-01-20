- Nama  : Aprian Pradipta E S
- Nim   : 235510008
- Prodi : Teknik Komputer S1
- Matkul: Komputasi Paralel Pada CLOUD COMPUTING

# FastAPI Sensor API (Dockerized)

Repository ini berisi aplikasi **FastAPI sederhana** yang digunakan untuk menampilkan data sensor (suhu dan kelembaban) dari beberapa laboratorium. Proyek ini dibuat sebagai bagian dari **UAS Mata Kuliah Cloud Computing** dan difokuskan pada proses *containerization* menggunakan **Docker**.

---

## 📌 Deskripsi Singkat

Aplikasi ini menyediakan REST API berbasis FastAPI yang mengembalikan data sensor dalam format **JSON**. Data yang ditampilkan berupa **data statis** dan digunakan untuk keperluan pengujian layanan API serta implementasi Docker.

---

## 🛠️ Teknologi yang Digunakan

* Python 3.11
* FastAPI
* Uvicorn
* Docker

---

## 📂 Struktur Folder

```
UAS_Cloud/
├── app/
│ ├── main.py
│ ├── database.py
│ └── init_db.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
```

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Build Docker Image

```bash
docker build -t fastapi-sensor .
```

### 2. Menjalankan Container

```bash
docker run -p 8000:8000 fastapi-sensor
```

### 3. Akses API

Buka browser atau tools seperti Postman dan akses:

```
http://localhost:8000/sensor
```

---

## 📤 Output API

Berikut adalah contoh data JSON yang dihasilkan oleh endpoint `/sensor`:

```
[
  {"lokasi":"Lab A","suhu":26.5,"kelembaban":60,"waktu":"2025-01-01"},
  {"lokasi":"Lab B","suhu":27.1,"kelembaban":62,"waktu":"2025-01-01"},
  {"lokasi":"Lab C","suhu":25.8,"kelembaban":58,"waktu":"2025-01-01"},
  {"lokasi":"Lab A","suhu":26.9,"kelembaban":61,"waktu":"2025-01-01"},
  {"lokasi":"Lab B","suhu":27.3,"kelembaban":63,"waktu":"2025-01-01"}
]
```

---

## ℹ️ Catatan

* Aplikasi ini menggunakan database SQLite lokal
* Fokus utama proyek adalah memastikan API dapat berjalan dengan baik di dalam container Docker.


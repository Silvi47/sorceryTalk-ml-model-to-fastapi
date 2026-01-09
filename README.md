# sorceryTalk-ml-model-to-fastapi
Source code webinar Sorcery Talk pada tanggal 9 Januari 2026

Repository ini adalah template sederhana yang dirancang untuk pemula yang ingin belajar cara mengintegrasikan model Machine Learning (**TensorFlow**) ke dalam REST API modern yang cepat menggunakan **FastAPI**.

Proyek ini dibuat sesederhana mungkin agar mudah dipahami.

---

## 📋 Prasyarat

Sebelum memulai, pastikan komputer Anda sudah terinstal:

1.  **Python 3.8+** (Disarankan Python 3.9 atau 3.10 agar kompatibel dengan TensorFlow terbaru).
2.  **Git** (Untuk meng-clone repository).

---

## 🛠️ Cara Instalasi

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputer lokal Anda:

### 1. Clone Repository
Buka terminal (Command Prompt/PowerShell/Terminal) dan jalankan perintah:

```bash
git clone https://github.com/Silvi47/sorceryTalk-ml-model-to-fastapi.git
cd sorceryTalk-ml-model-to-fastapi
```

### 2. Buat Virtual Environment (Sangat Disarankan!)
Agar library tidak bentrok dengan proyek lain, kita gunakan Virtual Environment.

Untuk Windows:

```bash
python -m venv venv
venv\Scripts\activate
Untuk Mac / Linux:
```

```bash
python3 -m venv venv
source venv/bin/activate
```

**Tanda Sukses:** Jika berhasil, Anda akan melihat tulisan (venv) di sebelah kiri baris perintah terminal Anda.

### 3. Install Dependencies
Install library FastAPI, Uvicorn, dan TensorFlow yang sudah didaftarkan di file requirements.txt:

```bash
pip install -r requirements.txt
```

**Catatan:** Proses ini mungkin memakan waktu beberapa menit karena ukuran library TensorFlow cukup besar.

## Cara Menjalankan Aplikasi
Setelah instalasi selesai, jalankan server lokal dengan perintah berikut:

```bash
fastapi dev main.py
```

## Akses Dokumentasi API
FastAPI menyediakan dokumentasi otomatis yang sangat membantu. Buka browser dan kunjungi:
**Swagger UI (Interaktif):** http://127.0.0.1:8000/docs

Di sini Anda bisa mencoba langsung endpoint API (Try it out).
**ReDoc (Alternatif):** http://127.0.0.1:8000/redoc


Sekian. Semoga bermanfaat!

Copyright Silvia Larasatul

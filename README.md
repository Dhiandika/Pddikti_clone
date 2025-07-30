# 🎓 PDDIKTI Clone - Sistem Pencarian Data Mahasiswa & Dosen

## 📋 Deskripsi Proyek

**PDDIKTI Clone** adalah aplikasi web yang menyediakan akses ke data mahasiswa, dosen, perguruan tinggi, dan program studi melalui API PDDIKTI (Pangkalan Data Pendidikan Tinggi). Aplikasi ini dibangun menggunakan Flask dan menyediakan antarmuka yang user-friendly untuk pencarian dan melihat detail informasi akademik.

### 🌟 Fitur Utama

- **🔍 Pencarian Mahasiswa**: Mencari data mahasiswa berdasarkan nama atau NIM
- **👨‍🏫 Pencarian Dosen**: Mencari data dosen berdasarkan nama atau NIDN
- **🏫 Pencarian Perguruan Tinggi**: Mencari data universitas/PT
- **📚 Pencarian Program Studi**: Mencari data program studi
- **📊 Detail Lengkap**: Melihat informasi detail mahasiswa dan dosen
- **⚡ Loading System**: Sistem loading untuk API dengan latency tinggi
- **🎨 UI Modern**: Antarmuka yang responsif dan modern

### 🛠️ Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: Font Awesome
- **API**: PDDIKTI API via pddiktipy library
- **Database**: Tidak diperlukan (menggunakan API eksternal)

## 📦 Instalasi

### Prasyarat

- Python 3.7 atau lebih baru
- pip (Python package installer)

### Langkah Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/pddikti-clone.git
   cd pddikti-clone
   ```

2. **Buat Virtual Environment (Opsional tapi Direkomendasikan)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi**
   ```bash
   python run.py
   ```

5. **Akses Aplikasi**
   Buka browser dan kunjungi: `http://localhost:5000`

## 🚀 Cara Penggunaan

### 1. Halaman Beranda
- **Quick Search**: Pencarian cepat di bagian hero
- **Menu Pencarian**: Pilih jenis pencarian (Mahasiswa, Dosen, PT, Program Studi)
- **Fitur Unggulan**: Lihat fitur-fitur aplikasi
- **Statistik**: Informasi statistik data

### 2. Pencarian Mahasiswa
1. Klik menu "Mahasiswa" di beranda
2. Masukkan nama mahasiswa (contoh: "Ilham Riski Wibowo")
3. Klik tombol "Cari"
4. Pilih salah satu hasil pencarian
5. Klik "Detail" untuk informasi dasar atau "Detail Lengkap (Direct)" untuk informasi lengkap

### 3. Pencarian Dosen
1. Klik menu "Dosen" di beranda
2. Masukkan nama dosen atau NIDN
3. Klik tombol "Cari"
4. Pilih hasil pencarian
5. Klik "Lihat Detail" untuk informasi lengkap dosen

### 4. Pencarian Perguruan Tinggi
1. Klik menu "Perguruan Tinggi" di beranda
2. Masukkan nama universitas
3. Klik tombol "Cari"
4. Lihat hasil pencarian

### 5. Pencarian Program Studi
1. Klik menu "Program Studi" di beranda
2. Masukkan nama program studi
3. Klik tombol "Cari"
4. Lihat hasil pencarian

## 📁 Struktur Proyek

```
pddikti-clone/
├── app/
│   ├── __init__.py
│   ├── route.py              # Route definitions
│   ├── static/               # Static files (CSS, JS, images)
│   └── templates/            # HTML templates
│       ├── base.html         # Base template
│       ├── home.html         # Home page
│       ├── search_mahasiswa.html
│       ├── search_dosen.html
│       ├── search_pt.html
│       ├── search_prodi.html
│       ├── detail_mahasiswa.html
│       ├── detail_mahasiswa_full.html
│       ├── detail_dosen.html
│       ├── debug.html
│       └── debug_detail.html
├── requirements.txt          # Python dependencies
├── run.py                   # Application entry point
├── API_DOCUMENTATION.md     # API documentation
└── README.md               # This file
```

## 🔧 Konfigurasi API

### API Endpoints yang Digunakan

1. **Search Mahasiswa**
   ```
   GET /search_mahasiswa?keyword={nama}
   ```

2. **Detail Mahasiswa Lengkap**
   ```
   GET /mahasiswa/{nim}/perguruan_tinggi/{npsn}/prodi/{kode_prodi}/detail_mahasiswa
   ```

3. **Search Dosen**
   ```
   GET /search_dosen?keyword={nama}
   ```

4. **Detail Dosen**
   ```
   GET /dosen/{dosen_id}/profile
   GET /dosen/{dosen_id}/penelitian
   GET /dosen/{dosen_id}/pengabdian
   GET /dosen/{dosen_id}/karya
   GET /dosen/{dosen_id}/paten
   GET /dosen/{dosen_id}/study_history
   GET /dosen/{dosen_id}/teaching_history
   ```

### Parameter API

- **nim**: Nomor Induk Mahasiswa
- **npsn**: Nomor Pokok Sekolah Nasional (ID universitas)
- **kode_prodi**: Kode program studi
- **dosen_id**: ID dosen

## 🎨 Fitur UI/UX

### Loading System
- **Progress Bar**: Animasi progress untuk API calls
- **Loading Overlay**: Full-screen loading dengan spinner
- **User Feedback**: Pesan informatif tentang waktu tunggu
- **Error Handling**: Pesan error yang jelas dan informatif

### Responsive Design
- **Mobile-Friendly**: Tampilan optimal di semua device
- **Bootstrap 5**: Framework CSS modern
- **Card Layout**: Tampilan card yang rapi
- **Icon Integration**: Font Awesome icons

## 🐛 Debugging

### Debug Routes
- **`/debug_search/<keyword>`**: Debug pencarian
- **`/debug_detail/<mahasiswa_id>`**: Debug detail mahasiswa
- **Debug Button**: Tombol debug di setiap hasil pencarian

### Error Handling
- **ValidationError**: Error validasi input
- **APIConnectionError**: Error koneksi API
- **None Response**: Handling response kosong
- **Missing Fields**: Handling field yang tidak ada

## 📸 Screenshots

### Halaman Beranda
[Screenshot beranda akan ditambahkan di sini]

### Halaman Pencarian Mahasiswa
[Screenshot pencarian mahasiswa akan ditambahkan di sini]

### Halaman Detail Mahasiswa
[Screenshot detail mahasiswa akan ditambahkan di sini]

### Halaman Detail Dosen
[Screenshot detail dosen akan ditambahkan di sini]

## 🔄 Update dan Maintenance

### Menambah Fitur Baru
1. Tambahkan route di `app/route.py`
2. Buat template HTML di `app/templates/`
3. Update navigasi di `base.html`
4. Test fitur baru

### Debugging API Issues
1. Gunakan debug routes untuk inspect response
2. Check console logs untuk error details
3. Verify API parameters dengan dokumentasi
4. Test dengan Postman untuk konfirmasi

## 🤝 Kontribusi

1. Fork repository
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## 📞 Kontak

- **Developer**: [Nama Developer]
- **Email**: [email@example.com]
- **GitHub**: [github.com/username]

## 🙏 Ucapan Terima Kasih

- **PDDIKTI**: Untuk menyediakan API data pendidikan tinggi
- **Flask**: Framework web yang powerful
- **Bootstrap**: Framework CSS yang responsif
- **Font Awesome**: Icon library yang lengkap

---

**⚠️ Catatan**: Aplikasi ini menggunakan API eksternal PDDIKTI. Performa dan ketersediaan data bergantung pada server PDDIKTI. API calls mungkin memakan waktu 10-15 detik karena latency server.


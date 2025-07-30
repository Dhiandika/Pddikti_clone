# 🚀 Panduan Instalasi PDDIKTI Clone

## 📋 Prasyarat

Sebelum menginstal aplikasi, pastikan sistem Anda memenuhi persyaratan berikut:

### Sistem Operasi
- ✅ Windows 10/11
- ✅ macOS 10.14+
- ✅ Ubuntu 18.04+ / Debian 9+

### Software yang Diperlukan
- **Python 3.7 atau lebih baru**
- **pip** (Python package installer)
- **Git** (untuk clone repository)

### Cek Versi Python
```bash
python --version
# atau
python3 --version
```

## 🔧 Langkah Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/username/pddikti-clone.git
cd pddikti-clone
```

### 2. Buat Virtual Environment (Direkomendasikan)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
python run.py
```

### 5. Akses Aplikasi
Buka browser dan kunjungi: `http://localhost:5000`

## 🐛 Troubleshooting

### Error: "Python not found"
**Solusi:**
```bash
# Windows
python --version
# Jika tidak ada, download dari python.org

# macOS
brew install python3

# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip
```

### Error: "pip not found"
**Solusi:**
```bash
# Windows
python -m ensurepip --upgrade

# macOS
brew install python3

# Ubuntu/Debian
sudo apt install python3-pip
```

### Error: "Module not found"
**Solusi:**
```bash
# Pastikan virtual environment aktif
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install ulang dependencies
pip install -r requirements.txt
```

### Error: "Port already in use"
**Solusi:**
```bash
# Cek port yang digunakan
netstat -ano | findstr :5000

# Kill process yang menggunakan port 5000
# Atau gunakan port berbeda
python run.py --port 5001
```

## 📦 Dependencies

### Dependencies Utama
- **Flask**: Web framework
- **pddiktipy**: PDDIKTI API wrapper
- **requests**: HTTP library

### Dependencies Development (Opsional)
- **pytest**: Testing framework
- **black**: Code formatter
- **flake8**: Linter

## 🔧 Konfigurasi

### Environment Variables (Opsional)
Buat file `.env` di root directory:
```env
FLASK_ENV=development
FLASK_DEBUG=1
API_KEY=your_api_key_here
```

### Konfigurasi Database (Jika diperlukan)
Saat ini aplikasi tidak menggunakan database lokal karena menggunakan API eksternal.

## 🚀 Deployment

### Local Development
```bash
python run.py
```

### Production (Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Docker (Opsional)
```bash
# Build image
docker build -t pddikti-clone .

# Run container
docker run -p 5000:5000 pddikti-clone
```

## 📝 Catatan Penting

1. **API Latency**: API PDDIKTI memiliki latency tinggi (10-15 detik)
2. **Internet Connection**: Pastikan koneksi internet stabil
3. **API Limits**: Perhatikan batasan rate limit dari API
4. **Error Handling**: Aplikasi sudah dilengkapi dengan error handling yang baik

## 🆘 Support

Jika mengalami masalah:

1. **Cek Logs**: Lihat output di terminal untuk error messages
2. **Debug Mode**: Gunakan debug routes di aplikasi
3. **API Status**: Pastikan API PDDIKTI berfungsi normal
4. **Documentation**: Lihat README.md dan API_DOCUMENTATION.md

## 📞 Kontak

- **Email**: [email@example.com]
- **GitHub Issues**: [github.com/username/pddikti-clone/issues]
- **Documentation**: Lihat file README.md

---

**⚠️ Disclaimer**: Aplikasi ini menggunakan API eksternal PDDIKTI. Performa dan ketersediaan data bergantung pada server PDDIKTI. 
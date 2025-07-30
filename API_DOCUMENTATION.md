# 📚 API Documentation - PDDIKTI Clone

## 🔗 API Endpoints Overview

### Base URL
```
https://devsuperapp-api.dikti.go.id/v2/pddikti/
```

### Authentication
```
x-api-key: ace3758228c2a9ce6d62a223dce9151a7fcd11c52b33e3785883044adb07b446
```

## 👨‍🎓 Mahasiswa (Student) APIs

### 1. Search Mahasiswa
**Endpoint:** `GET /search_mahasiswa`
**Description:** Mencari mahasiswa berdasarkan nama atau NIM
**Parameters:**
- `keyword` (string): Nama mahasiswa atau NIM

**Example Request:**
```python
with api() as client:
    result = client.search_mahasiswa('Ilham Riski Wibowo')
```

**Response Fields:**
- `id`: ID unik mahasiswa
- `nama`: Nama lengkap mahasiswa
- `nim`: Nomor Induk Mahasiswa
- `nama_pt`: Nama perguruan tinggi
- `npsn`: Nomor Pokok Sekolah Nasional (ID universitas)
- `kode_prodi`: Kode program studi
- `nama_prodi`: Nama program studi

### 2. Detail Mahasiswa Lengkap
**Endpoint:** `GET /mahasiswa/{nim}/perguruan_tinggi/{npsn}/prodi/{kode_prodi}/detail_mahasiswa`
**Description:** Mendapatkan detail lengkap mahasiswa
**Parameters:**
- `nim` (string): Nomor Induk Mahasiswa
- `npsn` (string): Nomor Pokok Sekolah Nasional
- `kode_prodi` (string): Kode program studi

**Example Request:**
```python
with api() as client:
    detail = client.get_detail_mhs('200030515', '082010', '57201')
```

**Response Fields:**
- `mahasiswa.id`: ID unik mahasiswa
- `mahasiswa.nama`: Nama lengkap mahasiswa
- `mahasiswa.nik`: Nomor Induk Kependudukan
- `mahasiswa.jenis_kelamin`: Jenis kelamin (L/P)
- `mahasiswa.tgl_lahir`: Tanggal lahir
- `mahasiswa.tempat_lahir`: Tempat lahir
- `mahasiswa.alamat`: Alamat lengkap
- `mahasiswa.telepon`: Nomor telepon
- `mahasiswa.handphone`: Nomor handphone
- `mahasiswa.email`: Alamat email
- `mahasiswa.agama`: Informasi agama
- `mahasiswa.kewarganegaraan`: Kewarganegaraan
- `mahasiswa.terdaftar`: Data pendaftaran
  - `nim`: NIM mahasiswa
  - `nama_pt`: Nama perguruan tinggi
  - `nama_prodi`: Nama program studi
  - `tgl_masuk`: Tanggal masuk
  - `ipk`: Indeks Prestasi Kumulatif
  - `jenjang_didik`: Jenjang pendidikan
- `mahasiswa.last_update`: Tanggal update terakhir
- `mahasiswa.ibu_kandung`: Nama ibu kandung

## 👨‍🏫 Dosen (Lecturer) APIs

### 1. Search Dosen
**Endpoint:** `GET /search_dosen`
**Description:** Mencari dosen berdasarkan nama atau NIDN
**Parameters:**
- `keyword` (string): Nama dosen atau NIDN

**Example Request:**
```python
with api() as client:
    result = client.search_dosen('Prof. Dr. Ilham')
```

**Response Fields:**
- `id`: ID unik dosen
- `nama`: Nama lengkap dosen
- `nidn`: Nomor Induk Dosen Nasional
- `nama_pt`: Nama perguruan tinggi
- `singkatan_pt`: Singkatan perguruan tinggi
- `nama_prodi`: Nama program studi

### 2. Detail Dosen - Profile
**Endpoint:** `GET /dosen/{dosen_id}/profile`
**Description:** Mendapatkan profil lengkap dosen
**Parameters:**
- `dosen_id` (string): ID dosen

**Response Fields:**
- `nama_dosen`: Nama lengkap dosen
- `nidn`: Nomor Induk Dosen Nasional
- `jabatan_akademik`: Jabatan akademik
- `pendidikan_tertinggi`: Pendidikan terakhir
- `status_ikatan_kerja`: Status kepegawaian
- `status_aktivitas`: Status aktivitas dosen

### 3. Detail Dosen - Penelitian
**Endpoint:** `GET /dosen/{dosen_id}/penelitian`
**Description:** Mendapatkan data penelitian dosen
**Parameters:**
- `dosen_id` (string): ID dosen

**Response Fields:**
- `judul_kegiatan`: Judul penelitian
- `tahun_kegiatan`: Tahun pelaksanaan
- `jenis_kegiatan`: Jenis penelitian
- `sumber_dana`: Sumber pendanaan

### 4. Detail Dosen - Pengabdian
**Endpoint:** `GET /dosen/{dosen_id}/pengabdian`
**Description:** Mendapatkan data pengabdian masyarakat dosen
**Parameters:**
- `dosen_id` (string): ID dosen

### 5. Detail Dosen - Karya Ilmiah
**Endpoint:** `GET /dosen/{dosen_id}/karya`
**Description:** Mendapatkan data karya ilmiah dosen
**Parameters:**
- `dosen_id` (string): ID dosen

### 6. Detail Dosen - Paten
**Endpoint:** `GET /dosen/{dosen_id}/paten`
**Description:** Mendapatkan data paten dosen
**Parameters:**
- `dosen_id` (string): ID dosen

### 7. Detail Dosen - Riwayat Pendidikan
**Endpoint:** `GET /dosen/{dosen_id}/study_history`
**Description:** Mendapatkan riwayat pendidikan dosen
**Parameters:**
- `dosen_id` (string): ID dosen

### 8. Detail Dosen - Riwayat Mengajar
**Endpoint:** `GET /dosen/{dosen_id}/teaching_history`
**Description:** Mendapatkan riwayat mengajar dosen
**Parameters:**
- `dosen_id` (string): ID dosen

## 🏫 Perguruan Tinggi (University) APIs

### 1. Search PT
**Endpoint:** `GET /search_pt`
**Description:** Mencari perguruan tinggi berdasarkan nama atau singkatan
**Parameters:**
- `keyword` (string): Nama atau singkatan perguruan tinggi

**Example Request:**
```python
with api() as client:
    result = client.search_pt('Unika Soegijapranata')
```

**Response Fields:**
- `id`: ID unik perguruan tinggi
- `kode`: Kode perguruan tinggi
- `nama`: Nama lengkap perguruan tinggi
- `nama_singkat`: Nama singkat/akronim

## 📚 Program Studi (Study Program) APIs

### 1. Search Prodi
**Endpoint:** `GET /search_prodi`
**Description:** Mencari program studi berdasarkan nama
**Parameters:**
- `keyword` (string): Nama program studi

**Example Request:**
```python
with api() as client:
    result = client.search_prodi('Teknik Informatika')
```

**Response Fields:**
- `id`: ID unik program studi
- `nama`: Nama program studi
- `jenjang`: Jenjang pendidikan (S1, S2, S3, D3, D4)
- `pt`: Nama perguruan tinggi
- `pt_singkat`: Singkatan perguruan tinggi

## 🔍 Search All API

### 1. Search All
**Endpoint:** `GET /search_all`
**Description:** Mencari semua jenis data (mahasiswa, dosen, PT, prodi)
**Parameters:**
- `keyword` (string): Kata kunci pencarian

**Example Request:**
```python
with api() as client:
    result = client.search_all('Ilham')
```

## ⚠️ Error Handling

### Common Error Types

1. **ValidationError**
   - **Cause:** Parameter input tidak valid
   - **Solution:** Periksa format parameter yang dikirim

2. **APIConnectionError**
   - **Cause:** Gagal koneksi ke server PDDIKTI
   - **Solution:** Periksa koneksi internet dan status server

3. **None Response**
   - **Cause:** API mengembalikan response kosong
   - **Solution:** Periksa parameter yang dikirim dan coba dengan keyword berbeda

### Error Response Format
```json
{
  "error": "Error message",
  "type": "Error type",
  "details": "Additional error details"
}
```

## 🚀 Performance Notes

### API Latency
- **Average Response Time:** 10-15 seconds
- **Peak Times:** 20-30 seconds
- **Recommended:** Implement loading indicators

### Best Practices
1. **Caching:** Implement caching for frequently accessed data
2. **Loading States:** Always show loading indicators
3. **Error Handling:** Graceful error handling with user-friendly messages
4. **Retry Logic:** Implement retry mechanism for failed requests

## 🔧 Debugging Tools

### Debug Routes in Application
1. **`/debug_search/<keyword>`**: Debug search functionality
2. **`/debug_detail/<mahasiswa_id>`**: Debug detail functionality
3. **Debug Buttons**: Available on search result pages

### Console Logging
```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📝 Example Usage

### Complete Student Search and Detail
```python
from pddiktipy import api

with api() as client:
    # Search for student
    search_result = client.search_mahasiswa('Ilham Riski Wibowo')
    
    if search_result and search_result.get('data'):
        student = search_result['data'][0]
        
        # Get detailed information
        nim = student['nim']
        npsn = student['npsn']
        kode_prodi = student['kode_prodi']
        
        detail = client.get_detail_mhs(nim, npsn, kode_prodi)
        
        if detail and detail.get('data'):
            student_detail = detail['data']['mahasiswa']
            print(f"Nama: {student_detail['nama']}")
            print(f"NIM: {student_detail['terdaftar']['nim']}")
            print(f"IPK: {student_detail['terdaftar']['ipk']}")
```

### Complete Lecturer Search and Detail
```python
with api() as client:
    # Search for lecturer
    search_result = client.search_dosen('Prof. Dr. Ilham')
    
    if search_result and search_result.get('data'):
        lecturer = search_result['data'][0]
        dosen_id = lecturer['id']
        
        # Get all lecturer details
        profile = client.get_dosen_profile(dosen_id)
        penelitian = client.get_dosen_penelitian(dosen_id)
        pengabdian = client.get_dosen_pengabdian(dosen_id)
        karya = client.get_dosen_karya(dosen_id)
        paten = client.get_dosen_paten(dosen_id)
        study_history = client.get_dosen_study_history(dosen_id)
        teaching_history = client.get_dosen_teaching_history(dosen_id)
```

## 📞 Support

For API-related issues:
- **Documentation:** Check this file for endpoint details
- **Testing:** Use debug routes in the application
- **Postman:** Test API calls directly with Postman
- **Console Logs:** Check application logs for detailed error information
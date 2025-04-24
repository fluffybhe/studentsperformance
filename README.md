# 💼 Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institute

## 📚 Business Understanding

**Jaya Jaya Institute** merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah dikenal sebagai kampus inklusif yang menerima mahasiswa dari berbagai latar belakang dan menyediakan lebih dari 10 program studi, baik di kelas pagi maupun malam. Reputasi institusi yang solid terlihat dari banyaknya alumni yang berhasil meniti karier di berbagai sektor.

Namun, di balik kesuksesan tersebut, institusi menghadapi tantangan besar berupa **tingginya tingkat putus studi (dropout)** mahasiswa. Fenomena ini tidak hanya berpotensi merusak citra institusi, tetapi juga menimbulkan kerugian dari sisi keuangan, sumber daya, dan moral. Lebih dari itu, mahasiswa yang mengalami dropout kehilangan kesempatan untuk menyelesaikan pendidikan tinggi yang esensial bagi masa depan mereka.

### 🎯 Latar Belakang Permasalahan

Berbagai studi menunjukkan bahwa tingkat dropout dapat dipengaruhi oleh banyak faktor, mulai dari performa akademik awal, jurusan yang dipilih, jalur penerimaan mahasiswa, hingga kondisi sosial-ekonomi. Oleh karena itu, pemetaan faktor-faktor ini secara data-driven menjadi hal yang sangat penting.

Menyadari urgensi tersebut, Divisi Akademik Jaya Jaya Institute menetapkan dua langkah strategis utama:

1. **Mengidentifikasi faktor signifikan** yang berkorelasi dengan status akademik mahasiswa, baik faktor internal seperti nilai akademik, maupun faktor eksternal seperti jalur masuk.
2. **Mengembangkan dashboard visual interaktif** yang tidak hanya menyajikan data akademik secara komprehensif, tetapi juga mampu **memprediksi kemungkinan dropout mahasiswa** secara real-time menggunakan pendekatan Machine Learning dengan Logistic Regression model

Dengan adanya dashboard ini, pihak kampus — termasuk dosen wali, ketua program studi, dan manajemen institusi — dapat memonitor performa mahasiswa secara menyeluruh serta mengambil langkah preventif dan intervensi secara lebih dini dan tepat sasaran.


## ❗ Permasalahan Bisnis

Permasalahan utama yang dihadapi Jaya Jaya Institute adalah **tingginya tingkat dropout mahasiswa**. Banyaknya jumlah jurusan serta latar belakang mahasiswa yang beragam membuat proses pemantauan menjadi kompleks. Untuk itu, diperlukan pendekatan analitik guna menemukan akar penyebab utama dan merumuskan solusi berbasis data yang efektif.

---

## 🔍 Cakupan Proyek

Proyek ini dirancang dengan cakupan sebagai berikut:

1. **Analisis eksploratif** terhadap data historis mahasiswa untuk menganalisis faktor penyebab dropout.
2. **Pengembangan model prediksi machine learning** yang mampu mengklasifikasikan mahasiswa yang berpotensi dropout.
3. **Implementasi model dan visualisasi interaktif** dalam bentuk dashboard berbasis Streamlit untuk digunakan oleh pihak kampus dalam pemantauan dan pengambilan keputusan.

### Persiapan


1. Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance


2. Setup environment:

- Pastikan perangkat Anda tersambung dengan koneksi internet untuk memungkinkan proses pengunduhan dan pemasangan modul (library) yang dibutuhkan.
- Jalankan Command Prompt (CMD) atau PowerShell sebagai administrator guna mendapatkan hak akses penuh selama proses instalasi.
---bash
pip install -r requirements.txt
```

### Business Dashboard

link dashboard  beserta prediksi machine learning : http://172.16.155.54:8501

Pada bagian atas dashboard, terdapat lima slicer yang bertujuan untuk membantu pengguna menfilter sesuai kebutuhan. Slicer tersebut terdiri dari sebagai berikut.
1. Status - terdiri dari "Dropout" , "Enrolled" dan "Graduated".
2. Course/Jurusan - terdiri dari jurusan yang ada. Hanya dapat memilih satu jurusan dalam satu waktu.
3. Gender - terdiri dari male dan female.
3. Attendance Time/Tipe jurusan - terdiri dari daytime (kelas pagi) dan evening (kelas malam).
5. Prediction dipilih untuk prediksi mahasiswa yang berpotensi dropout 

Di bagian bawah judul terdapat keterangan atau card yang terdiri dari dropout rate dan jumlah mahasiswa yang ada dan mahasiswa yang lulus . Keterangan tersebut bersifat dinamis dan berubah sesuai filter yang digunakan. Di bawah keterangan tersebut, terdapat tujuh grafik.

### 📊 **Distribusi Visual**
Dashboard menampilkan berbagai **grafik interaktif** untuk memberikan wawasan lebih dalam:

1. **💖 Scholarship Holders by Status**  
   - Membandingkan jumlah pemegang beasiswa antara mahasiswa dropout dan tidak dropout.

2. **📊 Age at Enrollment Distribution**  
   - Menampilkan **usia minimum, rata-rata, dan maksimum**:
     - Min: 17 tahun
     - Rata-rata: 23.27 tahun
     - Maks: 70 tahun
   - Membantu mengidentifikasi apakah usia berpengaruh terhadap risiko dropout.

3. **📊 Tuition Fees Up to Date**  
   - Visual untuk melihat apakah **tunggakan biaya** berkorelasi dengan dropout.

4. **📊 Debtor Distribution**  
   - Menyoroti jumlah mahasiswa yang memiliki **utang akademik**.

5. **📊 Average Grades (Semesters)**  
   - Melihat **nilai rata-rata mahasiswa** pada semester 1 dan 2 untuk mengukur performa awal akademik.

6. **📊 Dropout by Course**  
   - Menampilkan kursus mana yang memiliki **tingkat dropout tertinggi**.

7. **📊 Educational Special Needs Distribution**  
   - Memperlihatkan proporsi mahasiswa dengan kebutuhan khusus dan kaitannya dengan dropout.

-

### 💫 **Fitur Prediksi Dropout**  
Bagian interaktif di mana pengguna bisa:
- memilih slicer prediction
- Mengisi **form input data mahasiswa**:  
  - Kursus, usia, jenis kelamin, status beasiswa, nilai semester, dll.
  Mengisi data yang dibutuhkan. Perlu diperhatikan bahwa nilai jurusan atau Course tidak boleh 'None' serta terdapat batas minimum dan maksimum pada input numerik. Selain itu, pengguna harus menekan enter agar dapat menyimpan data numerik.
- Setelah submit, dashboard akan memberikan **hasil prediksi** apakah mahasiswa:
  - **🌟 Likely to Stay!** – Mahasiswa kemungkinan besar akan tetap lanjut.  
  - **🚨 Likely to Drop Out!** – Mahasiswa berisiko tinggi untuk dropout.
- Hasil prediksi akan tampil di bagian bawah. Akan tetapi, akan muncul pesan  ❌ Please select a valid course. akan muncul apabila pengguna tidak memilih jurusan atau Course.

Contoh input:
- Kursus: Animation and Multimedia Design  
- Usia: 60  
- Gender: Female  
- Admission grade :132
- Nilai Semester 1: 13.0  
- Nilai Semester 2: 12.0  
- **🌟 Prediction: Likely to Stay!**

🎯 Ini menunjukkan sistem **tidak hanya mengandalkan usia** atau satu faktor saja, melainkan menggabungkan semua data untuk membuat keputusan cerdas.

---

### 🌸 **Sentuhan Estetika**
- Warna dominan: **Pink, putih, dan pastel**.
- Setiap bagian didesain dengan **emoji, border bulat, dan padding lembut**.
- Memberikan kesan **ramah pengguna, modern, dan menyenangkan**.
- Penutup dashboard:
  > 🌷 Designed with 💕 by Febhe Maulita May Pramasta 🌷  
  Memberi sentuhan personal dan ownership pada proyek ini.

---

### 🧠 **Manfaat Dashboard Ini**
- Dapat digunakan oleh **manajemen kampus atau fakultas** untuk:
  - Mengidentifikasi mahasiswa yang berisiko dropout.
  - Menentukan strategi intervensi seperti mentoring, bantuan finansial, atau konseling.
- Memberikan data insight untuk perbaikan kurikulum dan layanan pendidikan.


## **Conclusion**

- Faktor yang paling berpengaruh terhadap status akademik mahasiswa adalah keterlambatan pembayaran biaya kuliah. Mahasiswa yang **tidak membayar biaya kuliah tepat waktu (Tuition_fees_up_to_date)** memiliki kemungkinan lebih tinggi untuk dropout. Selain itu, status **penerima beasiswa (Scholarship_holder)** juga berkontribusi signifikan, di mana mahasiswa penerima beasiswa cenderung memiliki risiko putus studi yang lebih rendah.

- Dari total populasi mahasiswa yang diamati, **32,1% mahasiswa mengalami dropout**, sementara **49,9% berhasil lulus**. Sisanya masih dalam status aktif atau belum selesai studi. Angka ini menunjukkan bahwa hampir sepertiga mahasiswa tidak menyelesaikan studinya, menjadi sinyal penting untuk peningkatan sistem dukungan akademik dan non-akademik.

- Program studi dengan **tingkat dropout tertinggi** adalah:
  - **Biofuel Production Technologies**: 66,67%
  - **Equinculture**: 55,32%
  - **Informatics Engineering**: 54,12%  
  Ketiga program ini perlu mendapatkan perhatian lebih dalam bentuk evaluasi kurikulum, sistem pembelajaran, dan dukungan terhadap mahasiswa.

- Rata-rata nilai masuk mahasiswa (admission grade) tidak menunjukkan perbedaan yang mencolok antar status akhir studi (*Dropout*, *Graduated*, *Enrolled*). Ini menandakan bahwa **nilai awal saat masuk bukan penentu utama keberhasilan akademik**, dan keberhasilan lebih dipengaruhi oleh faktor lain seperti dukungan finansial, motivasi belajar, dan lingkungan akademik.

- Mahasiswa penerima beasiswa menunjukkan **tingkat dropout yang jauh lebih rendah**, yaitu sekitar **12,1%** dari total 1.099 mahasiswa. Hal ini memperkuat dugaan bahwa **jalur atau status penerimaan mahasiswa, terutama yang berkaitan dengan dukungan finansial, memiliki korelasi positif terhadap keberhasilan studi**.



### Rekomendasi Action Items
Berikut adalah versi **Rekomendasi Action Items** untuk proyek Anda yang disesuaikan dengan hasil analisis dan konteks Jaya Jaya Institute:

---

### **Rekomendasi Action Items**

Untuk menurunkan angka **dropout mahasiswa** dan meningkatkan keberhasilan akademik di Jaya Jaya Institute, berikut beberapa rekomendasi tindakan yang dapat dilakukan:

- **Evaluasi sistem pembayaran biaya kuliah**, khususnya keterlambatan pembayaran (tuition fees). Pertimbangkan penerapan sistem cicilan, kebijakan penangguhan pembayaran, atau dukungan finansial tambahan bagi mahasiswa yang berisiko.

- **Perluasan dan optimalisasi program beasiswa**, mengingat mahasiswa penerima beasiswa memiliki tingkat dropout yang rendah (hanya 12,1%). Memberikan akses beasiswa yang lebih luas akan membantu mahasiswa yang mengalami tekanan ekonomi dan mengurangi beban hutang.

- **Melakukan pendampingan akademik dan psikologis** bagi mahasiswa yang memiliki risiko dropout. Hal ini dapat melibatkan mentoring akademik, pelatihan manajemen waktu, serta konseling untuk mahasiswa yang kesulitan menyesuaikan diri di lingkungan kampus.

- **Lakukan evaluasi mendalam pada program studi dengan tingkat dropout tinggi**, seperti:
  - **Biofuel Production Technologies** (66,67% dropout rate): Periksa relevansi kurikulum, beban studi, dan kualitas pengajaran.
  - **Equinculture** dan **Informatics Engineering**: Lakukan pemetaan kendala spesifik pada kelompok mahasiswa tertentu, misalnya berdasarkan gender atau latar belakang pendidikan.

- **Tinjau dan perbaiki proses seleksi masuk mahasiswa**, bukan hanya berdasarkan nilai awal, tetapi juga memperhatikan motivasi, kesiapan akademik, dan potensi adaptasi mahasiswa.

- **Bangun sistem monitoring akademik berbasis data**, agar mahasiswa dengan kecenderungan performa rendah atau keterlambatan pembayaran dapat diidentifikasi sejak dini dan diberikan intervensi yang tepat.

- **Promosikan program pendampingan oleh senior atau alumni**, guna menciptakan lingkungan belajar yang suportif dan mendorong keterlibatan mahasiswa dalam kegiatan akademik dan non-akademik.


# 🛒 Supermarket Sales Data Analysis Dashboard

**End-to-End Data Pipeline & Interactive Analytics for Retail Performance**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.14-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)](https://www.elastic.co/)
[![Kibana](https://img.shields.io/badge/Kibana-8.14-005571?style=for-the-badge&logo=kibana&logoColor=white)](https://www.elastic.co/kibana)
[![Airflow](https://img.shields.io/badge/Apache_Airflow-2.x-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)](https://airflow.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

---

## 📌 1. Project Overview & Problem Background

Project ini berfokus pada analisis data transaksi supermarket untuk memahami perilaku konsumen dan performa penjualan di tiga cabang berbeda: **Yangon, Mandalay, dan Naypyitaw**. Dashboard ini dirancang untuk menjawab tantangan operasional retail melalui pendekatan berbasis data.

* **Sales Trends:** Menganalisis fluktuasi penjualan harian untuk optimasi stok.
* **Product Performance:** Identifikasi lini produk paling diminati dan analisis kepuasan pelanggan melalui rating.
* **Demographics & Payments:** Memahami korelasi antara profil pelanggan (Member/Normal) dan preferensi pembayaran terhadap total revenue.

---

## 📁 2. Project Structure
Berdasarkan manajemen file repositori, berikut adalah struktur direktori project ini:

```text
.
├── .github/             # GitHub Actions & Environment configurations
├── images/              # Dashboard screenshots & documentation visuals
├── analysis_GX.ipynb    # Data Validation Framework (Great Expectations)
├── conceptual.txt       # Technical documentation & conceptual answers
├── DAG_graph.jpg        # Validated Pipeline Execution Graph (Airflow)
├── DAG.py               # Data Pipeline Automation (Apache Airflow)
├── data_clean.csv       # Validated & Processed Dataset
├── data_raw.csv         # Raw Supermarket Sales Dataset
├── ddl.txt              # SQL Schema & Database Ingestion Scripts
├── description.md       # Detailed project technical documentation
└── README.md            # Main professional landing page

```

---

## 🔬 3. Methodology & Stacks

### A. Data Automation Pipeline (Airflow)

   Pipeline berjalan secara otomatis untuk menjamin integritas data dari sumber ke database analitik:

      Extraction: Pengambilan data dari PostgreSQL (Docker environment).

      Transformation: Normalisasi skema kolom, pembersihan duplikat, dan penanganan nilai kosong.

      Loading: Indexing data bersih ke Elasticsearch untuk pencarian cepat.

### B. Data Quality Assurance (Great Expectations)
   
   Validasi dilakukan secara ketat dengan 7 kriteria utama guna menjamin Data Integrity sebelum masuk ke tahap visualisasi, mencakup validasi tipe data, keunikan ID, dan batas nilai numerik.


### C. Technology Stacks:

   Storage: PostgreSQL & Elasticsearch.

      > Orchestration: Apache Airflow.

      > Analysis: Great Expectations & Python.

      > Visualization: Kibana v8.14 (Lens).

---


---

## 📊 4. Interactive Dashboard Output

   Dashboard yang dibangun di Kibana menyediakan 9 visualisasi kunci yang mencakup aspek finansial, operasional, dan kepuasan pelanggan:


      > Financial: Analisis gross income dan total sales per cabang.

      > Operational: Perbandingan performa product line lintas wilayah.

      > Customer: Distribusi tipe pelanggan dan tren rating produk.
---

---

## 🚀 5. Getting Started

      1. Pastikan Docker Stack (Elastic, Kibana, Airflow) sudah berjalan.

      2. Inisialisasi database menggunakan query pada ddl.txt.

      3. Jalankan DAG.py melalui scheduler Airflow untuk memproses data dari data_raw.csv.

      4. Akses Dashboard melalui Kibana untuk melihat hasil analisis interaktif.

---

---

## 🏁 6. Conclusion

   Hasil eksplorasi ini memberikan rekomendasi strategis bagi tim Marketing dan Procurement dalam menentukan strategi bundling produk dan pengelolaan inventaris yang lebih efisien berdasarkan tren demografi pelanggan.


   **Author: Risyadhana Syaifuddin | 2026**

---
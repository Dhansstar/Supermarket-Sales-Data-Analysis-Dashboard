# Supermarket Sales Data Analysis Dashboard

## Repository Outline

README.md - Penjelasan gambaran umum project, metodologi, dan hasil analisis.

POM3_Risyadhana_data_raw.csv - Dataset mentah yang digunakan untuk analisis didownload dari kaggle



screenshots/ - Folder berisi gambar visualisasi dashboard.


## Problem Background
Project ini berfokus pada analisis data transaksi supermarket untuk memahami perilaku konsumen dan performa penjualan di tiga cabang berbeda (Yangon, Mandalay, Naypyitaw). Masalah utama yang ingin dijawab adalah:

1. Bagaimana tren penjualan harian selama periode tertentu?

2. Produk apa yang paling diminati dan bagaimana kualitasnya di mata pelanggan?

3. Bagaimana profil demografi dan preferensi pembayaran pelanggan memengaruhi pendapatan perusahaan?

## Project Output

Output dari project ini adalah sebuah Interactive Data Dashboard yang dibangun menggunakan Elasticsearch dan Kibana (Lens). Dashboard ini menyediakan 9 visualisasi kunci yang mencakup aspek finansial, operasional, dan kepuasan pelanggan secara real-time.

## Data
Dataset yang digunakan adalah Supermarket Sales Dataset yang memiliki karakteristik sebagai berikut:

Sumber Data: Kaggle / Internal Sales Records.

Jumlah Data: 1.000 baris transaksi.

Jumlah Kolom: 17 kolom (termasuk sales, quantity, product_line, rating, date, dll).

Missing Values: Tidak ditemukan data kosong (clean dataset).

Karakteristik: Data mencakup transaksi selama 3 bulan dengan variasi tipe pelanggan (Member/Normal) dan gender.

## Method

Metode yang digunakan adalah Exploratory Data Analysis (EDA) dengan pendekatan visual. Langkah-langkahnya meliputi:

Data Ingestion: Mengunggah file CSV ke Elasticsearch melalui fitur Upload File di Kibana.

Data Transformation: Mengatur mapping field seperti date dan memastikan field numerik seperti sales terbaca dengan benar.

Descriptive Analytics: Membuat visualisasi perbandingan (Bar Chart), distribusi (Pie/Donut Chart), tren (Line Chart), dan korelasi (Treemap).

## Stacks
Data Storage: Elasticsearch

Visualization Tool: Kibana v8.14 (Lens)

Data Format: CSV / JSON

Environment: Elastic Cloud atau Local Stack

## Reference
Dashboard Link: 

Dataset Reference: (https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)

For Installation airflow, kibana, elastic, etc: 

https://github.com/aliaufa/p2m3-steps/blob/main/README.md

https://github.com/ardhiraka/DEBlitz


---

**Referensi tambahan:**
- https://crontab.guru/
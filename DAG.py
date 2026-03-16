'''
=================================================
Milestone 3
Nama  : Risyadhana
Batch : HCK -036

Program ini dibuat untuk melakukan automatisasi ETL:
1. Fetch: Mengambil data dari PostgreSQL.
2. Cleaning: Membersihkan data sesuai kriteria (lowercase, underscore, no symbols, handling missing values).
3. Load: Memasukkan data ke Elasticsearch.
=================================================
'''

import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import psycopg2
import pandas as pd
import re
from elasticsearch import Elasticsearch, helpers # pakai helpers supaya lebih cepat

# Fungsi Task: Fetch from PostgreSQL
def fromPostgre():
    '''Mengambil data mentah dari PostgreSQL table_m3 apa adanya'''
    # saya pakai 'postgres' sebagai host jika di dalam network docker-compose yang sama
    conn = psycopg2.connect(
        host="postgres", 
        database="airflow", # Sesuai settingan docker-compose kamu tadi
        user="airflow",
        password="airflow",
        port=5432
    )
    query = "SELECT * FROM table_m3;"
    data = pd.read_sql_query(query, conn)
    
    # Simpan di path /opt/airflow/dags/ agar bisa diakses task selanjutnya
    data.to_csv('/opt/airflow/dags/P2M3_Risyadhana_data_raw.csv', index=False)
    conn.close()

# Fungsi Task: Data Cleaning
def cleanData():
    '''Data Cleaning'''
    df = pd.read_csv('/opt/airflow/dags/P2M3_Risyadhana_data_raw.csv')
    
    # Hapus data duplikat
    df = df.drop_duplicates()
    
    # Normalisasi Column (Lowercase, Underscore, No Symbols)
    clean_columns = []
    for col in df.columns:
        c = col.lower().strip()
        c = c.replace(' ', '_')
        c = re.sub(r'[^a-z0-9_]', '', c) # Menghapus simbol/spasi berlebih
        clean_columns.append(c)
    df.columns = clean_columns
    
    # Handling Missing Values (Kategorikal: Unknown, Numerik: 0)
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna('Unknown')
        else:
            df[col] = df[col].fillna(0)
    
    # Simpan sebagai P2M3_Risyadhana_data_clean.csv
    df.to_csv('/opt/airflow/dags/P2M3_Risyadhana_data_clean.csv', index=False)

# Fungsi Task: Post to Elasticsearch
def toElasticsearch():
    '''Memasukkan data clean ke Elasticsearch'''
    # saya pakai 'elasticsearch' sebagai host di dalam Docker network
    es = Elasticsearch(["http://elasticsearch:9200"]) 
    df = pd.read_csv('/opt/airflow/dags/P2M3_Risyadhana_data_clean.csv')
    
    # bulk helpers (lebih efisien daripada loop biasa)
    documents = df.to_dict(orient='records')
    actions = [
        {
            "_index": "risyadhana_store", # Index yang akan muncul di Kibana
            "_source": doc
        } for doc in documents
    ]
    helpers.bulk(es, actions)

# Konfigurasi DAG
default_args = {
    'owner': 'Risyadhana',
    'start_date': dt.datetime(2024, 11, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG(
    'P2M3_Risyadhana_DAG',
    default_args=default_args,
    # Cron: Menit 10,20,30 Jam 9 Hari ke-6 (Sabtu)
    schedule_interval='10,20,30 9 * * 6', 
    catchup=False
) as dag:

    fetch_data = PythonOperator(
        task_id='fetch_from_postgresql',
        python_callable=fromPostgre
    )
    
    clean_task = PythonOperator(
        task_id='data_cleaning',
        python_callable=cleanData
    )
    
    load_to_es = PythonOperator(
        task_id='post_to_elasticsearch',
        python_callable=toElasticsearch
    )

# Definisi urutan task
fetch_data >> clean_task >> load_to_es
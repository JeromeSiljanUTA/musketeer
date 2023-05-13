import tweepy
import psycopg2
import pandas as pd
import time
import re

db_url = "postgresql://vladimir:auCN0jNaEMIhSArPYHdhEg@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dmusketeer-db-6480"

conn = psycopg2.connect(db_url)

with conn.cursor() as cur:
    cur.execute("SET DATABASE = defaultdb")
    cur.execute("DELETE FROM tweets")
    conn.commit()
    conn.close()

conn = psycopg2.connect(db_url)

with conn.cursor() as cur:
    cur.execute("SET DATABASE = defaultdb")
    cur.execute("SELECT * FROM tweets")
    print(cur.fetchall())
    conn.commit()
    conn.close()

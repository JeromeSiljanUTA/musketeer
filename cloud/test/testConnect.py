import os
import psycopg2

DATABASE_STRING = 'postgresql://vladimir-test:39KNZtj6uqDTJXZFTmA0XA@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dtesting-6482'
conn = psycopg2.connect(DATABASE_STRING)

with conn.cursor() as cur:
    
    cur.execute('CREATE TABLE IF NOT EXISTS TweetTable (id INT PRIMARY KEY, tweetTime TIMESTAMP , tweetText CHAR(280), company CHAR(4));')
    cur.execute('CREATE TABLE IF NOT EXISTS StockTable (id INT PRIMARY KEY, valueTime TIMESTAMP , value INT, company CHAR(4));')
    conn.commit()
    conn.close ()



import psycopg2
import pandas as pd
#import tensorflow as tf
from sklearn.model_selection import train_test_split
#from tensorflow.keras.preprocessing.text import Tokenizer

db_url = 'postgresql://vladimir:auCN0jNaEMIhSArPYHdhEg@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dmusketeer-db-6480'

conn = psycopg2.connect(db_url)
with conn.cursor() as cur:
    cur.execute('SET DATABASE = defaultdb')
    cur.execute('SELECT text FROM tweets')
    all_tweets = cur.fetchall()
    conn.close()


print(all_tweets)

#tokenizer = Tokenizer(num_words = 100000)
#tokenizer.fit_on_texts(raw_x)
#word_index = tokenizer.word_index
#sequences = tokenizer.texts_to_sequences(raw_x)
#x = pad_sequences(raw_x)

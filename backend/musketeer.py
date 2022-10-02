import psycopg2
import pandas as pd
import h5py
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#from google.colab import drive
#drive.mount('/content/gdrive', force_remount=True)

db_url = 'postgresql://vladimir:auCN0jNaEMIhSArPYHdhEg@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dmusketeer-db-6480'

conn = psycopg2.connect(db_url)
with conn.cursor() as cur:
    cur.execute('SET DATABASE = defaultdb')
    cur.execute('SELECT text, inc FROM tweets')
    all_tweets = cur.fetchall()
    conn.close()


raw_x = [tweet[0] for tweet in all_tweets]
y = [tweet[1] for tweet in all_tweets]

vocab_size = 100000
tokenizer = Tokenizer(num_words = vocab_size)
tokenizer.fit_on_texts(raw_x)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(raw_x)
x = pad_sequences(sequences)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=3)

x_train = np.asarray(x_train)
x_test = np.asarray(x_test)
y_train = np.asarray(y_train)
y_test = np.asarray(y_test)

embedding_dim = 16
max_length = 24

model  = tf.keras.Sequential([
                tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length = max_length),
                tf.keras.layers.GlobalAveragePooling1D(),
                tf.keras.layers.Dense(24, activation = 'relu'),
                tf.keras.layers.Dense(1, activation = 'sigmoid')
])

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

num_epochs = 10

history = model.fit(x_train, y_train, epochs = num_epochs, validation_data = (x_test, y_test))


#model.save('/content/gdrive/My Drive/model.h5')
#model.save('/content/gdrive/MyDrive/bare_model')

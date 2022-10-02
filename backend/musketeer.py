import pandas as pd
import psycopg2

db_url = 'postgresql://vladimir:auCN0jNaEMIhSArPYHdhEg@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dmusketeer-db-6480'

#df = pd.read_csv('tsla.us.txt')
#
#df['datetime'] = [pd.to_datetime(f'{x}{y}', format='%Y%m%d%H%M00') 
#        for x, y in zip(df['<DATE>'], df['<TIME>'])]
#
#df = df[['<TICKER>', 'datetime', '<CLOSE>']]
#df.columns = ['ticker', 'datetime', 'price']

conn = psycopg2.connect(db_url)

with conn.cursor() as cur:
    cur.execute('SET DATABASE = defaultdb')
    cur.execute('SHOW TABLES')
    res = cur.fetchall()
    conn.commit()
    print(res)

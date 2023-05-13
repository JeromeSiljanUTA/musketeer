import pandas as pd
import psycopg2

db_url = "postgresql://vladimir:auCN0jNaEMIhSArPYHdhEg@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dmusketeer-db-6480"

df = pd.read_csv("tsla.us.txt")

df["datetime"] = [
    pd.to_datetime(f"{x}{y}", format="%Y%m%d%H%M00")
    for x, y in zip(df["<DATE>"], df["<TIME>"])
]

df = df[["<TICKER>", "datetime", "<CLOSE>"]]
df.columns = ["ticker", "datetime", "price"]

conn = psycopg2.connect(db_url)

df_iter = df.iterrows()

# cur.execute('CREATE TABLE stocks(id UUID NOT NULL DEFAULT gen_random_uuid(), ticker STRING NOT NULL, datetime TIMESTAMP NOT NULL, price FLOAT NOT NULL, UNIQUE(ticker, datetime, price))')

with conn.cursor() as cur:
    cur.execute("SET DATABASE = defaultdb")

    for row in df_iter:
        ticker = row[1][0]
        datetime = row[1][1]
        price = row[1][2]
        cur.execute(
            f"INSERT INTO stocks (ticker, datetime, price) VALUES('{ticker}', '{datetime}', {price})"
        )

    cur.execute("SELECT * FROM stocks")
    print(cur.fetchall())
    conn.commit()

import os
import psycopg2
DATABASE_STRING = "postgresql://vladimir:auCN0jNaEMIhSArPYHdhEg@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dmusketeer-db-6480"
with psycopg2.connect(DATABASE_STRING) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT now()")
        res = cur.fetchall()
        conn.commit()
        print(res)

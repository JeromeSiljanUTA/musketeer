import tweepy
import psycopg2
import pandas as pd
import time
import re

# List of companies & their CEO's twitter accounts
companies = [
    'TSLA'#,
    #'Apple',
    #'Google',
    #'Dell',
    #'Epic Games',
    #'Microsoft',
    #'Uber',
    #'Spotify',
    #'Xbox',
    #'Amazon',
    #'Peloton',
    #'Lyft',
    #'Airbnb'
    ]
ceo_accounts = [
    'elonmusk'#,
    #'tim_cook',
    #'sundarpichai',
    #'MichaelDell',
    #'TimSweeneyEpic',
    #'satyanadella',
    #'dkhos',
    #'eldsjal',
    #'XboxP3',
    #'JeffBezos',
    #'keylargofoley',
    #'logangreen',
    #'bchesky'
    ]

# Set Twitter API Information
consumer_key = "Ri4nziuxkZG6CPX0KJKmNag86"
consumer_secret = "MpXONuPlBEvd6Iv6gS04NurLDU340yYErq1gKB3eRfzXjeEe9Z"
access_token = "1296225091366326272-ylfucsoPEKnhqrg3Df7jfUrWq0omsa"
access_secret = "yse6bt4SG54jxTLicFw6VxOIHMSxvDp3iwcyncWtv9MHI"

# Configure Tweepy Object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Run through list of CEO messages and put them in one array
messages = []

for x in range(len(companies)):
    print("Company: " + companies[x] + " Account: " + ceo_accounts[x])
    cursor = tweepy.Cursor(api.user_timeline,
                        screen_name=ceo_accounts[x],
                        count=None,
                        since_id=None,
                        max_id=None,
                        trim_user=True,
                        exclude_replies=True,
                        include_rts=False
                        )
    try:
        for y in cursor.items():
            messages.append({'company': companies[x], 'message_id': y.id, "time": y.created_at, "text": y.text})
    except:
        print("Error: Waiting 2 minutes for cooldown")
        time.sleep(120)

# Push to db
db_url = 'postgresql://vladimir:auCN0jNaEMIhSArPYHdhEg@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dmusketeer-db-6480'
conn = psycopg2.connect(db_url)

df_iter = df.iterrows()
regex = re.compile('[^a-zA-Z]')

with conn.cursor() as cur:
    cur.execute('SET DATABASE = defaultdb')

    for row in df_iter:
        ticker = row[1][0]
        datetime = row[1][2]
        text = ''
        regex.sub(text, row[1][3].strip())
        cur.execute(f"INSERT INTO tweets (ticker, datetime, text) VALUES('{ticker}', '{datetime}', '{text}')")

    cur.execute('SELECT * FROM tweets')
    print(cur.fetchall())
    conn.commit()
    conn.close()

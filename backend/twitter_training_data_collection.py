import tweepy
import psycopg2
import pandas as pd
import time
import re

db_url = 'postgresql://vladimir:auCN0jNaEMIhSArPYHdhEg@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dmusketeer-db-6480'

def did_inc(date):
    conn = psycopg2.connect(db_url)
    with conn.cursor() as cur:
        cur.execute('SET DATABASE = defaultdb')
        try:
            cur.execute(f"SELECT * FROM stocks where datetime < '{date}' ORDER BY datetime DESC LIMIT 1")
            before = (cur.fetchall()[0][3])
        except:
            return 1
        try:
            cur.execute(f"SELECT * FROM stocks where datetime > '{date}' ORDER BY datetime ASC LIMIT 1")
            after = (cur.fetchall()[0][3])
        except:
            return 1
        if (before - after) >= 0:
            return 0
        else:
            return 1
        conn.close()

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
conn = psycopg2.connect(db_url)

regex = re.compile('[^a-zA-Z]')

with conn.cursor() as cur:
    cur.execute('SET DATABASE = defaultdb')

    for message in messages:
        ticker = message['company']
        datetime = message['time']
        text = ''
        regex.sub(text, message['text'].strip())
        print(text)
        inc_val = did_inc(datetime)
        cur.execute(f"INSERT INTO tweets (ticker, datetime, text, inc) VALUES('{ticker}', '{datetime}', '{text}', '{inc_val}')")

    cur.execute('SELECT * FROM tweets')
    print(cur.fetchall())
    conn.commit()
    conn.close()

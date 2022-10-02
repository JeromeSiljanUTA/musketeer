import tweepy
import pandas as pd
import time

# List of companies & their CEO's twitter accounts
companies = [
    'Apple',
    'Google',
    'Dell',
    'Epic Games',
    'Microsoft',
    'Uber',
    'Spotify',
    'Xbox',
    'Amazon',
    'Peloton',
    'Lyft',
    'Airbnb'
    ]
ceo_accounts = [
    'tim_cook',
    'sundarpichai',
    'MichaelDell',
    'TimSweeneyEpic',
    'satyanadella',
    'dkhos',
    'eldsjal',
    'XboxP3',
    'JeffBezos',
    'keylargofoley',
    'logangreen',
    'bchesky'
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

# Make DataFrame Object
df = pd.DataFrame(messages)
df.to_csv('saved_tweets')
print(df)

import pandas as pd

df = pd.read_csv('tsla.us.txt')

df = df[['<DATE>', '<TIME>', '<CLOSE>']]
df.columns = ['date', 'time', 'value']

df['time'] = df['time']/100

df['datetime'] = df['date'] + df['time']

print(df)

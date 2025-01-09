import pandas as pd

d_parser = lambda x: pd.datetime.strptime(x,'%Y-%m-%d %I-%p') #each individual string is sent thro this function
df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)
print(df)
#print(df.head())
#print(df.shape)

#print(df.loc[0,'Date'])

#df['Date'] = pd.to_datetime(df['Date'],format= '%Y-%m-%d %I-%p')

print(df.loc[0,'Date'].day_name())
print(df.columns)
#print(df.iloc[0:5,0:2])
print(df.loc[0:2,'Date':'Low'])
#print(df['Date'])
print(df['Date'].dt.day_name())
print(df['Date'].max() - df['Date'].min())
#print()

flt = (df['Date'] >= '2020')
print(df.loc[flt])
#print(df.loc[0:2,'Date':'Low'])
#print('****')
#print(df.iloc[0:3,2])
df.set_index('Date',inplace=True)
print(df['2020-01-01']['High'].max())

print(df.resample('W').mean())
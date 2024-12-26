import pandas as pd
df = pd.read_csv(r'C:\Users\itato\OneDrive\デスクトップ\RPython\プログラミング演習(DS)\csv\browser_share.csv', index_col=0) # CSVから読込
print(df, '\n')
d1 = df[1:3] # 行番号1～2の行を取得
print(d1, '\n')
d2 = df[['Edge', 'IE']] # 'Edge'と'IE'のラベルの列を取得
print(d2, '\n')
d3 = df.iloc[1:3, 1:4] # 行番号1～2と列番号1～3の範囲を取得
print(d3, '\n')
d4 = df.loc['Apr-19':'Apr-21'] # 'Apr-19'から'Apr-21'の範囲を取得
print(d4, '\n')
d5 = df[df['Firefox'] >= 10] # 'Firefox'の列で10以上の値の行を取得
print(d5)

newdf = pd.DataFrame(df[['IE', 'Safari', 'Firefox', 'Edge', 'Chrome']])
print(newdf, '\n')

df6 = df[df['Firefox'] + df['Chrome'] >= 65]
print(df6)

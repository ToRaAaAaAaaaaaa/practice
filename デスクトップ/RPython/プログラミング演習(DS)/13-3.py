import pandas as pd
df = pd.DataFrame({'Name':['Alice','Bob',''], 'Age':[None,23,25],
'Weight':[51.8,None,52.9]})
print(df, '¥n')
d1 = df.isnull() # 欠損値の確認
print(d1, '¥n')
d2 = df.dropna() # 欠損値を含む行を削除
print(d2, '¥n')
d3 = df.fillna(0.0) # 全ての欠損箇所に0を設定
print(d3, '¥n')
# Ageの欠損箇所には0を、Weightの欠損箇所には50を設定
d4 = d4 = df.fillna({'Age':0, 'Weight':50})
print(d4)

df5 = df.dropna(axis=0, how='any', subset=['Weight'], inplace=False)
print(df5)

df6 = df.fillna({'Weight':df['Weight'].mean()})
print(df6)
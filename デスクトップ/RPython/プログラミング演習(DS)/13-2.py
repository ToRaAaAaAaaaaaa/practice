import pandas as pd
df = pd.read_csv(r'C:\Users\itato\OneDrive\デスクトップ\RPython\プログラミング演習(DS)\csv\browser_share.csv', index_col=0) # CSVから読込
print(df, '¥n')
d1 = df.sort_values(['Edge', 'Firefox']) # 2つの列の値でソート
print(d1, '¥n')
print('最大値:¥n', df.max().to_string(), '¥n', sep='')
print('横方向の最小値:¥n', df.min(axis=1).to_string(), '¥n', sep='')
print('平均値 :¥n', df.mean().to_string(), '¥n', sep='')
print('標準偏差:¥n', df.std().to_string(), sep='')

df2 = df.sort_values(['Safari'], ascending=False)
print(df2)

print('平均値 :')
print('Edge   {:.3f}'.format(df['Edge'].mean()))
print('IE     {:.3f}'.format(df['IE'].mean()))
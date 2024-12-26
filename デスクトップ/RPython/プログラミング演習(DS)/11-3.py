'''
import numpy as np
rng = np.random.default_rng() # 乱数生成器の用意
a = rng.integers(0,101,12) # 1次元配列
print(a, '\n')
a.sort() # 1次元配列のソート
print('昇順:', a)
b = a[::-1] # 降順にしたい場合はソート後にスライスを用いる
print('降順:', b)

import numpy as np
rng = np.random.default_rng() # 乱数生成器の用意
a = rng.integers(0,101,12).reshape(3, 4) # 2次元配列
b = a.copy()
c = a.copy()
print(a, '\n')
a.sort() # 2次元配列のソート(行(横の一列)ごと)
print(a, '\n')
b.sort(axis=0) # 2次元配列のソート(列(縦の一列)ごと)
print(b, '\n')
c = c[:, c[0,:].argsort()] # 先頭行を基準にしてソート
print(c)

import numpy as np
rng = np.random.default_rng() # 乱数生成器の用意
a = rng.integers(0,101,12).reshape(3, 4) # 2次元配列
b = a.copy()
c = a.copy()
print(a, '\n')
a.sort() # 2次元配列のソート(行(横の一列)ごと)
print(a, '\n')
b.sort(axis=0) # 2次元配列のソート(列(縦の一列)ごと)
print(b, '\n')
c = c[c[:, 0].argsort(), :]
print(c)
'''

import pandas as pd

# CSVデータを読み込む
data = pd.read_csv(r'C:\Users\itato\OneDrive\デスクトップ\RPython\プログラミング演習(2a)\csv\ex09-1.csv', header=None)
data.columns = ['month', 'precipitation', 'temperature']

tmp = data[['month', 'temperature']].sort_values(by='temperature', ascending=False)
tmp.columns = ['月：', '気温（℃）：']
tmp = tmp.T

print('<前橋市の2021年月別最高気温（降順）>')
print(tmp.to_string(header=False))

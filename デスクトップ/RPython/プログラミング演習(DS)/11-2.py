'''
import numpy as np
rng = np.random.default_rng() # 乱数生成器の用意
a = rng.integers(0,101,12).reshape((3, 4)) # 3x4の2次元配列
print(a, '¥n')
print('最大値:', a.max())
print('最小値:', a.min())
print('縦方向ごとの最大値:', a.max(axis=0))
print('横方向ごとの最大値:', a.max(axis=1))
print()
print('平均値 :', a.mean())
print('分散 :', a.var())
print('標準偏差:', a.std())
'''

'''
import numpy as np
rng = np.random.default_rng() # 乱数生成器の用意
a = rng.integers(0,101,12).reshape((1, 12)) # 1x12の1次元配列
print(a, '¥n')
print('最大値:', a.max())
print('最小値:', a.min())
print('縦方向ごとの最大値:', a.max(axis=0))
print('横方向ごとの最大値:', a.max(axis=1))
print()
print('平均値 :', a.mean())
print('分散 :', a.var())
print('標準偏差:', a.std())
'''

import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\itato\OneDrive\デスクトップ\RPython\プログラミング演習(2a)\csv\ex09-1.csv', header=None)
data.columns = ['month', 'precipitation', 'temperature']
print('最大値:', data['precipitation'].max())
print('最小値:', data['precipitation'].min())
print()
print('平均値 :', data['precipitation'].mean())
print('分散 :', data['precipitation'].var(ddof=0))
print('標準偏差:', data['precipitation'].std(ddof=0))

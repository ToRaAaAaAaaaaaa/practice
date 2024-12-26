'''
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
a[0, 1] = 10 # 番号[0,1]の要素に代入
print(f'変更後¥n{a}')
b = 0
for i in range(3):
b += a[1, i] # a[1,0]～a[1,2]を順に足す
print(f'b={b}')

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a, '¥n')
print(a[:, 1], '¥n') # a[0,1]～a[1,1]の要素を表示
a[1, 0:2] += 10 # a[1,0]～a[1,1]に10を順に足す
print(a, '¥n')
a *= 10 # aの全要素を10倍する
print(a)

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(a + b, '¥n') # 要素同士の加算
print(a - b, '¥n') # 要素同士の減算
print(a * b, '¥n') # 要素同士の乗算
print(a / b) # 要素同士の除算

import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng() # 乱数生成器の用意
s1 = rng.integers(0,101,50) # 0～100の整数を100個生成
s2 = rng.integers(0,101,50) # 0～100の整数を100個生成
plt.scatter(s1, s2) # 生成した配列を用いて散布図を作成
plt.show()
'''

'''
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(f"{a}\n\n{a[:, 1]}\n")
a[1, 0:2] += 10 # a[1,0]～a[1,1]に10を順に足す
a[0, :] = [7, 8, 9]
print(a, '\n')
a *= 10 # aの全要素を10倍する
print(a)
'''

import numpy as np
import matplotlib.pyplot as plt

# 標準正規分布に従ったデータを生成
np.random.seed(42)  # 再現性のためシードを設定
rng = np.random.default_rng()
data = rng.standard_normal(size=10000)  # 平均0, 標準偏差1, サンプル数1000

# ヒストグラムの計算 (ビンの範囲と頻度を取得)
bins = np.linspace(-4, 4, 51)  # -4から4の範囲で等間隔に20個のビン
frequencies, edges = np.histogram(data, bins=bins)

# 棒グラフを描画
plt.bar(edges[:-1], frequencies, width=np.diff(edges), color='blue')
# グラフを表示
plt.show()
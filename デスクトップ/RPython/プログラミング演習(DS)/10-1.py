'''
import numpy as np
# 大きさ10の1次元配列をすべて0で作成
a1 = np.zeros(10)
# 大きさ3×2の2次元配列をリストのデータから作成
data = [[1, 2], [3, 4], [5, 6]]
a2 = np.array(data)
# 配列の中身の表示
print(a1, '¥n')
print(a2)

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(f'サイズ:{a.shape}')
print(f'要素数:{a.size}')
'''

import numpy as np
st = int(input("開始値の入力>>"))
en = int(input("終了値の入力>>"))
ctt = int(input("値の必要数>>"))

array_values = np.linspace(st, en, ctt)
print('作成された配列')
print(array_values)

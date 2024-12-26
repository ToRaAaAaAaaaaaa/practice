'''
import numpy as np
a1 = np.arange(12) # 大きさ12の1次元配列(要素は0～11)
print(a1, '\n')
a2 = a1.reshape((3, 4)) # a1を3×4の2次元にした配列を作成
print(a2, '\n')
a3 = a2.ravel() # a2を1次元にした配列を作成
print(a3, '\n')
a3[0] = 10
print(a2, '\n') # a3を変更した場合のa2への影響を確認
a4 = a2.transpose() # a2を転置した配列を作成
print(a4, '\n')
print(a1, '\n')
a1.resize((2, 6)) # a1を2×6の2次元にした配列に変更
print(a1)
'''

'''
import numpy as np
a1 = np.arange(12) # 大きさ12の1次元配列(要素は0～11)
print(a1, '\n')
a2 = a1.reshape((3, 4)) # a1を3×4の2次元にした配列を作成
print(a2, '\n')
a3 = a2.flatten() # a2を1次元にした配列を作成
print(a3, '\n')
a3[0] = 10
print(a2, '\n') # a3を変更した場合のa2への影響を確認
a4 = a2.transpose() # a2を転置した配列を作成
print(a4, '\n')
print(a1, '\n')
a1.resize((2, 6)) # a1を2×6の2次元にした配列に変更
print(a1)
'''

import numpy as np

a5 = np.random.randint(0, 101, size=(3, 3))
a6 = np.random.randint(0, 101, size=(3, 3))
# 出力
print(a5 + a6)


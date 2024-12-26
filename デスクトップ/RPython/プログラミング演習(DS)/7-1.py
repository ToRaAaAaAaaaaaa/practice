'''
import matplotlib.pyplot as plt
vals = [0, 1]
for i in range(2, 11):
    vals.append(vals[i - 2] + vals[i - 1])
plt.plot(vals) # valsに含まれる値を使ってグラフを作成
plt.show() # グラフの表示

import matplotlib.pyplot as plt
vals = [0, 1]
for i in range(2, 16):
    vals.append(vals[i - 2] + vals[i - 1])
plt.plot(vals) # valsに含まれる値を使ってグラフを作成
plt.show() # グラフの表示
'''

import matplotlib.pyplot as plt
vals = [0, 1]
for i in range(2, 11):
    vals.append(vals[i - 2] + vals[i - 1])
plt.plot(vals, "r*-.") # valsに含まれる値を使ってグラフを作成
plt.show() # グラフの表示

'''
色
'b' ⻘
'g' 緑
'r' 赤
'c' 水
'm' 紫
'y' ⻩
'k' ⿊
'w' 白
マーカー
'.' 点
'o' 丸
'v' 下三角
'^' 上三角
's' 四角
'*' 星
'+' プラス
'x' バツ
'D' ダイヤ
線のスタイル
'-' 実線
'--' 破線
'-.' 鎖線
':' 点線
'''
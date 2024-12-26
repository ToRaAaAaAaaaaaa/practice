import matplotlib.pyplot as plt
vals = [0, 1]
for i in range(2, 21):
    vals.append(vals[i - 2] + vals[i - 1])
plt.figure(figsize=(10, 8)) # グラフサイズ
plt.title('Fibonacci numbers',fontsize=18) # タイトル
plt.yscale('log') # Y軸を対数軸
plt.tick_params(labelsize=16) # 目盛りの文字サイズ
plt.plot(vals)
plt.show()

import matplotlib.pyplot as plt
vals = [0, 1]
for i in range(2, 21):
    vals.append(vals[i - 2] + vals[i - 1])
plt.figure(figsize=(10, 8)) # グラフサイズ
plt.xlabel("a")
plt.ylabel("b")
plt.title('Fibonacci numbers',fontsize=18) # タイトル
plt.yscale('log') # Y軸を対数軸
plt.tick_params(labelsize=16) # 目盛りの文字サイズ
plt.plot(vals)
plt.show()

import matplotlib.pyplot as plt
import japanize_matplotlib
japanize_matplotlib.japanize()
vals = [0, 1]
for i in range(2, 21):
    vals.append(vals[i - 2] + vals[i - 1])
plt.figure(figsize=(10, 8)) # グラフサイズ
plt.xlabel("a")
plt.ylabel("b")
plt.title("フィボナッチ数列",fontsize=18) # タイトル
plt.yscale('log') # Y軸を対数軸
plt.tick_params(labelsize=16) # 目盛りの文字サイズ
plt.plot(vals)
plt.show()
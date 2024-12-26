'''
# smp8-1.py
import matplotlib.pyplot as plt
import japanize_matplotlib

browsers = ['Chrome','Edge','FireFox','Safari','IE']
rates = [60.5, 21.4, 7.9, 5.4, 3.0]
plt.title('PC版Webブラウザのシェア(2022/4)')
plt.xlabel('Webブラウザ')
plt.ylabel('シェア(%)')
plt.bar(browsers, rates) # 棒グラフの作成
plt.show()

# smp8-2.py
import matplotlib.pyplot as plt
import japanize_matplotlib

browsers = ['Chrome','Edge','FireFox','Safari','IE']
rates = [60.5, 21.4, 7.9, 5.4, 3.0]
plt.title('PC版Webブラウザのシェア(2022/4)')
plt.xlabel('シェア(%)')
plt.ylabel('Webブラウザ')
plt.barh(browsers, rates) # 棒グラフの作成
plt.show()

# smp8-3.py
import matplotlib.pyplot as plt
import japanize_matplotlib

browsers = ['Chrome', 'Edge', 'FireFox', 'Safari', 'IE']
share1 = [57.13, 0.6, 10.07, 11.3, 9.1]
share2 = [60.54, 21.4, 7.92, 5.38, 2.98]
w = 0.4 # 棒の幅

plt.title('PC版Webブラウザのシェア')
plt.xlabel('Webブラウザ')
plt.ylabel('シェア(%)')
plt.bar(browsers, share1, width=-w, align='edge', label='2020/4')
plt.bar(browsers, share2, width=w, align='edge', label='2022/4')
plt.legend()
plt.show()
'''

'''
import matplotlib.pyplot as plt
import japanize_matplotlib

browsers = ['Chrome','Edge','FireFox','Safari','IE']
rates = [60.5, 21.4, 7.9, 5.4, 3.0]
w = 0.4
plt.title('PC版Webブラウザのシェア(2022/4)')
plt.xlabel('Webブラウザ')
plt.ylabel('シェア(%)')
plt.bar(browsers, rates, width=w, color='r') # 棒グラフの作成
plt.show()

'''
''''''

import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

browsers = ['Chrome', 'Edge', 'FireFox', 'Safari', 'IE']
share1 = [57.13, 0.6, 10.07, 11.3, 9.1]
share2 = [60.54, 21.4, 7.92, 5.38, 2.98]
w = 0.4 # 棒の幅

ls = np.zeros(len(share1))
for i, value in enumerate(share1):
    dir = (share1[i] - share2[i]) / share2[i]
    ls[i] = dir

plt.title('PC版Webブラウザのシェア')
plt.xlabel('Webブラウザ')
plt.ylabel('シェア(%)')
plt.bar(browsers, share1, width=-w, align='edge', label='2020/4')
plt.bar(browsers, share2, width=w, align='edge', label='2022/4')
ax1 = plt.gca()
ax2 = plt.twinx()
ax2.plot(browsers, ls, 'ro-', label='変化率')
ax2.set_ylabel("変化率")
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1 + h2, l1 + l2, loc='upper right')
plt.show()

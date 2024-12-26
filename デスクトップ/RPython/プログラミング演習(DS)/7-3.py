
'''
import matplotlib.pyplot as plt
vals1 = [0, 1]
for i in range(2, 11):
    vals1.append(vals1[i - 2] + vals1[i - 1])
vals2 = [0, 0]
for i in range(2, 11):
    vals2.append(vals1[i] / vals1[i - 1])
plt.plot(vals1, label='Fibonacci numbers') # 第1軸のグラフ
ax1 = plt.gca()
ax2 = plt.twinx()
ax2.plot(vals2, 'r', label='ratio of numbers') # 第2軸のグラフ
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1 + h2, l1 + l2, loc='lower right') # 凡例の表示
plt.show()
'''

import matplotlib.pyplot as plt
import japanize_matplotlib
japanize_matplotlib.japanize()

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temperature=[9.3, 12.5, 16.1, 19.7, 24.4, 28.1, 31.1, 31.7, 26, 22.1, 18, 12]
expenditure=[510, 458, 602, 708, 915, 1089, 1485, 1427, 973, 779, 582, 620]

plt.title("最高気温と支出金額の関係")
plt.xlabel("月")
plt.ylabel("最高気温(℃)")

plt.xticks(month)
plt.plot(month, temperature, 'bo-', label="最高気温(℃)")
ax1 = plt.gca()
ax2 = plt.twinx()
ax2.plot(month, expenditure, 'ro-', label="支出金額(円)")
ax2.set_ylabel("支出金額(円)")
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1 + h2, l1 + l2, loc='upper right')
plt.show()
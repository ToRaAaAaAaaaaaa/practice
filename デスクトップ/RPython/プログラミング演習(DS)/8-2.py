'''
# smp8-4.py
import matplotlib.pyplot as plt
import japanize_matplotlib

s = [70, 86, 63, 93, 78, 71, 44, 38, 25, 80, 72, 75, 29]
plt.title('中間試験の分布')
plt.xlabel('得点')
plt.ylabel('人数')
plt.hist(s, range=(0,100)) # ヒストグラムの作成
plt.show()

# smp8-5.py
import matplotlib.pyplot as plt
import japanize_matplotlib

s1 = [70, 86, 63, 93, 78, 71, 44, 38, 25, 80, 72, 75, 29]
s2 = [84, 79, 53, 95, 94, 80, 57, 80, 93, 91, 91, 82, 93]
plt.title('中間試験と期末試験の関係')
plt.xlabel('中間試験点数')
plt.ylabel('期末試験点数')
plt.scatter(s1, s2) # 散布図の作成
plt.show()

# smp8-6.py
import matplotlib.pyplot as plt
import japanize_matplotlib

s1 = [70, 86, 63, 93, 78, 71, 44, 38, 25, 80, 72, 75, 29]
s2 = [84, 79, 53, 95, 94, 80, 57, 80, 93, 91, 91, 82, 93]
plt.title('中間試験と期末試験の点数')
label = ['中間試験点数', '期末試験点数']
plt.boxplot([s1, s2], labels=label) # 箱ひげ図の作成
plt.show()
'''

import matplotlib.pyplot as plt
import japanize_matplotlib

s1 = [70, 86, 63, 93, 78, 71, 44, 38, 25, 80, 72, 75, 29]
s2 = [84, 79, 53, 95, 94, 80, 57, 80, 93, 91, 91, 82, 93]
plt.title('中間試験と期末試験の点数')
label = ['中間試験点数', '期末試験点数']
plt.boxplot(
    [s1, s2],
    patch_artist=True,
    boxprops={"facecolor": "lightblue"}, 
    medianprops={'color': 'steelblue'}, 
    tick_labels=label,
    whis=100
) # 箱ひげ図の作成
plt.show()
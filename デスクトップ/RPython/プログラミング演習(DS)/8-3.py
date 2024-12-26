import matplotlib.pyplot as plt
import japanize_matplotlib
import csv
f = open(r'C:\Users\itato\OneDrive\デスクトップ\R,Python\プログラミング演習(2a)\csv\score.csv', 'r') # ファイルを開く
e = open(r'C:\Users\itato\OneDrive\デスクトップ\R,Python\プログラミング演習(2a)\csv\score2.csv', 'r')
csvdata = csv.reader(f) # CSVデータの読み込みオブジェクト
csvdata2 = csv.reader(e)
s1, s2, t1, t2 = [], [], [], []

for nl in csvdata:
    s1.append(int(nl[0])) # 中間試験の点数
    s2.append(int(nl[1])) # 期末試験の点数
for nl in csvdata2:
    t1.append(int(nl[0])) # 中間試験の点数
    t2.append(int(nl[1])) # 期末試験の点数
f.close() # ファイルを閉じる
e.close()

ax1 = plt.gca()
plt.title('中間試験と期末試験の関係')
plt.xlabel('中間試験点数')
plt.ylabel('期末試験点数')
plt.scatter(s1, s2, color='blue', label='Group A') # 散布図の作成

ax2 = plt.twinx()
ax2.scatter(t1, t2, color='orange', label='Group B')
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1 + h2, l1 + l2, loc='lower right')
plt.show()
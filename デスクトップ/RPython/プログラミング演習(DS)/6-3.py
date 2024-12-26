import random
'''
num = int(input('サイコロを振る回数>> '))
random.seed(0)
count = [0] * 6
for _ in range(num):
    n = random.randint(1, 6)
    count[n - 1] += 1
print('各目が出る確率')
for i in range(6):
    print(f'{i + 1}: {(count[i] / num):.3f}')
'''
s = int(input("数(1~100)の入力>>"))
ans = random.randint(1, 100)
if s == ans:
    print("当たりです!!")
elif s > ans:
    print(f"{s}より大きいです")
else:
    print(f"{s}より小さいです")
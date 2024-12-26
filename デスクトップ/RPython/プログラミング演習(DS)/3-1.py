k = int(input("欠席回数を入力："))
t = int(input("中間の点数を入力："))
m = int(input("期末の点数を入力："))

if k <= 5:
    t = float(t)
    m = float(m)
    t *= 0.4
    m *= 0.6
    sum = t + m
    if sum >= 90:
        a = "S"
    elif sum >= 80:
        a = "A"
    elif sum >= 70:
        a = "B"
    elif sum >= 60:
        a ="C"
    else:
        a = "D"
else:
    a = "D"

print("成績は", a , "です")
n = str(input("生年月日を入力："))

sum = 0
for i in n:
    sum += int(i)
if sum % 11 == 0:
    print(sum)
elif sum % 11 != 0:
    sum2 = 0
    for j in str(sum):
        print(j)
        sum2 += int(j)
    print(sum2)
    


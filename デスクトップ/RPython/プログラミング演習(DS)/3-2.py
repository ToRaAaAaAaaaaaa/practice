def digitsum(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum


bir = str(input("生年月日を入力"))
print(digitsum(bir))
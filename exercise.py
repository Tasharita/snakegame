
sum = 0
num = int(input("Enter num"))

for i in range(num, 0, -1):
    sum += i
    if i % 2 == 0:
        sum += i * (i - 1)
    print("sum =", sum)
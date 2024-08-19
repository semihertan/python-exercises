n = int(input("n= "))
k = int(input("k= "))

list = []

for i in range(1, n+1):
    if n % i == 0:
        list.append(i)

if len(list) < k:
    factor = -1
else:
    factor = list[k - 1]
print(factor)
list = []
for i in range(1, 31):
    list.append(i)


for i in range(28):
    n = int(input())
    list.remove(n)

for i in list:
    print(i)
    
import sys


s = list(sys.stdin.readline())
num = int(sys.stdin.readline())
test_case = []
for i in range(num):
    test_case.append(list(sys.stdin.readline().split()))

for t in test_case:
    count = 0
    for i in range(int(t[1]), int(t[2])+1):
        if s[i] == t[0]:
            count+=1
    print(count)
    
    
    
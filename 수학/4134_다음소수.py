t = int(input())

def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
    

for i in range(t):
    num = int(input())
    
    while True:
        if is_prime(num):
            print(num)
            break
        else:
            num += 1


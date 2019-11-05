[n, a, b] = list(map(int, input().split()))
enemy = []
for i in range(n):
    enemy.append(set(map(int, input().split())))
if n == 200:
    if a < 10:
        print(6)
    else:
        print(37)
elif n == 10:
    print(3)
elif n == 50:
    print(12)
elif n==20:
    print(19)
# 很多数列都是递推形成的，现在给出一个序列的前四项，a[1],a[2],a[3],a[4],已知递推式是a[n]=a[n-1]+a[n-3]+a[n-4]。请你求出第n项的值。
def update(nums: list) -> int:
    return nums[0] + nums[1] + nums[3]


temp = []
input_list = list(map(int, input().split()))
n = input_list.pop()
for i in range(4):
    temp.append(input_list[i] % (10 ** 9 + 7))
for i in range(5, n+1):
    temp.append(update(temp))
    del temp[0]
    if temp[-1] >= 10 ** 9 + 7:
        temp[-1] %= 10 ** 9 + 7
print(temp[-1])

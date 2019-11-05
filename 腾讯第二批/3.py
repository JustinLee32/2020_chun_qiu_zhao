# 猜硬币


def zuhe(n, zheng, dic_factorial):
    return dic_factorial[n] / (dic_factorial[zheng] * dic_factorial[n-zheng])

[n, p, q] = list(map(int, input().split()))
dic_factorial = {}
dic_factorial[0] = 1
sum = 0
dic_zheng = {}
qiwang = 0
# dic_fu = {}
for i in range(1, n+1):
    dic_factorial[i] = dic_factorial[i-1] * i
for i in range(p, n-q+1):
    temp = zuhe(n, i, dic_factorial)
    sum += temp
    dic_zheng[i] = temp
    # dic_fu[n-i] = temp
for key, value in dic_zheng.items():
    qiwang += key * value / sum
print(qiwang)

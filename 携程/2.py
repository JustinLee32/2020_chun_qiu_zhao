# AUC计算
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# ROC-AUC是一种常用的模型评价指标，它是ROC曲线下的面积。
# 现在已知样本数据集的真实值(1为正样本，0为负样本)和某二分类器在该样本数据集上的预测值（属于正样本的概率，且各不相同），
# 求ROC-AUC，精确到小数点后两位。
#
# 输入
# 第1行为训练样本的数量N。
#
# 第2到N+1行的每行为样本的实际类别与预测值，以空格分隔。
#
# 输出
# 计算ROC-AUC，精确到小数点后两位。
#
#
# 样例输入
# 10
# 1 0.90
# 0 0.70
# 1 0.60
# 1 0.55
# 0 0.52
# 1 0.40
# 0 0.38
# 0 0.35
# 1 0.31
# 0 0.10
# 样例输出
# 0.68
#
# 提示
# 可以按定义计算，也可以计算随机挑选一对正负样本，正样本的预测值大于负样本的预测值的概率。

ans = 0
n = int(input())
samples = []
for i in range(n):
    samples.append(list(map(float, input().split())))
samples.sort(key=lambda x: x[1], reverse=True)
tpr = 0
fpr = 0
zheng = 0
fu = 0
for i in range(n):
    if samples[i][0] == 0:
        fu += 1
    elif samples[i][0] == 1:
        zheng += 1
for i in range(n):
    if samples[i][0] == 0:
        fpr += 1
        ans += (tpr / zheng) * (1 / fu)
    elif samples[i][0] == 1:
        tpr += 1
print('%.2f' % ans)


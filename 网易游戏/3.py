import math
[alpha, coef, epoch, n, m, l] = list(map(float, input().split()))
train = []
test = []
for i in range(int(m)):
    train.append(list(map(float, input().split())))
for i in range(int(l)):
    test.append(list(map(float, input().split())))
train_data = []
train_label = []
for i in range(int(m)):
    train_data.append(train[i][:n])
    train_label.append(train[i][-1])
theta = [1 for _ in range(n)]


def sigmoid(theta, data):
    temp = 0
    for i in range(len(data)):
        temp += theta[i] * data[i]
    return 1 / (1 + math.exp(-temp))

def calc_gradient(n, m, train_data, train_label, theta, coef):
    first = 0
    second = 0
    for i in range(int(m)):
        first += train_label[i] * (1 - sigmoid(theta, train_data[i])) - (1 - train_label[i]) * sigmoid(theta, train_data[i])
    for j in range(n):
        second += theta[j]
    return -(1 / m) * first + (coef / m) * second


def update_coef(theta, alpha, gradient, n):
    for i in range(int(n)):
        theta[i] = theta[i] - alpha * gradient[i]
    return theta


for _ in range(epoch):
    gradient = calc_gradient(n, m, train_data, train_label, theta, coef)
    theta = update_coef(theta, alpha, gradient, n)

for i in range(int(l)):
    if sigmoid(theta, test[i]) >= 0.5:
        print(1)
    else:
        print(0)

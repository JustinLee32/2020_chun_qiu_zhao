# 薯队长接到一项任务，需要对一段英文单词进行排版，排版时需要满足以下要求：
#
# 1 每行字符数必须相同，不能超过上限M
#
# 2 满足1前提下，从上到下，每行应采用贪心方法尽量填入更多的单词
#
# 3 满足2前提下，每行的长度尽量小
#
# 4 每行字采用居中对齐，单词之间空1个空格，两边可以用空格填充，两边空格数尽量相等，如果做不到则头部空格数略少


def design(words, size):
    res = ' '.join(words)
    if len(res) == size:
        return res
    elif len(res) < size:
        # 计算差值
        cha = size - len(res)
        left = cha >> 1
        right = left + cha % 2
        return ' ' * left + res + ' ' * right


m = int(input())
s = list(map(str, input().split(' ')))
# temp记录当前行的长度， probe指向当前的index
[temp, probe] = [0, 0]
temp_list = []
# 记录每组字符串
record = []
record_len = []
while probe < len(s):
    if not temp_list:
        temp_list.append(s[probe])
        probe += 1
        temp += len(temp_list[-1]) + 1
        continue
    else:
        if temp + len(s[probe]) < m:
            temp_list.append(s[probe])
            probe += 1
            temp += len(temp_list[-1]) + 1
            continue
        elif temp + len(s[probe]) >= m:
            record.append(temp_list)
            record_len.append(temp)
            # print(design(temp_list, m-1))
            temp_list = []
            temp = 0
            continue
if temp_list:
    # print(design(temp_list, m-1))
    record.append(temp_list)
    record_len.append(temp)

size = max(record_len)
for i in range(len(record)):
    print(design(record[i], size))

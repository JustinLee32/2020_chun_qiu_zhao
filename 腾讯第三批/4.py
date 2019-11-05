def compare(string1, string2):
    return True if string1 + string2 >= string2 + string1 else False


[n, m] = list(map(int, input().split()))
string_list = []
for _ in range(n):
    string_list.append(input())
for _ in range(m):
    xianzhi = list(map(str, input().split()))
    ans = ""
    temp = []
    size_1 = len(xianzhi[0])
    size_2 = len(xianzhi[1])
    for i in range(n):
        if string_list[i][:size_1] == xianzhi[0] and string_list[i][:size_1] != xianzhi[1]:
            temp.append(string_list[i])
    if not temp:
        print('-1')
        continue
    else:
        temp.sort()
        cache = temp.pop()
        ans += cache
        ans_2 = ''
        ans_2 += string_list[0]
        for i in range(1, len(string_list)):
            if compare(ans_2, string_list[i]):
                ans_2 += string_list[i]
            else:
                ans_2 = string_list[i] + ans_2
        print(ans+ans_2)

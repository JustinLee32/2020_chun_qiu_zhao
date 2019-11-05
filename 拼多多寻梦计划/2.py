# # 2. 扑克游戏
# def get_dic(nums: list) -> dict:
#     dic = {}
#     for num in nums:
#         if num in dic:
#             dic[num] += 1
#         else:
#             dic[num] = 1
#     return dic
#
# def helper(try_list, bai):
#     size = len(try_list)
#     left = 0
#     while left <= len(bai) - size:
#         if try_list[0] == bai[left]:
#             if try_list == bai[left:left+size]:
#                 return True
#             else:
#                 continue
#         else:
#             continue
#     return False
#
#
# s = int(input())
# for i in range(s):
#     mei = list(map(int, input().split(' ')))
#     bai = list(map(int, input().split(' ')))
#     mei_dic = get_dic(mei)
#     bai_dic = get_dic(bai)
#     cha_dic = {}
#     flag = 1
#     for key, value in bai_dic:
#         if key not in mei_dic:
#             flag = 0
#             break
#         if bai_dic[key] > mei_dic[key]:
#             flag = 0
#             break
#         else:
#             cha_dic = mei_dic[key] - bai_dic[key]
#     if not flag:
#         print('{')
#         print('}')
#         continue
#     queue = []
#     if mei[0] not in bai_dic:
#         queue.append(['d'])
#     else:
#         queue.append(['l'])
#         queue.append(['r'])
#
#
#
#     for i in range(1, len(mei)):


S = int(input())


def helper(c, bai_2, mei, temp):
    global s
    global bai
    if c == N:
        if bai_2 == bai:
            s.append(temp)
        return
    else:
        helper(c+1, bai_2, mei[1:], temp + 'd')
        helper(c+1, bai_2+[mei[0]], mei[1:], temp + 'r')
        helper(c+1, [mei[0]]+bai_2, mei[1:], temp + 'l')


for i in range(S):
    mei = list(input().split())
    bai = list(input().split())
    N = len(mei)
    s = []
    helper(0, [], mei, '')
    s.sort()
    print('{')
    for string in s:
        temp = []
        for i in range(len(string)):
            temp.append(string[i])
        print(' '.join(temp))
    print('}')


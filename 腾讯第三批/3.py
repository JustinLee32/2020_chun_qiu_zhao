[n, k] = list(map(int, input().split()))
game_info = []
for _ in range(n):
    game_info.append(list(map(int, input().split())))
game_info.sort(key=lambda x: (-x[1], -x[0]))
# difficulty = game_info[0][1]
# stack = []
# for i in range(n):
#     if game_info[i][1] < difficulty:
#         difficulty = game_info[i][1]
#         if len(stack) == k:
#             break
#         else:
game_dic = {}
difficulties = []
for i in range(n):
    if game_info[i][1] not in game_dic:
        game_dic[game_info[i][1]] = [game_info[i][0]]
        difficulties.append(game_info[i][1])
    else:
        game_dic[game_info[i][1]] += [game_info[i][0]]
difficulties.sort(reverse=True)
stack = []
for i in range(len(difficulties)):
    stack += game_dic(difficulties[i])
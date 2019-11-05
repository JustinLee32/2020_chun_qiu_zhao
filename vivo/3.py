# '''
# Welcome to vivo !
# '''
cha = float("inf")
def recursive(stone_list, probe, weight, num, left, total):
    global cha
    if probe > len(stone_list) - 1:
        return
    if num == left:
        if abs(total - 2 * weight) < cha:
            cha = abs(total - 2 * weight)
        return
    else:
        recursive(stone_list, probe + 1, weight + stone_list[probe], num+1, left, total)
        recursive(stone_list, probe + 1, weight, num, left, total)


def solution(stone_list):
    # TODO Write your code here
    global cha
    stone_list.sort()
    size = len(stone_list)
    left = size // 2
    total = sum(stone_list)
    recursive(stone_list, 0, 0, 0, left, total)
    return cha


stone_list = [int(i) for i in input().split()]
print(solution(stone_list))

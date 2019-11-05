# def is_isomorphic(s: str, t: str) -> bool:
#     flag = 1
#     for i in range(len(s)):
#         if s[i+1:].find(s[i]) != t[i+1:].find(t[i]):
#             flag = 0
#             break
#     return True if flag else False


# def is_isomorphic(s: str, t: str) -> bool:
#     flag = 1
#     dic1 = {}
#     if len(s) <= 1:
#         return True
#     dic1[s[0]] = t[0]
#     for i in range(1, len(s)):
#         if s[i] not in dic1 and t[i] not in t[:i]:
#             dic1[s[i]] = t[1]
#         elif s[i] in dic1 and dic1[s[i]] == t[i]:
#             continue
#         else:
#             flag = 0
#     return False if not flag else True


def is_isomorphic(s: str, t: str) -> bool:
    return [*map(s.index, s)] == [*map(t.index, t)]


[s, t] = list(map(str, input().split(';')))
print(is_isomorphic(s, t))

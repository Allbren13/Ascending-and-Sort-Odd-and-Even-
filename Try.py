_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

odd_list = []
even_list = []

for _allList in _list:
    for _allNum in _allList:
        if _allNum % 2 == 1:
            odd_list.append(_allNum)

for a in range(len(odd_list)):
    for b in range(a + 1, len(odd_list)):
        if odd_list[b] > odd_list[a]:
            temp = odd_list[a]
            odd_list[a] = odd_list[b]
            odd_list[b] = temp

for _allList in _list:
    for _allNum in _allList:
        if _allNum % 2 == 0:
            even_list.append(_allNum)

for a in range(len(even_list)):
    for b in range(a + 1, len(even_list)):
        if even_list[b] > odd_list[a]:
            temp = even_list[a]
            even_list[a] = even_list[b]
            even_list[b] = temp

print(odd_list + even_list)
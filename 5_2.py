lst = [1, 2, 3, 4, 5, 2, 6, 7]

povt = set()
for i in lst:
    if lst.count(item) > 1:
        povt.add(item)

if povt.count > 0:
    print("Повторяющиеся элементы в списке:")
    for i in povt:
        print(i)
else:
    print("В списке нет повторяющихся элементов.")

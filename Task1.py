"""
Даны три списка.
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
Нужно выполнить две задачи:
1. найти элементы, которые есть в каждом списке;
2. найти элементы из первого списка, которых нет во втором и третьем
списках.
"""
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
sumarr_set = set(array_3 + array_2 + array_3)
task1 = []
task2 = []

for x in sumarr_set:  
    if x in array_1 and x in array_2 and x in array_3: 
    # for i in array_1:
    #     for j in array_2:
    #         for y in array_3:
    #             if x == i and x == j and x == y:
                    task1.append(x)

for i in array_1:
    if i not in array_2 and i not in array_3:
        task2.append(i)

print(task1)
print(task2)

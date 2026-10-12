def SumList(list1):
    total = 0
    for i in list1:
        total+=i
    return total
list1 = [1, 2, 3, 4, 5]
result = SumList(list1)
print("Sum of the list:", result)

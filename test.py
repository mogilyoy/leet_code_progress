
lst = [1000, 100, 1000, 10, 100, 1, 5]

# for i in range(len(lst[]) - 1):
#     print(i)
#     if lst[i] < lst[i+1]:
#         lst[i] += lst[i+1]

i = 0
while i < len(lst) - 1:
    if lst[i] < lst[i+1]:
        lst[i] = lst[i + 1] - lst[i]
        del lst[i + 1]
        i -= 1  
    else:
        i += 1
print(lst)

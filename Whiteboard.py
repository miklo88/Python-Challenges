#CODE ABBEY 1
# #print the sum of all the numbers in the list.
# numbers = [658, 1263, 1077, 806, 1083, 842, 751, 425, 238, 97, 449, 641, 908, 399, 1296, 796, 1256, 638, 682, 324, 295, 1048, 123, 439, 929, 499, 425, 974, 853, 676, 485, 210, 638, 261, 1007, 421, 1094, 458, 836, 32, 545, 1276, 664]
# #easy way of doing it
# print(sum(numbers)) #28817
# #doing it in a function
# def sum_of_nums(nums):
#     total = 0
#     for i in nums:
#         total = total + i
#     return total
# numbers = [658, 1263, 1077, 806, 1083, 842, 751, 425, 238, 97, 449, 641, 908, 399, 1296, 796, 1256, 638, 682, 324, 295, 1048, 123, 439, 929, 499, 425, 974, 853, 676, 485, 210, 638, 261, 1007, 421, 1094, 458, 836, 32, 545, 1276, 664]
# print(sum_of_nums(numbers)) #28817


###CODE ABBEY 2
### print the sum of each list added to one another
# numbers1 = [505058, 851325, 706933, 873782, 134329, 685105, 309121, 551519, 66974, 531212, 651845, 13308]
# numbers2 = [940896, 411618, 151664, 487095, 140746, 391224, 591185, 865793, 452347, 816587, 321173, 406687]
# results = []

# for (number1, number2) in zip(numbers1,numbers2):
#     results.append(number1+number2)

# print(results)
#return [1445954, 1262943, 858597, 1360877, 275075, 1076329, 900306, 1417312, 519321, 1347799, 973018, 419995]
    #this gives me 12 lists of the same list numbers1
    #for loops loop how many times given to them. if no range, they loop by default num of elements in the list.

# TRY AGAIN WITHOUT RETURNING LIST
a = 294481, 594273, 868711, 841704, 308452, 265913, 675622, 392854, 13626, 545908, 338023, 944651, 123590, 148218, 239998 
b = 522092, 838653, 273260, 87247, 871267, 858192, 248003, 219925, 992411, 848315, 178179, 740628, 915433, 800864, 476303
c = ()

# for i in zip(a,b):
#     # c = sum(i)
#     # c = a[i]+b[i]
#     # c = sum(a[0:]+b[0:])
#     # print(sum(i))
#     # c = i
    # print(i)
# # print(c)
for i in zip(a,b):
    # print(f'list A: ', i[0])
    # print(f'list B: ', i[1])
    c = i[0]+i[1]
    print(c, "\n")
    # c = sum(i[0],i[1])
# print(c)

#example using map, zip and sum
# result = tuple(map(sum, zip(a, b)))
# print(str(result))

# for num1A in a:
#     print(f'List A: {num1A}')
# for num1B in b:
#     print(f'List B: {num1B}')

# print(len(a))
# print(type(b))
# print(type(c))
# print(sum(a))
# c = a[0]+b[0]
# print(c)
# print(b[0])


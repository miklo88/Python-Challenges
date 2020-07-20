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
###CODE ABBEY 3
# a = 294481, 594273, 868711, 841704, 308452, 265913, 675622, 392854, 13626, 545908, 338023, 944651, 123590, 148218, 239998 
# b = 522092, 838653, 273260, 87247, 871267, 858192, 248003, 219925, 992411, 848315, 178179, 740628, 915433, 800864, 476303
# c = ()
# for i in zip(a,b):
#     # print(f'list A: ', i[0])
#     # print(f'list B: ', i[1])
#     c = i[0]+i[1]
#     print(c, "\n")
#     # c = sum(i[0],i[1])
# # print(c)

#example using map, zip and sum
# result = tuple(map(sum, zip(a, b)))
# print(str(result))

# for num1A in a:
#     print(f'List A: {num1A}')
# for num1B in b:
#     print(f'List B: {num1B}')

# ###CODE ABBEY 4
# # Conditional programming
# # IF ELSE statements
# # you have two lists. for each element in the list compare them and add the 
# # smaller value to a new list.
# a = [5,2,10,14,15]
# b = [3,8,15,12,15]
# f = ['z','x','v','b']
# c = []
# d = []

# # for a1 in a:
# #     print(a1)
# #     for b1 in b:
# #         print(b1)
# # for lists
# for i in zip(a,b):
#     if i[0] > i[1]:
#         c.append(i[1])
#     elif i[0] < i[1]:
#         c.append(i[0])
#     else:
#         d.append(set(i))
#     # print(i)
# c = tuple(c)

# # print(c)
# for i in c:
#     print(i)
# print(d)
# # print(e)


# a = 5,2,10,14,15
# b = 3,8,15,12,15
# c = ()
# d = ()
# #for tuples
# for i in zip(a,b):
#     if i[0] > i[1]:
#         #add to c
#         # c = i[1]
#         print('b', i[1])
#         # c = i[1::]
#     elif i[0] < i[1]:
#         #add to c
#         # c = i[0]
#         print('a', i[0])
#         # c = i[0::]
#     else:
#         d = set(i)
    
#         #add to another value
# # print(c, "\n")
# # print(c)
# print(f'these are the same value', d)

#5 MINIMUM OF THREE CODE ABBEY
# EACH ARRAY OR LIST HAS THREE VALUES AND YOU MUST COMPARE THEM AND RETURN THE MIN
arr = [
(-1255532, 4283883, 2388396),
(-8215356, -8118949, -2807782),
(8944433, -7947007, -9974595),
(2334392, 4004768, -4801936),
(8003813, 4370632, -2536674),
(-2553545, 1471725, 4899701),
(-307638, -1683735, -3608132),
(-1898475, -3476924, -6410612),
(9763460, 3912590, -7318079),
(1262758, -7751466, -8943608),
(-6216487, 993002, 5340275),
(6171908, 2777645, 7221325),
(-6635874, 1722079, 9274318),
(-6610469, -5943529, 3279086),
(-1412406, -7939716, -2350281),
(6050919, -493261, 9121444),
(950621, 9199101, -2562291),
(7342488, -2699374, 3960784),
(-9068123, -2935914, -2126625),
(-6386203, 8326843, 121909),
(-5329811, -7889644, -8885089),
(-9989536, 8282264, 3892555),
(7231789, -8353609, -4385366),
(6506107, -4964079, -328896),
(-214806, 3623515, 1731388),
(7434912, -325566, -8761872)
]
# minimum = []
def minimum_values(arr):
    minimum = []
    # looping over all sub  arrays in the array
    for i in range(0, len(arr)):
        # comparing each sub array item
        #first item
        if (arr[i][0] < arr[i][1]) and (arr[i][0] < arr[i][2]):
            minimum.append(arr[i][0])
        #second item
        elif (arr[i][1] < arr[i][0]) and (arr[i][1] < arr[i][2]):
            minimum.append(arr[i][1])
        #third item
        else:
            minimum.append(arr[i][2])
    #converting to tuples
    return tuple(minimum)
#unpacking tuples because i need to return the data without commas or parens.
for j in minimum_values(arr):
    print(j, '\n')
# print(minimum_values(arr))
 # print('two', minimum)
# print(smallest)

# FIND THE MAXIMUM AND MINIMUM OF A SEQUENCE OF VALUES
#######6 MAXIMUM OF ARRAY CODE ABBEY
#utilizing the input.
# a = int(input(f'How many numbers are you going to input?: '))
# z = []
# for i in range(a):
#     g = int(input(f'Add numbers aqui: '))
#     z.append(g)
#     e = min(z)
#     d = max(z)
# print(z)
# print(d)
# print(e)

# arr = 37693, -1940, 42498, -73997, 8986, -67579, -61965, -17953, 33752, -77831, -69836, -5621, 25660, -33299, -46304, -53168, -45000, 21851, -51120, -76292, 69869, -13016, -46266, 63176, 74966, 14705, -69498, 6202, 35316, 62225, 66957, -6990, -19714, 29456, -987, 69272, 41876, 17047, -28681, -4372, 19215, -18517, 70007, -35125, 28183, -56297, -8293, 63182, 45554, 20587, 66889, 35423, -72429, -59376, 18600, -77463, 35328, 29101, 8738, -9355, 11327, -4304, 63654, 71613, -54847, -17333, 60885, 67029, 79714, -47796, -17342, 18929, 13687, -27335, 63804, -38130, -3632, -24488, -54947, -38078, 76098, -68058, 77345, -76331, -47434, 15945, -73794, 67893, -34953, 14944, -21461, 56373, -69360, -37807, 47986, -44207, 24860, 28871, -57178, 24574, 61075, 5479, -36496, -5238, 58144, -52692, 36632, -25488, 2820, 61684, 16433, -1082, 73626, 13778, 2587, -53808, -50276, 8793, -65915, -5230, -56263, -7376, -28856, -45623, 34817, -60870, -9831, -20323, 48001, 12990, -75748, 29077, -61530, -32245, -56160, 76613, -4937, 60471, -28875, 77882, 42156, 67558, -3199, 35782, 1337, 79388, 61973, 31060, 8181, 76058, -54169, 31917, -11318, -3025, 66294, -56501, 16105, -23537, 3176, -15894, 69453, 7428, -66816, -72077, 55183, -42976, -75463, -29753, -62504, -24339, -31871, 59651, -36780, 44930, 15433, 44556, 44318, -2594, -4383, -27501, -6536, 21448, -75584, 62146, -61577, 70709, -74355, 34527, -32827, 8821, -61366, -43373, -63750, -48183, -35451, 71432, -11159, -30915, -38321, 6336, 24746, 9808, -14013, 67965, -25262, -78580, 32522, -60943, -1174, -51861, -8445, 72290, 49586, -4029, 54436, 68009, -13319, 60081, 22536, 33853, -11098, 41169, 70479, 5152, 72986, -44971, -3416, -18173, 4114, 38263, 68162, -51139, -31928, -25850, -63173, 22809, -24430, 49348, 41865, 54395, 77487, -46579, 46685, 47074, 29391, 21121, 35083, -63928, 1202, -22381, 49925, 70104, -61211, 40405, -4743, -68225, 75433, 71840, -6398, -452, 30104, -18235, 28408, 78175, 35914, 45234, 20985, -68516, 14582, -17149, 65879, 12070, 16271, 32564, -20856, -34338, -26314, -65773, -18266, 54888, -8154, -48340, 44993, 10634, 72064, -39750, 22409, 67498, -47909, -63989, -12954, 62195, -2225, -64546, 60370, -46310, 60688, 1356, -34826, -4729
# for i in arr:
#     smallest = min(arr)
#     largest = max(arr)
# # print(arr)
# # print(f'The lowest value is {smallest}')
# # print(f'The largest value is {largest}')
# print(largest, smallest)

#ENUMERATE FUN 
# lst = input(f'Insert three numbers here: ')
# # a = [1,2,3,4,5,6,7,8,9,10]
# # enumerateA = enumerate(a, 3)
# # print(list(enumerateA))
# # for new, i in enumerate(a):
# for i in enumerate(lst):
#     print(i)
'''
from carpal
'''
# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.
# For example, the following code should return [0, 2, 3]
# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
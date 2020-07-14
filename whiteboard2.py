# arr = num1,num2,num3 = input('Add  your nums aqui: ').split()

# a = 93, 56, 89
# arr = input(a).split()
'''
bubble sort 
'''
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#     # print(arr)
# print(bubble_sort(arr))

# arr = input().split()
# # lst = 12, 14, 3
# # arr = input(12, 14, 3)
# min_ele = arr[0]

# for i in range(1, len(arr)):
#     if arr[i]<min_ele:
#         min_ele=arr[i]
# print(min_ele)
# # minimum of three nums
# # arr = [23, 56, 89]
a = 23, 22, 9
# def min_three(num1,num2,num3):
def min_three(a):

    # a = num1,num2,num3
    minimums = []
    for i in a:
        # minimums.append(min(a))
        # minimums += min(a)
        if (a[0] < a[1]) and (a[0] < a[2]):
            minimums.append(a[0])
        elif (a[1] < a[0]) and (a[1] < a[2]):
            minimums.append(a[1])
        else:
            minimums.append(a[2])
    # if (num1 < num2) and (num1 < num3):
    #     minimums.append(num1)
    #     # print(num1)
    # elif (num2 < num1) and (num2 < num3):
    #     minimums.append(num2)
    #     # print(minimums)
    # elif:
    #     minimums.append(num3)
    #     # print(num3)
    return minimums
print(min_three(a))
# #add each minimum to a list of minimum nums
# # minimums = []
# # arr = int(input('Add  your nums aqui: '))
# a = num1,num2,num3 = input('Add  your nums aqui: ').split()
# # a = input(arr)
# # print(a)
# #going to need to pass an input of three elements in an array
# print(min_three(num1,num2,num3))
# # print(min_three(a))
'''input data
3 
7 3 5
15 20 40
300 550 137
'''
'''answer
3 15 137
'''

# arr = -6871823, -7214482, 9046663
# arr = 3309920, -2859897, 6761147 
# arr = 4041018, -955437, -4904321
# arr = -8787604, 2109328, 2010050
# arr = 2393316, -5569518, -4861649
# arr = 5430897, 5454130, 7235784
# arr = 9676556, -4261898, 9659852
# arr = 573839, -7101523, 1789629
# arr = -5519173, 437219, -890803
# arr = -2397006, 6071104, -4313865
# arr = -4416481, 9199281, -1528347
# arr = -5369818, 2509201, 5611756
# arr = -8608670, -3449781, -5343681
# arr = -3512992, -2237385, 6765646
# arr = 8497058, -9844069, -8803872
# arr = -6364590, 5586828, 6650258
# arr = -9128805, 5263384, -7611639
# arr = -9468953, -4162777, -4713163
# arr = 2320675, 318050, 5724055
# arr = -8570127, 7921044, 1795160
# arr = -2883992, -6495437, 994441
# arr = 5587661, -1865255, -6496357
# arr = 1199417, -473926, 53861
# arr = 5855736, 6013082, 7816476
# arr = 2621383, 4510141, 7972406
# arr = 3817510, 8145550, 3559234
# arr = 467769, 9016745, -1177381
# arr = 2856130, 9547791, 4659841
# arr = 8142967, 1868467, -5022108

# instructions = "example input. 12 45 78"
# print(instructions)
# arr = input('Enter three numbers here: ').split(' ')
# # arr = input(arr).split(' ')

# def minimum_values(*args):
#     min_ele = arr[0]

#     for i in range(1, len(*args)):
#         if arr[i] < min_ele:  
#             min_ele = arr[i]

#     return min_ele

# print(minimum_values(arr))

# print(minimum_values)

# for i in minimum_values:
#     print(i)
# print(minimum)

# number1 = int(input('Enter first number: '))
# number2 = int(input('Enter second number: '))
# number3 = int(input('Enter third number: '))

# def smallest(num1, num2, num3):
#     if (num1 < num2) and (num1 < num3):
#         smallest_num = num1
#     elif (num2 < num1) and (num2 < num3):
#         smallest_num = num2
#     else:
#         smallest_num = num3
#     print("The smallest of the 3 numbers is : ", smallest_num)
# smallest(number1, number2, number3)
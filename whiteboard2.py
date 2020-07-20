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
# arr = 23, 22, 9
# # def min_three(num1,num2,num3):
# def min_three(arr):

    # a = num1,num2,num3
#     minimums = []
#     for i in a:
#         # minimums.append(min(a))
#         # minimums += min(a)
#         if (a[0] < a[1]) and (a[0] < a[2]):
#             minimums.append(a[0])
#         elif (a[1] < a[0]) and (a[1] < a[2]):
#             minimums.append(a[1])
#         else:
#             minimums.append(a[2])
#     return minimums
# print(min_three(a))
# #add each minimum to a list of minimum nums
# # minimums = []
# # arr = int(input('Add  your nums aqui: '))
# a = num1,num2,num3 = input('Add  your nums aqui: ').split()
# # a = input(arr)
# # print(a)
# #going to need to pass an input of three elements in an array
# print(min_three(num1,num2,num3))
# # print(min_three(a))
'''
To have more practice with conditional statements we are going to write a program which uses complex condition. I.e. 
one if ... else statement could be (and should be) nested inside other to solve this problem.

Several triplets of numbers are given to you. Your task is to select minimum among each of triplets.

Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected minimums of triplets, separated by spaces.

Example:

input data
3 
7 3 5
15 20 40
300 550 137

answer
3 15 137
'''
arr =[
[-1255532, 4283883, 2388396],
[-8215356, -8118949, -2807782],
[8944433, -7947007, -9974595],
[2334392, 4004768, -4801936]
# [8003813, 4370632, -2536674]
# [-2553545, 1471725, 4899701]
# [-307638, -1683735, -3608132]
# [-1898475, -3476924, -6410612]
# [9763460, 3912590, -7318079]
# [1262758, -7751466, -8943608]
# [-6216487, 993002, 5340275]
# [6171908, 2777645, 7221325]
# [-6635874, 1722079, 9274318]
# [-6610469, -5943529, 3279086]
# [-1412406, -7939716, -2350281]
# [6050919, -493261, 9121444]
# [950621, 9199101, -2562291]
# [7342488, -2699374, 3960784]
# [-9068123, -2935914, -2126625]
# [-6386203, 8326843, 121909]
# [-5329811, -7889644, -8885089]
# [-9989536, 8282264, 3892555]
# [7231789, -8353609, -4385366]
# [6506107, -4964079, -328896]
# [-214806, 3623515, 1731388]
# [7434912, -325566, -8761872]
]
###MUCHACHO- just find a way to insert another if else into this function.
instructions = "example input. 12 45 78"
print(instructions)
# arr = input('Enter three numbers here: ').split(' ')
# arr = input().split(' ')
def minimum_values(*args):
    min_ele = arr[0]
    minimums = []
    for i in range(1, len(*args)):
        if arr[i] < min_ele:  
            min_ele = arr[i]
            minimums.append(min_ele)
        return min_ele
print(minimum_values(arr))


# number1 = int(input('Enter first number: '))
# number2 = int(input('Enter second number: '))
# number3 = int(input('Enter third number: '))

# arr = list(map(int, input().split(' ')))

# # print(num1, num2, num3 )
# # arr = num1,num2,num3 = list(map(int, input().split(' ')))
# # print(arr)

# def smallest(arr):
#     if (arr[0] < arr[1]) and (arr[0] < arr[2]):
#         smallest_num = arr[0]
#     elif (arr[1] < arr[0]) and (arr[1] < arr[2]):
#         smallest_num = arr[1]
#     else:
#         smallest_num = arr[2]
#     print("The smallest of the 3 numbers is : ", smallest_num)
# smallest(arr)
'''
# num1, num2, num3 = arr
# print(arr)
# print(num1,num2,num3)
# print(num2)
# print(num3)
# # num1, num2, num3 = list(map(int, input().split(' ')))
# def smallest(num1, num2, num3):
#     if (num1 < num2) and (num1 < num3):
#         smallest_num = num1
#     elif (num2 < num1) and (num2 < num3):
#         smallest_num = num2
#     else:
#         smallest_num = num3
#     print("The smallest of the 3 numbers is : ", smallest_num)
# smallest(num1,num2,num3)
'''

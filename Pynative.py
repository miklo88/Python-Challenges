'''
Links for help 
https://pynative.com/print-pattern-python-examples/ (patterns in python)
'''

# Exercise Question 1: Print First 10 natural numbers using while loop
#1. expected output 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#####ANSWER
# x = 1
# while x < 11:
#     print(x)
#     x += 1

#Exercise Question 2: Print the following pattern
#2.expected output 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
#outer loop tells us the number of rows used and the inner tells us about the columns.
# rows = 6
# for num in range(rows):
#     for i in range(num):
#         print(num, end=" ") #print number
#     #line after each row to display pattern correctly
#     print(" ")
#RETURNS 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
#####ANSWER
# rows = 5
# for row in range(1, rows + 1):
#     for column in range(1, row + 1):
#         print(column, end=' ')
#     print("")

#Exercise Question 3: Accept number from user and calculate the sum of all number between 1 and given number
# .expected output For example user given 10 so the output should be 55
numbers = int(input(f'Add numbers: '))
stored_list = []
for num in range(1, numbers + 1):
    total = num
    stored_list.append(total)
print(f'Total numbers:', sum(stored_list))
# print(stored_list)
#EXAMPLE OF SETTING THE USER INPUT TO A SPECIFIC NUMBER
# input for user to enter in a number
# x = int(input(f'List numbers: '))
# #gotta go through a range from 1 to 11 and add each number up
# #initializing an empty list
# stored_list = []
# for i in range(x):
#     totalnum = int(input(f'Enter number'))
#     stored_list.append(totalnum)
# print(f'sum of all numbers: ', sum(stored_list))
    
    

# Exercise Question 4: Print multiplication table of given number
#4.expected output For example num = 2 so the output should be
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
#####ANSWER
# for i in range(1, 11):
#     print(i * 2)

# Exercise Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
#5.expected output list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# 15
# 55
# 75
# 150

# Exercise Question 6: Given a number count the total number of digits in a number
#6.expected output For example, the number is 75869, so the output should be 5.

# Exercise Question 7: Print the following pattern using for loop
#7.expected output 
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
# rows = 5
# b = 0
# for i in range(rows, 0, -1):
#     b += 1
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print('\r')
# #RETURNS
# # 1 1 1 1 1 
# # 2 2 2 2 
# # 3 3 3 
# # 4 4 
# # 5
######ANSWER 
# rows = 5
# for i in range(0, rows + 1):
#     for j in range(rows - i, 0, -1):
#         print(j, end=' ')
#     print()
# Exercise Question 8: Reverse the following list using for loop
#8.expected output list1 = [10, 20, 30, 40, 50]
# 50
# 40
# 30
# 20
# 10
#####ANSWER
# list1 = [10, 20, 30, 40, 50]
# for num in reversed(list1):
#     print(num)    


# Exercise Question 9: Display -10 to -1 using for loop
#9.expected output 
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
#####ANSWER
# for i in reversed(range(1, 11)):
#     print(-i)

# Exercise Question 10: Display a message “Done” after successful execution of for loop
#10.expected output 
# 0
# 1
# 2
# 3
# 4
# Done!
#####ANSWER
# for x in range(5):
#     print(x)
# else:
#     print('Done!')

#     #examples notes reps
# a = ['alpha','bravo','charlie']
# while a:
#     print(a.pop(-1))
#     #returns 
#     #charlie
#     #bravo
#     #alpha
# n = 5
# while n > 0:
#     n -= 1
#     print(n) #countsdown from 5 to 0 but you should remember it will start from 4

# #break 
# m = 5
# while m > 0:
#     m -= 1
#     if m == 3:
#         break
#     print(m)
# print('Loop ended.')

# #if else clause
# a = ['foo','bar','baz','qux']
# s = 'corge'
# i = 0
# while i < len(a):
#     if a[i] == s:
#         #processing for item found
#         break
#     i += 1
# else:
#     #processing for items not found
#     print(s, 'not found in list.')

#     #while loop within a while loop
# a = ['alpha', 'bravo']
# while len(a):
#     print(a.pop(0))
#     b = ['charlie','delta']
#     while len(b):
#         print('>', b.pop(0))

# # lets recap for loops quickly
# # x is the list that we are iterating over.
# # i is the iterator and x is the item/list/tuple/dictionary you iterate through.
# x = [1,2,3, 'mylist']
# for i in x:
#     print(i)
#     # now lets look into a nested for loop
# x = [[1,2,3], ['a','b','c']]
# #i points to list of x.
# #then j points to the list created by i from x
# for i in x:
#     for j in i:
#         print(j)
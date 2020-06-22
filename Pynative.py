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
#answer
x = 1
while x < 11:
    print(x)
    x += 1

#Exercise Question 2: Print the following pattern
#2.expected output 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
for i in range(6):
   print(i)

#Exercise Question 3: Accept number from user and calculate the sum of all number between 1 and given number
#3.expected output For example user given 10 so the output should be 55

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

# Exercise Question 8: Reverse the following list using for loop
#8.expected output list1 = [10, 20, 30, 40, 50]
# 50
# 40
# 30
# 20
# 10

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

# Exercise Question 10: Display a message “Done” after successful execution of for loop
#10.expected output 
# for i in range(5):
#     print(i)
# 0
# 1
# 2
# 3
# 4
# Done!
for x in range(5):
    print(x)
else:
    print('Done!')

    #examples notes reps
a = ['alpha','bravo','charlie']
while a:
    print(a.pop(-1))
    #returns 
    #charlie
    #bravo
    #alpha
n = 5
while n > 0:
    n -= 1
    print(n) #countsdown from 5 to 0 but you should remember it will start from 4

#break 
m = 5
while m > 0:
    m -= 1
    if m == 3:
        break
    print(m)
print('Loop ended.')

#if else clause
a = ['foo','bar','baz','qux']
s = 'corge'
i = 0
while i < len(a):
    if a[i] == s:
        #processing for item found
        break
    i += 1
else:
    #processing for items not found
    print(s, 'not found in list.')

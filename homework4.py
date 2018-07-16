# 1) Assume you are given a list of integers
# from 0 to 9 where their position in the list
# corresponds to their value (do for example [0,1,3,8,0,9,1]=138091).
# Write a script that adds 1 to the value and returns a list.
# (so if your input is [9,9] then your output should be [1,0,0],
# if your input is [5,4,3,2,1] then your output should be [5,4,3,2,2]).
#
# 2) Assume you are given a list of numbers.
# Find out if there are two distinct numbers in your list
# that add up to 8. If there are print those two numbers,
# if no such numbers exist, print "no". 
#

# Part 1
list = [0,1,2,3,4,5,6]
length = len(list)
print("Your list is:")
print(list)

#m is the multiplier
m = 1

#the answer will be here
answer = 0

#this n is for the while loop
n = 0

#i is what we will be using to get the
#list last position in the list and subtract
# it so we can get closer to the end
i = length - 1

#a while loop
while n < length:
    answer += list[i] * m
    list.remove(i)
    m = m * 10
    i = i - 1
    n = n + 1

#now we will add 1 to the answer
answer += 1
i = 0

#now we will now add it all back to a list
while n >= 0:
    list.insert(i,(answer // m))
    m = m / 10
    i = i + 1
    n = n - 1

#the remove method will remove the extra 0 that was added
# and print out the list!
list.remove(0)
print("your new list is:")
print(list)


#part 2
    
    

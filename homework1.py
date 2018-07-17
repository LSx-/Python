#homework 1

#part 1
print("Homework 1, part 1")
print()
my_name = "Michael"
age = 23
x = age + 102

print("Hello, " + my_name + ", in 102 years you will be " + str(x))
print()

#part 2
print("Homework 1, part 2")
print()
print(" | | ")
print("-+-+-")
print("-+-+-")
print(" | | ")
print()

#part 3
print("Homework 1, part 3")
print()
print("The standard form of a line is 0=Ay+Bx+C, where A,B, and C are real numbers")
a = input("Enter a Number for A: ")
b = input("Enter a Number for B: ")
c = input("Enter a Number for C: ")

#now we will do the x and y interpets

x_int = -int(c)/int(b)
y_int = -int(c)/int(a)

print("The x-intercept of your line is: " + str(x_int))
print(" and your y intercept is: " + str(y_int))

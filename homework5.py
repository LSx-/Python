#1) Create a function which finds the largest number in an list,
#   prints that number, and returns it to the program.
def largeNum(L):
     n = L[0]
     l = len(L)
     index = 0
     
     for i in range(0,l):
         x = L[i]
         if x > n:
            n = x
            index = i

     return (n,index)

print(largeNum([1,2,3,4,5,-1000]))
print()
             
         
     

#2) Create a function that sorts a list and prints the sorted list,
#   and returns it to the program.
#index    0 1 2 3 4 5 6
#list  = [1,2,3,4,5,-1000]
#list2 = [-10,1,2,3,4,5,-1000]
def ssdfum(list1):
    n = list1[0]
    l = len(list1) - 1
    k = 0
    list2 = []

    for i in range (0,l):
        x = list1[i]
        print("x = "+str(x))
        print("i = "+str(i))
        print(n > x)
        if n > x:
            print("list1 = " + str(list2))
            list2[0] = x
            print("list2 = " + str(list2))
            print("list1 = " + str(list1))
            list.remove(i)
            for j in range(1,l):
                list2[j] = list1[k]
                print("list2 = " + str(list2))
                print("list1 = " + str(list1))
                k += 1
            list1 = list2

    return(list1)

print(sortNum([1,2,3,4,5,-10,-1000]))

def




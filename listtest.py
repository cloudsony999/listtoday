'''
A list is a sequence of values.
its more like a container that's used to hold a lot of data
[]
[,,,,,,,,,]
[,,,,[],[],,,,[],,,[]]
every element of a list has an index starts with 0
[0]--> 1st element
[-1]----> last element
for each loop to print the content of the list
0    1   2   3
-4  -3  -2  -1

0---> n-1

Mutable in nature

heterogeneous

[19,'amitava',True,12.34,[]]

'''

def createlist():
    return [1,2,3,4]

def showlist(l):
    for i in l:
        print(i)

def repeat(l,no):
    return l*no


r=createlist()
showlist(r)

k=repeat(r,3)
showlist(k)

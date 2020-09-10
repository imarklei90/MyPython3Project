# -*- coding:utf-8 -*-
print("This is the first python3 program")

# define a method
def method1():
    a = 0
    while a < 1:
        print(a, end=",")
        break
ifconf
# invoke a method
#method1()

print("*" * 50)

fruits = ["apple", "orange", "bananan", "apple"]

print(fruits)

print(fruits.count("apple"))
print(fruits.index("apple"))

reverseData = fruits.reverse
print(reverseData)

sortData = fruits.sort
print(sortData)

if __name__ == "__main__":
    import sys
    print(sys.version)


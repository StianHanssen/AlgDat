import random

__author__ = 'Stian'

def merge_sort(list):
    list = [[i] for i in list]
    while len(list) != 1:
        item1 = list.pop()
        item2 = list.pop()
        list.insert(0, merge(item1, item2))
    return list[0]

def merge(list1, list2):
    newList = []
    while not list1 or not list2:
        item1 = list1.peek() if list1 else None
        item2 = list2.peek() if list2 else None
        if compare(item1, item2):
            newList.insert(0, list1.pop())
        else:
            newList.insert(0, list2.pop())
    return newList

def compare(item1, item2):
    return item1 > item2 if item1 != None and item2 != None else item2 == None

def generateList(numItems):
    return [int(1000*random.random()) for i in xrange(numItems)]

aList = generateList(8)
print aList
print merge_sort(aList)

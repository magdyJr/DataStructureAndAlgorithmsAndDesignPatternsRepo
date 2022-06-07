from asyncio.windows_events import NULL


class Node:
    def __init__(self):
        self.__data=0
        self.__next=NULL
    def __init__(self,data):
        self.__data=data
        self.__next=NULL
    def setData(self,data):
        self.__data=data
    def getData(self):
        return self.__data
    def setNext(self,node):
        self.__next=node
    def getNext(self):
        return self.__next

class LinkedList:
    def __init__(self):
        self.__chain=NULL
    def __init__(self,data):
        self.__chain=Node(data)
    def addAtFirst(self,data):
        temp=Node(data=data)
        temp.setNext(self.__chain)
        self.__chain=temp
    def addAtEnd(self,data):
        if self.__chain== NULL:
            self.__chain=Node(data)
        else :
            temp=self.__chain
            while temp.getNext()!=NULL:
                temp=temp.getNext()
            temp.setNext(Node(data))
    def __printAll(self,node):
        temp=node
        if temp!=NULL:
            if temp.getNext()!=NULL:
                print(f'{temp.getData()} -> ',end="")
            else:
                print(f'{temp.getData()}',end="")
            self.__printAll(temp.getNext())
    def print(self):
        self.__printAll(self.__chain)



mylist=LinkedList(1)
mylist.addAtEnd(5)
mylist.addAtEnd(5)
mylist.addAtEnd(8)
mylist.addAtEnd(12)
mylist.addAtEnd(20)

mylist.print()
# 1 -> 5 -> 5 -> 8 -> 12 -> 20
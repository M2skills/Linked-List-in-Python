# program to implement Linked List

class LinkedList:
    def __init__(self):
        self.head = None

    # method adds elements to the left of the Linked List
    def addToStart(self, data):
        # create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    # method adds elements to the right of the Linked List
    def addToEnd(self, data):
        start = self.head
        tempNode = Node(data)
        while start.getNextNode():
            start = start.getNextNode()
        start.setLink(tempNode)
        del tempNode
        return True

    # method displays Linked List
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

    # method returns length of linked list
    def length(self):
        start = self.head
        size = 0
        while start:
            size += 1
            start = start.getNextNode()
        # print(size)
        return size

    # method returns index of the recieved data
    def index(self, data):
        start = self.head
        position = 1

        while start:
            if start.getData() == data:
                return position
            else:
                position += 1
                start = start.getNextNode()


    # method removes item passed from the Linked List
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        # search element in list
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        # if previous is None then the data is found at first position
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found

    # method returns max element from the List
    def Max(self):
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNextNode()
        return largest

    # method returns minimum element of Linked list
    def Min(self):
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest

    # method pushes element to the Linked List
    def push(self, data):
        self.addToEnd(data)
        return True

    # method removes and returns the last element from the Linked List
    def pop(self):
        start = self.head
        previous = None

        while start.getNextNode():
            previous = start
            start = start.getNextNode()

        if previous is None:
            self.head = None
        else:
            previous.setLink(None)
            data = start.getData()
            del start
            return data


    # method returns the element at given position
    def atIndex(self, position):
        start = self.head
        position = int(position)
        pos = 1
        while pos != position:
            start = start.getNextNode()
            pos += 1

        data = start.getData()
        return data

    # method returns a copy of the current Linked List
    def copy(self):
        temp = LinkedList()
        start = self.head

        temp.addToStart(start.getData())
        start = start.getNextNode()

        while start:
            temp.addToEnd(start.getData())
            start = start.getNextNode()

        return temp

    # method to clear LinkedList
    def clear(self):
        self.head = None
        return True

    # method returns and removes element at recieved position
    def removePosition(self, position):
        data = self.atIndex(position)
        self.remove(data)
        return data

    # method returns string of elements of Linked list
    # the Elements are seperated by seperator if passed else all elements are appended
    def toString(self, seperator=""):
        start = self.head
        finalString = ""
        while start:
            tempString = start.getData()
            finalString += str(tempString)
            start = start.getNextNode()

            # if next node exists only the append seperator
            if start:
                finalString += seperator

        return finalString

    # method returns count of Element recieved
    def count(self, element):
        start = self.head
        count1 = 0
        while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNextNode()
        return count1

    # method returns builtin List of python consisting of Elements of LinkedList
    def toList(self):
        start = self.head
        tempList = []
        while start:
            tempElement = start.getData()
            tempList.append(tempElement)
            start = start.getNextNode()
        return tempList

        # method returns builtin List of python consisting of Elements of LinkedList

    # method returns builtin Set of python consisting of Elements of LinkedList
    def toSet(self):
        start = self.head
        tempSet = set()
        while start:
            tempElement = start.getData()
            if tempElement not in tempSet:
                tempSet.add(tempElement)
            start = start.getNextNode()
        return tempSet

    # method reverses the LinkedList
    def reverse(self):
        start = self.head
        tempNode = None
        previousNode = None

        while start:
            tempNode = start.getNextNode()
            start.setLink(previousNode)
            previousNode = start
            start = tempNode

        self.head = previousNode
        return True

    # method that sorts LinkedList
    def sort(self):
        start = self.head
        beginNode = start
        while beginNode:
            tempNode = beginNode
            tempNode2 = beginNode
            smallest = beginNode.getData()
            while tempNode:
                if smallest > tempNode.getData():
                    smallest = tempNode.getData()
                    tempNode2 = tempNode
                tempNode = tempNode.getNextNode()

            # swap data of beginNode and tempNode2
            temp = beginNode.getData()
            beginNode.updateData(tempNode2.getData())
            tempNode2.updateData(temp)

            beginNode = beginNode.getNextNode()

    # method returns new instance of the sorted LinkedList without changing original LinkedList
    def sorted(self):
        start = self.head
        tempList = self.copy()
        tempList.sort()
        return tempList



# node class
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    # method to update the data feild of Node
    def updateData(self, data):
        self.data = data

    # method to set Link feild the Node
    def setLink(self, node):
        self.link = node

    # method returns data feild of the Node
    def getData(self):
        return self.data

    # method returns address of the next Node
    def getNextNode(self):
        return self.link


# main method

# creating LinkedList
myList = LinkedList()

# adding some elements to the start of LinkedList
myList.addToStart(5)
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)


myList.display()

# adding some elements to the End of the LinkedList
myList.addToEnd(12)
myList.addToEnd(13)
myList.addToEnd(3)
myList.display()

# printing Length
print(myList.length())

# printing index of an element
print(myList.index(3))

# printing element at a particular index
print(myList.atIndex(5))

# removing an element
print(myList.remove(12))

# removing element from a particular position
myList.removePosition(2)

myList.display()

# printing max and min element
print(myList.Max())
print(myList.Min())

# pushing and poping elements
print(myList.push(31))
myList.display()
print(myList.pop())
myList.display()

# creating a copy of the Linked List
myList2 = myList.copy()
myList2.display()

# removing all elements from the LinkedList
myList2.clear()
myList2.display()


# printing a string of elements of the LinkedList
print(myList.toString(","))

# printing count of particular element in the List
print(myList.count(3))

# making a builtIn List from the LinkedList
newList = myList.toList()
print(newList)

# making a List from the LinkedList
newSet = myList.toSet()
print(newSet)

# reversing the LinkedLkst
myList.reverse()
myList.display()

# making a sorted LinkedList out of the Original
myList3 = myList.sorted()
myList3.display()

# sorting the LinkedList
myList.sort()
myList.display()

class Player:

    def __init__(self, ownFieldList, name, choosedMark):
        self.ownFieldList = ownFieldList
        self.name = name
        self.choosedMark = choosedMark
    
    def getOwnFields(self):
        return self.ownFieldList

    def getMark(self):
        return self.choosedMark

    def getName(self):
        return self.name

    def printList(self):
        for i in self.ownFieldList:
            print(i, end='')
        print("\n")
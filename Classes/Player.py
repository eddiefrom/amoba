class Player:

    def __init__(self, ownFieldList, name, choosedMark):
        self.ownFieldList = ownFieldList
        self.name = name
        self.choosedMark = choosedMark
    
    def getOwnFields(self):

        for column in self.ownFieldList:
            for row in column:
                print(row)

    def getMark(self):
        return self.choosedMark

    def getName(self):
        return self.name
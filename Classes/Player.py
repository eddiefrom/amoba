class Player:

    def __init__(self, ownFieldList):
        self.ownFieldList = ownFieldList
    
    def ownField(self):

        for i in self.ownFieldList:
            print(i)
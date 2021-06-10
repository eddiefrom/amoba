from Classes.Player import Player


class Table:
    
    def __init__(self, size, marks):
        self.size = size 
        self.marks = marks


    def drawTable(self, player1 : Player, player2 : Player):

        field_counter = 1

        for row in range(0, self.size):  
            for line in range (0, self.size ):
                print(" -------", end='')
            print("")


            for side in range(0, 3):       
                for column in range(0, self.size):
                
                    if(column == self.size - 1):
                        if(side == 0):
                            if(len(str(field_counter)) == 1):
                                print("|"+ str(field_counter) + "      |")
                            else:
                                print("|"+ str(field_counter) + "     |")
                            field_counter += 1     
                        if(side == 1):
                            print("|   " + self.marks[row] + "   |")                        
                        if(side == 2):
                            print("|       |")

                    else:
                        if(side == 0):
                            if(len(str(field_counter)) == 1):
                                print("|"+ str(field_counter) + "      ", end='')
                            else:
                                print("|"+ str(field_counter) + "     ", end='')
                            field_counter += 1     
                        if(side == 1):
                            print("|   " + self.marks[row] + "   ", end='')
                        if(side == 2):
                            print("|       ",end='')
              
        for line in range (0, self.size ):
                print(" -------", end='')
        print("")


    def getTableLength(self):
        return self.size * self.size

    def getMarks(self):
        return self.marks
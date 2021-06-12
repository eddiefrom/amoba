
class Table:
    
    def __init__(self, size, marks):
        self.size = size 
        self.marks = marks

    def drawTable(self):
        field_counter = 1
        mark_counter = 0

        for row in range(0, self.size):  
            for line in range (0, self.size ):
                print(" -------", end='')
            print("")

            for side in range(0, 3):      
                for column in range(0, self.size):
         
                    if(column == self.size - 1):
                        if(side == 0):
                            print("|"+ str(field_counter) + (" " * (7 - len(str(field_counter))) + "|"))
                            field_counter += 1     
                        if(side == 1):
                            print("|"+ " " * 3 + self.marks[mark_counter] + " " * 3 + "|")
                            mark_counter += 1
                        if(side == 2):
                            print("|"+ " "  * 7 +"|")
                    else:
                        if(side == 0):
                            print("|"+ str(field_counter) + (" " * (7 - len(str(field_counter)))), end='')
                            field_counter += 1     
                        if(side == 1):            
                            print("|"+ " " * 3 + self.marks[mark_counter] + " " * 3, end='')
                            mark_counter += 1
                        if(side == 2):
                            print("|"+ " "  * 7, end='')
                    
        for line in range (0, self.size ):
                print(" -------", end='')
        print("")


    def getTableLength(self):
        return self.size * self.size
    
    def getTableSize(self):
        return self.size

    def getMarks(self):
        return self.marks
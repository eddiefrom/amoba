class Table:
    
    def __init__(self, size):
        self.size = size 

    def drawTable(self):

        for field_size in range(0, self.size):

            for lines in range(0, self.size ):
                print(" -------", end='')
            print("")

            for column_size in range(0, 3):
                for row_size in range(0, self.size): 
                    if(row_size == self.size - 1):
                        if(column_size == 1):           #játékosok mezői alapján a feltétel 
                            print("|   X   |", end="")
                        else:
                            print("|       |", end="")
                    else:
                        if(column_size == 1):           #játékosok mezői alapján a feltétel 
                            print("|   X   ", end="")
                        else:
                            print("|       ", end="")
                print("")
            
            if(field_size == self.size - 1):
                for i in range(0, self.size ):
                    print(" -------", end='')
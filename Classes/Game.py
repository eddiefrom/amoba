from Classes.Table import Table
from Classes.Player import Player

class Game:

    def __init__(self, table : Table, player1 : Player, player2 : Player, game_diff, item_number_to_win):
        self.table = table
        self.player1 = player1
        self.player2 = player2
        self.game_diff = game_diff
        self.item_number_to_win = item_number_to_win

    def playerChoose(self, name):
        
        while(True):
            try:
                print(name+" köre.")
                field = int(input("Hanyadik mező: "))

                if(field > 0 and field < self.table.getTableLength() + 1):
                    if(self.table.getMarks()[field - 1] == " "):

                        if(name == self.player1.getName()):
                            self.player1.getOwnFields()[field - 1] = 1
                            self.table.getMarks()[field - 1] = self.player1.getMark()
                            break
                        if(name == self.player2.getName()):
                            self.player2.getOwnFields()[field - 1] = 1
                            self.table.getMarks()[field - 1] = self.player2.getMark()
                            break
                    else:
                        print("A mező foglalt!\n")
                else:
                    print("Hibás intervallum!\n")
            except:
                print("Hibás szám adat!\n")

    def checkNumberOfMarks(self, while_con, if_conm, player : Player):
        
        playerList = player.getOwnFields()
        counter = 0

        for i in range(0, len(playerList)) :

            if(playerList[i] == 1):
                counter += 1
                item = i
                while(item + while_con < len(playerList) + 1 ):
                    if(playerList[item + if_conm]  == 1):
                        counter += 1
                        item = item + if_conm
                    else:
                        break
                if(counter == 5):
                    player.setWin(1)
                    break
            counter = 0
        
    def checkDirection(self, direction, player : Player):

        if(direction == "\\"):
            self.checkNumberOfMarks(self.table.getTableSize() + 2, self.table.getTableSize() + 1 , player)
        if(direction == "/"):
            self.checkNumberOfMarks(self.table.getTableSize() + 2, self.table.getTableSize() - 1, player)
        if(direction == "-"):
            self.checkNumberOfMarks(1, 1, player)
        if(direction == "|"):
            self.checkNumberOfMarks(self.table.getTableSize() + 1, self.table.getTableSize(), player)


    def checkStatus(self, player : Player):

            self.checkDirection("\\", player)
            self.checkDirection("/", player)
            #self.checkDirection("-", player)
            self.checkDirection("ˇ|", player)
                 
    def getTable(self):
        return self.table.drawTable()

    #implementálás
    def machineChoose(self):
        print("AI :D")

    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2

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
                field = int(input("Hanyadik mező: "))
                if(field > 0 and field < self.table.getFieldLength() + 1):
                    if(self.player1.getName == name):
                        self.player1.getOwnFields()[field - 1] = 1
                        self.table.getMarks()[field - 1] = self.player1.getMark()
                        break
                    else:
                        self.player2.getOwnFields()[field - 1] = 1
                        self.table.getMarks[field - 1] = self.player2.getMark()
                        break
                else:
                    print("Hibás adat!")
            except:
                print("Hibás adat!")
              
    def getTable(self, player1 : Player, player2 : Player):
        return self.table.drawTable(player1, player2)

    def machineChoose(self):
        print("AI :D")

    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2

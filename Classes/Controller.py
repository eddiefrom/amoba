from Classes.Table import Table
from Classes.Player import Player
from Classes.Menu import Menu
from Classes.Game import Game

class Controller:

    def __init__(self) -> None :
        pass

    def startMenu(self):
        self.myMenu = Menu()
        self.myMenu.drawMenu()


    def startGame(self):
        self.field_size = self.myMenu.getFieldSize()
        self.game_difficult = self.myMenu.getGameDifficult()
        self.item_number_to_win = self.myMenu.getItemNumberToWin()
        self.player1Name = self.myMenu.getName1()
        self.player2Name = self.myMenu.getName2()
        self.mark1 = self.myMenu.getMark1()
        self.mark2 = self.myMenu.getMark2()
        

        player1List = [self.field_size ][ self.field_size]
        player2List = [self.field_size ][ self.field_size]
        self.player1 = Player(player1List, "p1")
        self.player2 = Player(player2List, "p2")

        self.table = Table(self.field_size)
        self.game = Game(self.table, self.player1, self.player2, self.game_difficult, self.item_number_to_win)


#----------------------------------TESZT--------------------------------
        
        #ciklusban jelölgetnek nyerésig

        self.myMenu.drawHeader()
        self.table.drawTable(self.player1, self.player2)
        self.game.playerChose(self.player1)
        self.game.playerChose(self.player2)

       





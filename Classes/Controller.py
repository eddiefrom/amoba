from Classes.Table import Table
from Classes.Player import Player
from Classes.Menu import Menu

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

        player1List = []
        player2List = []
        self.player1 = Player(player1List)
        self.player2 = Player(player2List)

        self.table = Table(self.field_size)
#----------------------------------TESZT--------------------------------
        self.myMenu.drawHeader()
        self.table.drawTable()



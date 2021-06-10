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
        list_size =  self.field_size * self.field_size

        player1List = [0] * list_size
        player2List = [0] * list_size
        self.player1 = Player(player1List, self.player1Name, self.mark1)
        self.player2 = Player(player2List, self.player2Name, self.mark2)

        marksList = [' '] * list_size
        self.table = Table(self.field_size, marksList)
        self.game = Game(self.table, self.player1, self.player2, self.game_difficult, self.item_number_to_win)


#----------------------------------TESZT--------------------------------
        
        #ciklusban jelölgetnek nyerésig
        self.game.getTable(self.game.getPlayer1, self.game.getPlayer2)
        #for i in range(0, 4): 
            
         #   self.game.playerChoose(self.game.getPlayer1().getName)
           # self.game.machineChoose()

            #self.game.getPlayer1().printList()
            # self.game.playerChoose(self.player2)

       





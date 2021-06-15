from Classes.Table import Table
from Classes.Player import Player
from Classes.Menu import Menu
from Classes.Game import Game
import os, sys, platform

class Controller:

    def __init__(self) :
        pass

    def startMenu(self):
        self.myMenu = Menu()
        self.myMenu.drawMenu()


    def gameInit(self):
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
        self.player1 = Player(player1List, self.player1Name, self.mark1, 0)
        self.player2 = Player(player2List, self.player2Name, self.mark2, 0)

        marksList = [' '] * list_size
        self.table = Table(self.field_size, marksList)
        self.game = Game(self.table, self.player1, self.player2, self.game_difficult, self.item_number_to_win)


    def startGame(self):

        self.gameInit()

        winner_name =  ""
        self.myMenu.drawHeader()
        self.game.getTable()
        
        while(winner_name == ""):
            self.game.playerChoose(self.game.getPlayer1().getName())
            self.myMenu.drawHeader()
            self.game.getTable()
            self.game.checkStatus(self.game.getPlayer1())

            if(self.game.getPlayer1().isWin()):
                winner_name = self.game.getPlayer1().getName()
                break

            if(self.myMenu.getLiveOrMachine() == 1):
                self.game.machineChoose(self.myMenu.getGameDifficult())
            else:
                self.game.playerChoose(self.game.getPlayer2().getName())    

            self.myMenu.drawHeader()
            self.game.getTable()
            self.game.checkStatus(self.game.getPlayer2())

            if(self.game.getPlayer2().isWin()):
               winner_name = self.game.getPlayer2().getName()
               break

        print("A nyertes: ", winner_name)
        answer = self.myMenu.answerCheck(0, 3, "Akar ujat jatszani? Igen(1), Nem(2) : ")
       
        if(answer == 1):
            self.startGame()
        else:
            if(platform.system() == "Windows"):
                os.system('cls')
            else:
                os.system('clear')
            sys.exit()




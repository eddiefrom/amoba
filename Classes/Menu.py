from Classes.Player import Player
import os, sys
       
class Menu:

    def __init__(self) -> None:
        pass
        
    def drawHeader(self):
        os.system('cls')
        print("------------------------AMŐBA JÁTÉK--------------------------\n"
            "                    készítette: Jakab Csaba\n\n\n") 

    def answerCheck(self, num1, num2, out_string):
        if(num1 > num2): 
            num1, num2 = num2, num1

        while(True):
            try:
                value = int(input(out_string))
                if(value > num1 and value < num2):
                    return value
                else:
                    print("Hibás adat!")  
            except:
                print("Hibás adat!")

    def newGameMenu(self):


        # név bekérés
        self.drawHeader()
        self.name1 = input("Adja meg a nevét: ")
        # jel bekérés
        self.drawHeader()
        self.mark1 = input("X(1) vagy 0(2) ? : ")
        #self.mark1 = self.answerCheck(0, 3, "X(1) vagy 0(2) ? : ")
        # gépi vagy élő ellenfél, ha élő neki is név, jel bekérés
        self.drawHeader()
        self.liveOrMachine = input("Gépi(1) vagy élő(2) ellenfél?  : ")
        #self.liveOrMachine = self.answerCheck(0, 3, "Gépi(1) vagy élő(2) ellenfél?  : ")
        if(self.liveOrMachine == 2):
            self.drawHeader()
            self.name2 = input("Adja meg az ellenfél nevét: ")
            if(self.mark1 =='X'):
                self.mark2 = '0'
            else:
                self.mark2 = 'X'

        #HIBAKEZELÉS


        self.drawHeader()
        self.field_size = self.answerCheck(11, 2, "Mező mérete (3 - 10): ")
            
        self.drawHeader()
        self.game_difficult = self.answerCheck(0,3,"Nehézség (1,2): ")
                  
        self.drawHeader()
        self.item_number_to_win = self.answerCheck(2, 11, "Győzelemhez szükséges elemszám (3 - 10): ")

        

    def getName1(self):
        return self.name1

    def getName2(self):
        return self.name2
    
    def getMark1(self):
        return self.mark1
    
    def getMark2(self):
        return self.mark2
    
    def getLiveOrMachine(self):
        return self.liveOrMachine

    def getFieldSize(self):
        return self.field_size

    def getGameDifficult(self):
        return self.game_difficult

    def getItemNumberToWin(self):
        return self.item_number_to_win    

    def infoMenu(self):

        self.drawHeader( )
        print("Az amőba egy kétszemélyes játék, amiben úgy lehet nyerni, ha az ellenfelet megelőzve \n"
                " elhelyezünk 5 darab általunk választott jelet egymás mellé vizszintesen, horizontálisan vagy átlósan.\n")
        answer = input("Nyomjon meg egy gombot a visszalépéshez..")
    
        self.drawMenu()

    def drawMenu(self):

        self.drawHeader()      

        print("1. Új játék")
        print("2. Ismertető")
        print("3. Kilépés\n")
 
        while(True):
            try:
                answer = int(input("Válasszon a menüpontok közzül: "))
                if(answer > 0 and answer < 4):
                    break  
                else:
                    print("Hibás adat!")                   
            except :
                print("Hibás adat!")                
                    
        if(int(answer) == 1):
            self.newGameMenu()
        elif(int(answer) == 2):
            self.infoMenu()
        elif(int(answer) == 3):
            os.system('cls')
            sys.exit()


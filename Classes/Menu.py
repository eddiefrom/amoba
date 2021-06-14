import os, sys
       
class Menu:

    def __init__(self) -> None:
        pass
        
    def drawHeader(self):
        os.system('cls')
        print("------------------------AMŐBA JÁTÉK--------------------------\n"
            "                    készítette: Jakab Csaba\n\n\n") 

    def answerCheck(self, num1, num2, text):

        while(True):
            try:
                value = int(input(text))
                if(value > num1 and value < num2):
                    return value
                else:
                    print("Hibás intervallum!")  
            except:
                print("Hibás szém érték!")

    def newGameMenu(self):

        self.drawHeader()
        self.field_size = self.answerCheck(4, 12, "Mező mérete (5 - 11): ")
                  
        self.drawHeader()
        self.item_number_to_win = 5

        self.drawHeader()
        self.name1 = input("Adja meg a nevét: ")

        self.drawHeader()
        self.mark1 = self.answerCheck(0, 3, "X(1) vagy 0(2) ? : ")

        self.drawHeader()
        self.liveOrMachine = self.answerCheck(0, 3, "Gépi(1) vagy élő(2) ellenfél?  : ")

        if(self.liveOrMachine == 2):
            self.drawHeader()
            self.name2 = input("Adja meg az ellenfél nevét: ")
            self.game_difficult = ""
        else:
            self.name2 = "Gép"
            self.drawHeader()
            self.game_difficult = self.answerCheck(0,3, "Nehézség (1, 2): ")

        if(self.mark1 == 1):
            self.mark1 = 'X'
            self.mark2 = '0'
        else: 
            self.mark1 = '0' 
            self.mark2 = 'X'
            
    
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

        answer = self.answerCheck(0, 4, "Válasszon a menüpontok közzül: ")      
                    
        if(answer == 1):
            self.newGameMenu()
        elif(answer == 2):
            self.infoMenu()
        elif(answer == 3):
            os.system('cls')
            sys.exit()

    
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


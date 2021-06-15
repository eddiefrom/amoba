import os, sys, platform
       
class Menu:

    def __init__(self) :
        pass
        
    def drawHeader(self):
        if(platform.system() == "Windows"):
            os.system('cls')
        else:
            os.system('clear')
        print("------------------------AMOBA JATEK--------------------------\n"
            "                    keszitette: Jakab Csaba\n\n\n") 

    def answerCheck(self, num1, num2, text):

        while(True):
            try:
                value = int(input(text))
                if(value > num1 and value < num2):
                    return value
                else:
                    print("Hibas intervallum!")  
            except:
                print("Hibas szam ertek!")

    def newGameMenu(self):

        self.drawHeader()
        self.field_size = self.answerCheck(4, 12, "Mezo merete (5 - 11): ")
                  
        self.drawHeader()
        self.item_number_to_win = 5

        self.drawHeader()
        self.name1 = input("Adja meg a nevet: ")

        self.drawHeader()
        self.mark1 = self.answerCheck(0, 3, "X(1) vagy 0(2) ? : ")

        self.drawHeader()
        self.liveOrMachine = self.answerCheck(0, 3, "Gepi(1) vagy elo(2) ellenfel?  : ")

        if(self.liveOrMachine == 2):
            self.drawHeader()
            self.name2 = input("Adja meg az ellenfel nevet: ")
            self.game_difficult = ""
        else:
            self.name2 = "Gep"
            self.drawHeader()
            self.game_difficult = self.answerCheck(0,3, "Nehezseg (1, 2): ")

        if(self.mark1 == 1):
            self.mark1 = 'X'
            self.mark2 = '0'
        else: 
            self.mark1 = '0' 
            self.mark2 = 'X'
            
    
    def infoMenu(self):

        self.drawHeader( )
        print("Az amoba egy ketszemelyes jatek, amiben ugy lehet nyerni, ha az ellenfelet megelozve \n"
                " elhelyezunk 5 darab altalunk valasztott jelet egymas melle vizszintesen, horizontalisan vagy atlosan.\n")
        answer = input("Nyomjon meg egy gombot a visszalepeshez..")
    
        self.drawMenu()

    def drawMenu(self):

        self.drawHeader()      

        print("1. Uj jatek")
        print("2. Ismerteto")
        print("3. Kilepes\n")

        answer = self.answerCheck(0, 4, "Valasszon a menupontok kozzul: ")      
                    
        if(answer == 1):
            self.newGameMenu()
        elif(answer == 2):
            self.infoMenu()
        elif(answer == 3):
            if(platform.system() == "Windows"):
                os.system('cls')
            else:
                os.system('clear')
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


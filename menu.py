import os
       

def drawHeader():
    os.system('cls')
    print("------------------------AMŐBA JÁTÉK-------------------------- "
        "\n                  készítette: Jakab Csaba\n\n\n") 

def newGameMenu():

    drawHeader()
    field_size = int(input("Mező mérete (3 - 10): "))
    while(True):
        if(field_size > 2 and field_size < 11):
            break
        else:
            field_size = int(input("Hibás adat, adja meg újra: "))
        
    drawHeader()
    game_difficult = int(input("Nehézség (1,2): "))
    while(True):
        if(game_difficult > 0 and game_difficult < 3):
            break
        else:
            game_difficult = int(input("Hibás adat, adja meg újra: "))
            
    drawHeader()
    item_number_to_win = int(input("Győzelemhez szükséges elemszám (3 - 10): "))
    while(True):
        if(item_number_to_win > 2 and item_number_to_win < 11):
            break
        else:
            item_number_to_win = int(input("Hibás adat, adja meg újra: "))


def drawMenu():
    drawHeader()      

    print("1. Új játék")
    print("2. Ismertető")
    print("3. Kilépés\n")
    answer = int(input("Válasszon a menüpontok közzül: "))

    while(True):
        if(answer > 0 and answer < 4):
            break
        else:
            answer = int(input("Hibás adat, adja meg újra: "))

    return answer
    


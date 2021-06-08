from menu import drawMenu, newGameMenu
import sys
import os

def main():
    answer = drawMenu()

    if(int(answer) == 1):
        newGameMenu()
    elif(int(answer) == 2):
        print("Második")
    elif(int(answer) == 3):
        os.system('cls')
        sys.exit()

if __name__ == "__main__":
	main()



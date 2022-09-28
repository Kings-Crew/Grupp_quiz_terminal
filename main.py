from questions import *
from time import sleep
poängtavla_ = 0
namn_ = str()

class Spelare():#Här lagras data om spelare
    def __init__(self,namn:str):
        assert type(namn) == str ,"Är inte en string(str) funktion"
        self.namn = namn

    def __repr__(self):
        return f"Namn på spelare: {self.namn}"



class Main:    
    @staticmethod
    def funktion_för_frågor():#This function takes the list of questions and writes it out
        global poängtavla_
        
        for i in range(10):
            spelar_fråga = input(f"{lista_på_frågor[i]}>>>")#Prints out question and waits for user input, then proceeds to print the next question     

            str_spelar_fråga = str(spelar_fråga.upper())#Takes the user input and converts it to uppercase letter

            #Compares the user input A-D with rightanswer A-D
            if str_spelar_fråga != lista_på_frågor[i].rightanswer:      
                print( "Fel svar")
            elif str_spelar_fråga == lista_på_frågor[i].rightanswer:
                poängtavla_ += 1
                print("Rätt svar")
            
    
    
    def main():                                  #This function is for playing the game
        def felhantering_för_input():            #Error-handling in case the player writes out of the ordinary
           #The sleep(1) waits 1 sec before printing the next line
            print("Hej och välkommen till King Crew's AB quiz spel")
            sleep(1)
            print("Du ska svara på 10 frågor...")
            sleep(1)
            print("Men först, vad heter du?")
            global namn_
            while True:#If user enter an int or float the user is stuck at entering their name
                prompt = input(">>>")

                try:
                    #Converts promt to intiger, if try succeds that means that the users input was int
                    värde = int(prompt)
                    print("Du har ett heltal i din input")
                except ValueError:
                    try:
                    #Converts the promt to float, same as above(int) but instead the user have put in float
                        val = float(prompt)
                        print("Input är ett flyttal")
                    except ValueError:#If it fails to do so it means that the user used letters and then it assigns the name variable
                        namn_ = Spelare(prompt)
                        break
        while True:
            felhantering_för_input()#User input name and error-handeling
            Main.funktion_för_frågor()#printing questions and awaits User input
            
            print(f"{namn_}\n Antal poäng:{poängtavla_} av 10 möjliga")
            print("Tryck 1 för JA \nTryck 2 för NEJ")
            prompt = input("Vill du spela igen? \n>>>")
            if prompt == "1":#Continues to run this while-loop
                continue
            elif prompt == "2":#Breakes out of while-loop
                break
            

if __name__ == "__main__":
    Main.main()
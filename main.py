from questions import *
from time import sleep
poängtavla_ = 0
namn_ = str()
#Alla frågor sparas som instansvariabler från klassen: Frågor()

class Spelare():                    #Här lagras data om spelare & deras poäng
    def __init__(self,namn:str):
        assert type(namn) == str ,"Är inte en string(str) funktion"
        self.namn = namn

    def __repr__(self):
        return f"Namn på spelare: {self.namn}"



class Main:    
    @staticmethod
    def funktion_för_frågor():      #Tar emot och skriver ut frågor
        global poängtavla_
        
        for i in range(10):
            spelar_fråga = input(f"{lista_på_frågor[i]}>>>")      

            str_spelar_fråga = str(spelar_fråga.upper())            #Konverterar till stor bokstav

            if str_spelar_fråga != lista_på_frågor[i].rightanswer:      #Jämför svar
                print( "Fel svar")
            elif str_spelar_fråga == lista_på_frågor[i].rightanswer:
                poängtavla_ += 1
                print("Rätt svar")
            
    
    
    def main():                                  #Detta är funktionen för att spela spelet  
        def felhantering_för_input():            #Felhantering utifall spelaren skriver något konstigt
            print("Hej och välkommen till King Crew's AB quiz spel")
            sleep(1)
            print("Du ska svara på 10 frågor...")
            sleep(1)
            print("Men först, vad heter du?")
            global namn_
            while True:
                prompt = input(">>>")

                try:
                    #Konverterar prompt till ett heltal
                    värde = int(prompt)
                    print("Du har ett heltal i din input")
                except ValueError:
                    try:
                    #Konverterear prompt till flyttal
                        val = float(prompt)
                        print("Input är ett flyttal")
                    except ValueError:
                        namn_ = Spelare(prompt)
                        break
        while True:
            felhantering_för_input()
            Main.funktion_för_frågor()
            
            print(f"{namn_}\n Antal poäng:{poängtavla_}")
            print("Tryck 1 för JA \nTryck 2 för NEJ")
            prompt = input("Vill du spela igen? \n>>>")
            if prompt == "1":
                continue
            elif prompt == "2":
                break
            

if __name__ == "__main__":
    Main.main()
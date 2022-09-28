from questions import *
#Alla frågor sparas som instansvariabler från klassen: Frågor()


class main:

    
    @staticmethod
    def funktion_för_frågor():      #Tar emot och skriver ut frågor
        score = 0
        for i in range(10):
            spelar_fråga = input(f"{lista_på_frågor[i]}>>>")      

            str_spelar_fråga = str(spelar_fråga.upper())            #Konverterar till stor bokstav

            if str_spelar_fråga != lista_på_frågor[i].rightanswer:      #Jämför svar
                print( "Fel svar")
            elif str_spelar_fråga == lista_på_frågor[i].rightanswer:
                
                print("Rätt svar")
            print(f"Du hade såhär många rätt {score}")
                
            

class spelare():                    #Här lagras data om spelare & deras poäng
    def __init__(self,namn:str,poängtavla:int):
        assert type(namn) == str ,"Är inte en string(str) funktion"
        self.namn = namn
        self.poängtavla = poängtavla

    def __repr__(self):
        return f"Namn på spelare: {self.namn}\nTotalt poäng för {self.namn}: {self.poängtavla} poäng"




#Test av objekt


if __name__ == "__main__":
    print(main.funktion_för_frågor())
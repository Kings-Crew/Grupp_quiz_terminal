from questions import questions

def main():
    
    def funktion_för_frågor():      #Tar emot och skriver ut frågor
        pass
       
    def lagra_frågor():             #Lagrar frågor från questions.py
        frågor = questions
        pass

class spelare():                    #Här lagras data om spelare & deras poäng
    def __init__(self,namn:str,poängtavla:int):
        assert type(namn) == str ,"Är inte en string(str) funktion"
        self.namn = namn
        self.poängtavla = poängtavla


    def __repr__(self):
        return f"Namn på spelare: {self.namn}, totalt poäng för {self.namn}: {self.poängtavla} poäng"


    #Test av objekt

Kalle = spelare("Kalle", 5)
print(Kalle)

    




if __name__ == "__main__":
    main()
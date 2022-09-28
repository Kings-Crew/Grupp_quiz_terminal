#Alla frågor lagras i en separat fil. Det lagras som en dict() för enkelt åtkomst, 
#Och för att det på ett enkelt sätt skall kunna skickas som t.ex. en JSON

#Möjligtvis om man skall använda sig av defaultdict biblioteket för multidimensionella dicts()
#Kanske blir för komplex: https://www.geeksforgeeks.org/defaultdict-in-python/ //Marcus 2022-09-27

class Frågor:
    def __init__(self,question,answer1,answer2,answer3,answer4,rightanswer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.rightanswer = rightanswer


    def __repr__(self):
        
        return(f"""
        
        Skriv A,B,C,D för att svara på rätt fråga\n
        Question: {self.question}
    
        Answer-A: {self.answer1} \t Answer-B: {self.answer2}
    
        Answer-C: {self.answer3} \t Answer-D: {self.answer4}

        
    
        """ 
        )

fråga_1 = Frågor("Vem skapade Python?:", "Stefan Löfven", "Mike Tyson", "Bjarne Stroustrup", "Guido van Rossum", "D")
fråga_2 = Frågor("Vad är Python?:", "tolkat språk", "en giftig orm", "ett spel", "en båt", "d")
fråga_3 = Frågor("dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd")
fråga_4 = Frågor("dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd")
fråga_5 = Frågor("dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd")
fråga_6 = Frågor("dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd")
fråga_7 = Frågor("dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd")
fråga_8 = Frågor("dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd")
fråga_9 = Frågor("dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd")
fråga_10 = Frågor("dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd", "dsfsdfsd")


lista_på_frågor = [fråga_1,fråga_2,fråga_3,
                   
                   fråga_4,fråga_5,fråga_6,
                   
                   fråga_7,fråga_8,fråga_9,
                   
                   fråga_10]





#if spelare_input !=
print(fråga_1.rightanswer)






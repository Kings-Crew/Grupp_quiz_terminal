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

        
    
        """ )

fråga_1 = Frågor("Vem skapade Python?:", "Stefan Löfven", "Mike Tyson", "Bjarne Stroustrup", "Guido van Rossum", "D")
fråga_2 = Frågor("Vad är Python?:", "Tolkat språk", "En giftig orm", "Ett spel", "En båt", "A")
fråga_3 = Frågor("När uppfann man Python?", "1992", "1995", "1991", "1988", "C")
fråga_4 = Frågor("Vilket företag har Python som sitt officiella språk?", "Ericsson", "Pressbyrån", "Google", "Snapchat", "C")
fråga_5 = Frågor("Vad kan språket andvändas för?", "Skicka paket", "Webbutveckling", "Felsökning", "Anti virusskydd", "B")
fråga_6 = Frågor("Python-bytekoden sparas i vilken filform?", ".txt", ".pdf", ".jpeg", ".py", "D")
fråga_7 = Frågor("Varför är Python så populärt?", "Open source", "Reklamfritt", "Sparar ändringar per automatik", "Molnbaserad", "A")
fråga_8 = Frågor("Hur många års erfaraenhet av programmering behöver man för att lära sig Python", "2 år", "10 år", "5 år", "Ingen erfarenhet alls", "D")
fråga_9 = Frågor("Vad behövs för att lära sig en python?", "En skruvmejsel", "En exklusiv injudan", "En dator", "Tillgång till cryptovalutor", "C")
fråga_10 = Frågor("Hur många python utvecklare finns det?", "Över 7 miljoner", "Över 10 miljoner", "Över 25 miljoner", "Över 100 miljoner", "A")


lista_på_frågor = [fråga_1,fråga_2,fråga_3,
                   
                   fråga_4,fråga_5,fråga_6,
                   
                   fråga_7,fråga_8,fråga_9,
                   
                   fråga_10]












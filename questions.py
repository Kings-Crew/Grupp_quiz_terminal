#Alla frågor lagras i en separat fil. Det lagras som en dict() för enkelt åtkomst, 
#Och för att det på ett enkelt sätt skall kunna skickas som t.ex. en JSON

#Möjligtvis om man skall använda sig av defaultdict biblioteket för multidimensionella dicts()
#Kanske blir för komplex: https://www.geeksforgeeks.org/defaultdict-in-python/ //Marcus 2022-09-27

class frågor:
    def __init__(self,question,answer1,answer2,answer3,answer4,rightanswer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.rightanswer = rightanswer

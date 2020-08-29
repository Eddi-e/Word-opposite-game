import time
import random
WordList1 = ["hot","summer","hard","dry","simple","light","weak","male","sad","win","small","ignore","buy","succeed","reject","prevent","exclude"]
WordList2 = ["cold","winter","soft","wet","complex","darkness","strong","female","happy","lose","big","pay attention","sell", "fail","accept", "allow", "include"]
q1 = []
q2 = []
for x in range(0,10):
    q1.clear()
    q2.clear()
    equalCheck = True
    while equalCheck == True:
        number1 = random.randint(0,len(WordList1))
        number2 = random.randint(0,len(WordList1))
        if number1 != number2:
            equalCheck = False
    q1.append(WordList1[number1])
    q1.append(WordList2[number1])
    q2.append(WordList1[number2])
    q2.append(WordList2[number2])
    print (q1,q2)
    
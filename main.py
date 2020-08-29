import time
import random
Score = 0
WordList1 = ["hot","summer","hard","dry","simple","light","weak","male","sad","win","small","ignore","buy","succeed","reject","prevent","exclude","positive","thick","quiet","wrong","up"]
WordList2 = ["cold","winter","soft","wet","complex","darkness","strong","female","happy","lose","big","pay attention","sell", "fail","accept", "allow", "include","negative","thin","loud","right","down"]
q1 = []
q2 = []
for x in range(0,10):
    list1len = len(WordList1)
    list2len = len(WordList2)
    q1.clear()
    q2.clear()
    equalCheck = True
    while equalCheck == True:
        number1 = random.randint(0,list1len-1)
        number2 = random.randint(0,list2len-1)
        print(number1,number2)
        if number1 != number2:
            equalCheck = False
    q1.append(WordList1[number1])
    q1.append(WordList2[number1])
    q2.append(WordList1[number2])
    q2.append(WordList2[number2])
    print ("Q",x,q1[0],"is to",q1[1],"as",q2[0],"is to ... \n Answer")
    Answer = input()
    if Answer == q2[1]:
        Score += 1
        print("Correct, your score is now: \n",Score)
    else:
        print("Incorrect, the correct answer is: \n",q2[1])
    WordList1.remove(q1[0])
    WordList1.remove(q2[0])
    WordList2.remove(q1[1])
    WordList2.remove(q2[1])
print ("Well done, your score is: \n",Score)

    
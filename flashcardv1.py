import random

class flashcard:
    def __init__(self,word,info):
        self.word = {'Classification':'Supervised Learning',
        'Clustering':'Unsupervised Learning'}

    def quiz(self):
        while(True):
            word,info = random.choice(list(self.word.items()))
            print("What does {} mean?".format(word))
            answer = input()

            if(answer.lower()==info):
                print("Correct answer")
            else:
                print("Wrong answer")

            play = int(input("Enter 1 if you want to stop, enter 0 if you want to continue"))

            if (play):
                break

print("Let's start")
f = flashcard()
f.quiz()

from random import random,sample, shuffle

trivia = ["Who won the 2012 NBA Finals MVP?",
           "What player has the highest career PPG?",
           "What team won the first NBA championship?",
           "Who has the most career rebounds?",
           "Who was the #1 pick in the 1996 draft?",
           "Most coaching titles?",
           "What player won the most regular season MVP's ?",
           "What player has the highest career FT percentage?",
           "Who has the most coaching wins?",
           "What team drafted Ray Allen? ",
           "What year was the first time an NBA finals went to 7 games? ",
           "Who is the first player to be drafted #1 without playing college\n or high school basketball in the U.S.? ",
           "What team drafted Kobe Bryant?",
           "Who is the lowest seeded team to win the NBA title?",
           "Who is the lowest seeded team to make it to the NBA Finals?" ]

triviaAnswer = ["Lebron James", "Michael Jordan", "Philadelphia Warriors", "Wilt Chamberlain",
                "Allen Iverson", "Phil Jackson", "Kareem Abdul-Jabbar", "Steve Nash",
                "Don Nelson", "Timberwolves", "1950", "Yao", "Charlotte Hornets",
                "Rockets", "Knicks"]

print()
print("Welcome to NBA trivia")
print("Hit the spacebar or '0' to quit the game at any time")
print()

def question(num):
    print("Question:", num)
    
def answer(ans):
    answer = input("What is your answer?: ").lower()
    if answer == triviaAnswer:
        print("Correct!")
        return score + 1
    if answer == '000':
        print("Leaving quiz")
        exit()
            
question(1)
for q in trivia:
    if q == trivia[0]:
        print(trivia[0])
answer(1)
score = 0
print()

question(2)
for q in trivia:
    if q == trivia[1]:
        print(trivia[1])        
answer(1)
print()                 

question(3)
for q in trivia:
    if q == trivia[2]:
        print(trivia[2])
answer(1)
print()                 

question(4)
for q in trivia:
    if q == trivia[3]:
        print(trivia[3])
answer(1)
print()                 

question(5)
for q in trivia:
    if q == trivia[4]:
        print(trivia[4])
answer(1)
print()                 

question(6)
for q in trivia:
    if q == trivia[5]:
        print(trivia[5])
answer(1)
print()                 

question(7)
for q in trivia:
    if q == trivia[6]:
        print(trivia[6])
answer(1)
print()                 

question(8)
for q in trivia:
    if q == trivia[7]:
        print(trivia[7])
answer(1)
print()                 

question(9)
for q in trivia:
    if q == trivia[8]:
        print(trivia[8])
answer(1)
print()                 

question(10)
for q in trivia:
    if q == trivia[9]:
        print(trivia[9])
answer(1)
print()                 

question(11)
for q in trivia:
    if q == trivia[10]:
        print(trivia[10])
answer(1)
print()                 

question(12)
for q in trivia:
    if q == trivia[11]:
        print(trivia[11])
answer(1)
print()                 

question(13)
for q in trivia:
    if q == trivia[12]:
        print(trivia[12])
answer(1)
print()

question(14)
for q in trivia:
    if q == trivia[13]:
        print(trivia[13])
answer(1)
print()                 

question(15)
for q in trivia:
    if q == trivia[14]:
        print(trivia[14])
answer(1)
print()
            
#numRight = score // len(trivia)
#print("Your total score = ",score, "out of", len(trivia))



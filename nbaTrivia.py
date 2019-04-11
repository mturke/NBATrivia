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
            
numRight = score // len(trivia)
print("Your total score = ",score, "out of", len(trivia))






'''          
qA = {"Who one the 2012 NBA Finals MVP: ": "Lebron James",
           "What player has the highest career PPG?: ": "Michael Jordan",
           "What team won the first NBA championship?: ": "Philadelphia Warriors",
           "Who has the most career rebounds?: ": , "Wilt Chamberlain"
           "Who was the #1 pick in the 1996 draft: ": "Allen Iverson",
           "Most coaching titles?: ": "Phil Jackson",
           "What player won the most regular season MVP's: ?": "Kareem Abdul-Jabbar",
           "What player has the highest career FT percentage?: ": "Steve Nash",
           "Who has the most coaching wins: ": "Don Nelson",
           "What team drafted Ray Allen?: ": "Minnesota Timberwovles",
           "What year was the first time an NBA finals went to 7 games?:":"!9150-1951",
           "Who is the first player to be drafted #1 without playing college or high school basketball in the U.S.?: ": "Yao Ming",
           "What team drafted Kobe Bryant: ?": "Charlotte Hornets",
           "Who is the lowest seeded team to win the NBA title?: ": "Houston Rockets",
           "Who is the lowest seeded team to make it to the NBA Finals?: ": "Knicks" }


for q in qA:
    input

def question(num):
    print("Question: ")

print("Welcome to NBA trivia!")
score = 0
numQ = 15
question(1)

x = input("Who one the 2012 NBA Finals MVP: ")

if x == 'Lebron' or x == 'Lebron' or x == 'lebron' or x == 'lebron james' or x == 'Lebron James':
    print("Correct!")
    score += 1
elif x != 'Lebron' or x != 'Lebron' or x != 'lebron' or x != 'lebron james' or x != 'Lebron James':
    print("Incorrect! You get one more guess!")
    x = input("Guess again: ")
    if x == 'Lebron' or x == 'Lebron' or x == 'lebron' or x == 'lebron james' or x == 'Lebron James':
        print("Correct!")
        score += 1
    else:
        print("Sorry- The correct answer was: Lebron")
        score -= 1


print()
question(2)
print()

x = input("What player has the highest career PPG?: ")
if x == "Michael Jordan" or x == "michael jordan":
    print("Correct! MJ had a career average of 30.12ppg")
    score += 1
elif x != "Michael Jordan" or x != "michael jordan":
    print("Incorrect! You get one more guess")
    x = input("Guess again: ")
    
    if x == "Michael Jordan" or x == "michael jordan":
        print("Correct! MJ had a career average of 30.12ppg")
        score += 1
    else:
        print("Sorry- The correct answer was: Michael Jordan")
        score -= 1

print()
question(3)
print()

x = input("What team won the first NBA championship?: ")
if x == 'Philadelphia Warriors' or x == "philadelphia warriors" or x == 'warriors' or x == "Warriors":
    print("Correct! The Philadelphia Warriors won the first NBA Championship in the 1946-47 season")
    score += 1
elif x != 'Philadelphia Warriors' or x == "philadelphia warriors" or x == 'warriors' or x == "Warriors":
    print("Incorrect! You get one more guess")
    x = input("Guess again: ")
    if x == 'Philadelphia Warriors' or x == "philadelphia warriors" or x == 'warriors' or x == "Warriors":
        print("Correct! The Philadelphia Warriors won the first NBA Championship in the 1946-47 season")
        score += 1
    else:
        print("Sorry- The correct answer was the Philadelphia Warriors")
        score -= 1

print()
question(4)
print()
x = input("Who has the most career rebounds?: ")
if x == "wilt chamberlain" or x == "Wilt Chamberlain" or x == "wilt" or x == "Wilt":
    print("Correct! Wilt Chamberlain had 23,924 career rebounds")
    score += 1
elif x != "wilt chamberlain" or x != "Wilt Chamberlain" or x != "wilt" or x != "Wilt":
    print("Incorrect! You get one more guess")
    x = input("Guess again: ")
    if x == "wilt chamberlain" or x == "Wilt Chamberlain" or x == "wilt" or x == "Wilt":
        print("Correct! Wilt Chamberlain had 23,924 career rebounds")
        score += 1
    else:
        print("Sorry- The correct answer was Wilt Chamberlain")
        score -= 1

print()

question(5)
print()
x = input("Who was the #1 pick in the 1996 draft: ")
if x == "Allen Iverson" or x == "allen iverson":
    print("Correct! Allen Iverson was the #1 pick in the '96 draft")
    score += 1
elif x != "Allen Iverson" or x != "allen iverson":
    print("Incorrect! You get one more guess")
    x = input("Guess again: ")
    if x == "Allen Iverson" or x == "allen iverson":
        print("Correct! Allen Iverson was the #1 pick in the '96 draft")
        score += 1
    else:
        print("Sorry- The correct answer was Allen Iverson")
        score -= 1

print()
question(6)
print()
x = input("Who has the most coaching titles: ")
if x == "Phil Jackson" or x == "phil jackson":
    print("Correct! Phil Jackson has 11 coaching titles")
    score += 1
elif x != "Phil Jackson" or x != "phil jackson":
    print("Incorrect! You get one more guess")
    x = input("Guess again: ")
    if x == "Phil Jackson" or x == "phil jackson":
        print("Correct! Phil Jackson has 11 coaching titles")
        score += 1
    else:
        print("Sorry- The correct answer was Phil Jackson")
        score -= 1


print()
question(7)
print()
x = input("What player won the most regular season MVP's: ? ")
if x == "Kareem Abdul Jabbar" or x == "kareem abdul jabbar" or x == "kareem abdul-jabbar" or x == "Kareem Abdul-Jabbar":
    print("Correct! Kareem Abdul-Jabbar had 6 tegular season MVP's")
    score += 1
elif x != "Kareem Abdul Jabbar" or x != "kareem abdul jabbar" or x != "kareem abdul-jabbar" or x != "Kareem Abdul-Jabbar":
    print("Incorrect! You get one more guess")
    x = input("Guess again: ")
    if x == "Kareem Abdul Jabbar" or x == "kareem abdul jabbar" or x == "kareem abdul-jabbar" or x == "Kareem Abdul-Jabbar":
        print("Correct! Kareem Abdul-Jabbar had 6 regular season MVP's")
        score += 1
    else:
        print("Sorry- The correct answer was Kareem Abdul-Jabbar")
        score -= 1


print()
question(8)
print()
x = input("What player has the highest career FT percentage: ?")
if x == "Steve Nash" or x == "steve nash":
    print("Correct! Steve Nash had a caeer FT % of .9043")
    score += 1
elif x != "Steve Nash" or x != "steve nash":
    print("Incorrect! You get one more guess")
    x = input("Guess again: ")
    if x == "Steve Nash" or x == "steve nash":
        print("Correct! Steve Nash had a caeer FT % of .9043")
        score += 1
    else:
        print("Sorry- The correct answer was Steve Nash")
        score -= 1

      
totalScore = numq - score
print(totalScore)
################################################3
from random import choice, sample
a = "Who one the 2012 NBA Finals MVP: "
b = "What player has the highest career PPG?: "
c = "What team won the first NBA championship?: "
d = "Who has the most career rebounds?: "
e = "Who was the #1 pick in the 1996 draft: " #Allen iverson
f = "Most coaching titles?: " #Phil Jackson, 11
g= "What player won the most regular season MVP's: ?" #Kareem Abdul- Jabbar, 6
h= "What player has the highest career FT percentage?: " #Steve Nash, .9043
i= "Who has the most coaching wins: " #Don Nelson, 1,335
j= "What team drafted Ray Allen?: " # Minnesota Timberwolves
k= "What year was the first time an NBA finals went to 7 games?: " # 1950-51
l= "Who is the first player to be drafted #1 without playing college or high school basketball in the U.S.?: " #Yao Ming
m= "What team drafted Kobe Bryant: ?" # Charlotte Hornets
n= "Who is the lowest seeded team to win the NBA title?: " # Rockets, 6th seed
o= "Who is the lowest seeded team to make it to the NBA Finals?: " #Knicks, 8th seed

lst = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
x = choice(lst(input("What's your guess: ?")))
if x == a:
    print("good guess")
else:
    print("wrong guess")

ORIGINAL WORKING EXAMPLE OF NBATRIVIA:
if answer == triviaAnswer[4].lower():
    print("CORRECT!", trivia[4])
    score += 1
elif answer == '0' or answer == '':
    exit()
else:
    print("Incorrect")
'''

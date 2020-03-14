#!/usr/bin/python3
##################################################################################################################
#### IMPORTS #####################################################################################################
import random
import requests
import json
##################################################################################################################
#### MAIN EVENT START ############################################################################################
print("--------------------------------------- QUIZ using open Trivia api ---------------------------------------\n")
##################################################################################################################
###### DECLARATIONS
roundStart_failsafe = False
main_failsafe = False
##################################################################################################################
###### FUNCTIONS
def NewRoundData():
    r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=medium&type=multiple")
    NewRounJsonData = json.loads(r.text)
    return NewRounJsonData
def GetNewQuestion(x):
    newQuestion = x["results"][0]["question"]
    return newQuestion
def GetCorrectAnswer(x):
    correctAnswer = x["results"][0]["correct_answer"]
    return correctAnswer
def GetIncorrectAnswers(x):
    IncorrectAnswersList = x["results"][0]["incorrect_answers"]
    return IncorrectAnswersList
def GetQuizAnswerEllements(x,y):
    possibleAnswersList = []
    possibleAnswersList.append(x)
    incoAnswer1=y[0]
    incoAnswer2=y[1]
    incoAnswer3=y[2]
    possibleAnswersList.append(incoAnswer1)
    possibleAnswersList.append(incoAnswer2)
    possibleAnswersList.append(incoAnswer3)
    FinalElementsList = random.sample(possibleAnswersList,len(possibleAnswersList))
    return FinalElementsList
def DataTreatment(i,c,e):
    response = ""
    if(i == "A"):
        if(c==e[0]):
            response = "ok"
    elif(i == "B"):
        if(c==e[1]):
            response = "ok"
    elif(i == "C"):
        if(c==e[2]):
            response = "ok"
    elif(i == "D"):
        if(c==e[3]):
            response = "ok"
    else:
        response = "no"
    return response
##################################################################################################################
###### LOGIC
while main_failsafe == False:
    userChoice = input("Would you like to Play a Musical quiz ?  (yes/no): ").lower()
    if userChoice == "yes":
        while roundStart_failsafe == False:
            newRound = NewRoundData()
            question = GetNewQuestion(newRound)
            correct_answer = GetCorrectAnswer(newRound)
            incorrect_answers = GetIncorrectAnswers(newRound)
            quizAnswerElements = GetQuizAnswerEllements(correct_answer,incorrect_answers)

            print("\nQuestion:",question)
            print("\n\t\t#answer [A]:",quizAnswerElements[0])
            print("\t\t#answer [B]:",quizAnswerElements[1])
            print("\t\t#answer [C]:",quizAnswerElements[2])
            print("\t\t#answer [D]:",quizAnswerElements[3])
            while True:
                usrChoice = input("\n\t\t\tFrom the Answers Above, type the most Correct answer (A/B/C/D): ").upper()
                if(usrChoice == "A" or usrChoice == "B" or usrChoice == "C" or usrChoice == "D" ):
                    break
                else:
                    print("Wrong input, only input of (A/B/C/D) are allowed.")
                    continue
            if DataTreatment(usrChoice,correct_answer,quizAnswerElements) == "ok":
                print("Congratulations, "+usrChoice+" is the right choice.")
            else:
                print("Sadly, "+usrChoice+" Was not the right answer, the correct Answer is "+correct_answer+".")
            while True:
                secondChoice = input("Would you Like to play Again or Quit? (play/quit): ")
                if secondChoice == "play":
                    break
                elif secondChoice == "quit":
                    print("that was fun, see you again later!")
                    roundStart_failsafe = True
                    main_failsafe = True
                    break
                else:
                    print("Invalid input, please type in either 'play' or 'quit'")
                    continue
    elif(userChoice == "no"):
        print("Shame, i was hopping you could play with me, see you later :-) ")
        main_failsafe = True
    else:
        print("Invalid Input, Only 'yes' or 'no' are valid")
        continue
##################################################################################################################
print("\n---------------------------------------------------END-----------------------------------------------------")
#### MAIN EVENT END ##############################################################################################
##################################################################################################################
# sorry for typos if any

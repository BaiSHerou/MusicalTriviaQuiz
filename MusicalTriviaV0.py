#!/usr/bin/python3
##################################################################################################################
#### IMPORTS #####################################################################################################
# import time as t
# import datetime as dt
# import math
import random
# import matplotlib.pyplot as plt
import requests
import json
# import pprint
import html
import os
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
    newQuestion = html.unescape(x["results"][0]["question"])
    return newQuestion
def GetCorrectAnswer(x):
    correctAnswer = x["results"][0]["correct_answer"]
    return correctAnswer
def GetIncorrectAnswers(x):
    IncorrectAnswersList = x["results"][0]["incorrect_answers"]
    return IncorrectAnswersList
def GetQuizAnswerEllements(x,y):
    ElementsList = y
    ElementsList.append(x)
    FinalElementsList = random.sample(ElementsList,len(ElementsList))
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
        os.system("clear")
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
                    print("\n\t\tWrong input, only input of (A/B/C/D) are allowed.")
                    continue
            if DataTreatment(usrChoice,correct_answer,quizAnswerElements) == "ok":
                print("\n\t\tCongratulations, "+usrChoice+" is the right choice.")
            else:
                print("\n\t\tSadly, "+usrChoice+" Was not the right answer, the correct Answer is "+correct_answer+".")
            while True:
                secondChoice = input("\t\t\tWould you Like to play Again or Quit? (play/quit): ")
                if secondChoice == "play":
                    os.system("clear")
                    break
                elif secondChoice == "quit":
                    print("\n\t\tthat was fun, see you again later!")
                    roundStart_failsafe = True
                    main_failsafe = True
                    break
                else:
                    print("\n\t\tInvalid input, please type in either 'play' or 'quit'")
                    continue
    elif(userChoice == "no"):
        os.system("clear")
        print("Shame, i was hopping you could play with me, see you later :-) ")
        main_failsafe = True
    else:
        os.system("clear")
        print("Invalid Input, Only 'yes' or 'no' are valid")
        continue
##################################################################################################################
print("\n---------------------------------------------------END-----------------------------------------------------")
#### MAIN EVENT END ##############################################################################################
##################################################################################################################

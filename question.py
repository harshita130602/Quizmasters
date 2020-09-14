import json
import time

# Python program to print colored text and background 
class colors:  
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'
    bold = '\033[1m'

TOPICS_LIST = ['science', 'history'] 

def ask_one_question(question):
    print("\n" + question)
    choice = input(f"{colors.darkgrey}Enter Your Choice [a/b/c/d]: ")
    while(True):
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print(f"{colors.darkgrey}Invalid choice. Enter again")
            choice = input("Enter Choice [a/b/c/d]: ")

def score_one_result(key, meta):
    actual = meta["answer"]
    if meta["user_response"].lower() == actual.lower():
        i=1
        print(f"{colors.green}Q.{i} Good Job! Absolutely Correct answer!\n".format(key))
        i+=1
        return 2
    else:
        i=1
        print(f"{colors.red}Q.{i} Oops! Incorrect answer!".format(key))
        print("Right Answer is ({i})".format(actual))
        i+=1
        print (f"{colors.blue}Learn more : " + meta["more_info"] + "\n")
        return -1

def test(questions):
    score = 0
    print(f"{colors.darkgrey}\nGENERAL INSTRUCTIONS:\n1. Please enter only the choice letter corresponding to the correct answer.\n2. Each question carries 2 points\n3. Wrong answer leads to -1 marks per question\nQuiz will start momentarily. GOOD LUCK! :)\n")
    time.sleep(5)
    for key, meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])
    print(f"{colors.purple}\n\n***************** RESULT ********************\n")
    for key, meta in questions.items():
        score += score_one_result(key, meta)
    print(f"\n{colors.purple}YOUR SCORE:", score, "/", (2 * len(questions)))
    print("\n")
    print("\n")

def load_question(filename):
    """
    loads the questions from the JSON file into a Python dictionary and returns it
    """
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)

def play_quiz():
    flag= False
    try:
        inp = int(input(f"{colors.orange}\n Please enter your interest:\n(1). Science\n(2). History\n(3). Commerce\n(4). Technology\n(5). World Gk\nEnter Your Choice [1/2/3/4/5]: "))
        if inp > len(TOPICS_LIST) or inp < 1:
            print(f"\n {colors.yellow} Invalid input! Please try again.\n ")
            flag = True
    except ValueError as e:
        print(f"\n {colors.yellow} Invalid Input! Please try again\n")
        flag = True

    if not flag:
        questions = load_question('quiz_topics/'+TOPICS_LIST[inp-1]+'.json')
        test(questions)
    else:
        play_quiz()

def prompt():
    print(f"\n\n{colors.bold}{colors.purple}                   KNOWLEDGE IS LIFE WITH WINGS :) \n")
    print(f"\n{colors.bold}{colors.lightcyan} Welcome to the QUIZMASTERS! Wanna test your knowlege?{colors.pink}\nA. Yes\nB. No")
    play=input()
    if play.lower() == 'a' or play.lower() ==  'y':
        play_quiz()
    elif play.lower() == 'b':
        print(f"{colors.lightcyan}\nHope you come back soon! :)")
    else:
        print(f"{colors.lightcyan}\nI didn't quite understand that.\nPress A to play, or B to quit.")

def execute():
    prompt()

if __name__ == '__main__':
    execute()

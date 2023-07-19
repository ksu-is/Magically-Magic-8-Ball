# This is where the code is going to be.
import random
import time


responses = [
    "Of course.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes, definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "For real for real.",
    "Outlook is good.",
    "Yes.",
    "That is the way it is.",
    "Reply hazy, try again.",
    "Ask again later.",
    "You know it!",
    "Do not count on it.",
    "My reply is no.",
    "No way loser.",
    "Outlook is not so good.",
    "Very doubtful."]


def play_game():
    inp = input('What do you need to know from me, the Magically Magic 8 Ball? ')
    print("You asked: '" + str(inp) + "'")
    time.sleep(.5)
    print("Let me see... ")
    time.sleep(1.25) 
    print("...Still thinking... ")
    time.sleep(2)
    print("...Sorry got distracted... ")
    time.sleep(1.5)
    print("...Aha, got it... ")
    time.sleep(2)
    print(responses[random.randint(0, len(responses) - 1)])
    play_again()  

def play_again():
    quest = input("Do you have another question for me? yes or no ")
    if quest == 'yes':
        print('')
        play_game()
    elif quest != 'yes':
        print('')
        time.sleep(1.5)
        print('...Goodbye! ...')
        quit()

play_game()

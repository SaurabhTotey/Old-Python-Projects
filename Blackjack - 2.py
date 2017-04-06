#
#MAKE DEALER DRAW 3 CARDS AND REVEAL IMMIDIATELY WHAT 2 OF THEM ARE BEFORE THE PLAYER DRAWS, AND THEN IF THE USER STANDS OR BUSTS, REVEALS THE 3RD ONE ONLY FOR THE DEALER TO START PLAYING
#Random is imported for the card draw
import random
#
#
#

#
#
#Defining a standard deck and all the scores (for all the possible ace draws) as well as the actual deck which atm is empty
STDeck = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
ActualDeck = []
Score1 = 0
Score2 = 0
Continue = True
TimesRun = 0
TotalCards = 0
#
#
#

#
#
#This is how cards will be drawn and removed from the deck
def Draw_A_Card(current_deck):
    
    #This loop checks that as long as there are cards to be drawn, cards will be drawn, otherwise it will return the deck is empty
    draw_again = False
    for item in current_deck:
        if item > 0:
            draw_again = True
    if draw_again == False:
        returnstuff = [current_deck, "NO CARDS IN DECK!", 42]
    
    #As long as there are cards to be drawn, a card will be drawn and removed from the deck; if it draws a card that isn't in the deck, it will draw again
    else:
        while draw_again == True:
            cardraw = random.randint(1, 13)
            current_deck[cardraw-1] -= 1
            if current_deck[cardraw-1] < 0:
                draw_again = True
            else:
                draw_again = False
        
        #This checks what actual card was drawn, and sets facecards to 10
        if cardraw == 1:
            typeofcard = "you drew an Ace!"
        elif cardraw == 8:
            typeofcard = "you drew an 8!"
        elif cardraw == 11:
            typeofcard = "you drew a Jack!"
            cardraw = 10
        elif cardraw == 12:
            typeofcard = "you drew a Queen!"
            cardraw = 10
        elif cardraw == 13:
            typeofcard = "you drew a King!"
            cardraw = 10
        else:
            typeofcard = "you drew a " + str(cardraw) + "!"
                
        #It makes the return variable a list: the first element is the new deck, the second element being the current draw        
        returnstuff = [current_deck, cardraw, typeofcard]
    return returnstuff
#
#
#

#
#Do current cards/ total cards to see if the deck is legal within threshold
#This bit of code multiplies the deck by however many decks they want as well as setting up a threshold (WIP)
Multiplier = int(raw_input("How many decks do you want to use? "))
for item in STDeck:
    ActualDeck.append(item * Multiplier)
for item in ActualDeck:
    TotalCards += 1
STDeck = ActualDeck
Threshold = float(raw_input("What percentage of cards do you want the deck to go to before it reshuffles? ")) * (100 ** -1)
#
#
#

#
#
#This draws 3 cards for the dealer opponent and does the score

#
#
#

#
#
#Main program
while Continue == True or TimesRun < 2:
    TimesRun +=1
    CardAndDeck = Draw_A_Card(ActualDeck)
    CardValue = CardAndDeck[1]
    ActualDeck = CardAndDeck[0]
    Card = CardAndDeck[2]
    if CardValue == "NO CARDS IN DECK!":
        print "Unfortunately, the deck is empty; a draw could not be made... "
        Continue = False
    else:
        Continue = "up for decision"
        if CardValue != 1:
            Score1 += CardValue
            Score2 += CardValue
        else:
            Score1 += CardValue
            Score2 += 11
            if Score2 > 21 and Score1 + 10 < 21:
                Score2 = Score1 + 10
        if Score1 == Score2 < 21 or (Score1 < 21 and Score2 > 21):
            print "Your total score is " + str(Score1) + " because " + Card
        elif Score1 != Score2 and Score2 < 21:
            print "Your total score is " + str(Score1) + " or " + str(Score2) + " because " + Card
        elif Score1 > 21 and Score2 > 21:
            print "You busted because " + Card
            Continue = "n"
        elif Score1 == 21 or Score2 == 21:
            print "Jackpot because " + Card
            Continue = "n"
        while Continue[0].lower() != "y" and Continue[0].lower() != "n" and TimesRun >= 2:
            Continue = raw_input("Draw again? ")
        if Continue[0].lower() == "y":
            Continue = True
        else:
            Continue = False

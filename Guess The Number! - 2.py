#Saurabh Totey
import random

bodyIsReady = "no"
playerScore = 0
compScore = 0
compGuess = 0
playerGuess = 0
playerCorrect = 0
compCorrect = 0

toWin = int(raw_input('To how many points do you want to play? Short is around 10 points, Medium is around 20, Long is around 30, and Extra-Long is around 50. If you want to see if you are lucky, try 100! '))
toGuess = int(raw_input('From 1 to what do you want to be guessing numbers? '))
print "Welcome to BEAT THE COMPUTER!\nIn this game, you need to guess a correct number between 1 and " + str(toGuess) + ". Whatever the number was will get added to your score if you guessed correctly. Otherwise, the computer will take a guess at the correct number for the chance to gain some points! Whoever gets to " + str(toWin) + " first gets " + str(toWin/5) + " extra bonus points! Also, for every number you get right, 4 points will get added to your score!"

while bodyIsReady[0].lower() != "y":
    bodyIsReady = raw_input('Are you ready to play? ')
    
compListVar = toGuess + 1
compList = []
while compListVar > 0:
    compListVar = compListVar - 1
    compList.append(compListVar)

while playerScore <= toWin and compScore <= toWin:
    GUESS_ME = random.randint(1, toGuess)
    compSmart = random.randint(1, 4)
    previousGuesses = []
    compGuess = 0
    playerGuess = 0
    while playerGuess != GUESS_ME and compGuess != GUESS_ME:
        compGuess = 0
        playerGuess = 0
        playerGuess = int(raw_input('Guess an integer between 1 and ' + str(toGuess) + ' ! '))
        while playerGuess not in compList or playerGuess in previousGuesses:
            print str(playerGuess) + " is not a guessable number, or that number was guessed... Please guess another number from 1 to " + str(toGuess) + "."
            playerGuess = int(raw_input('Guess an integer between 1 and ' + str(toGuess) + '! '))
        previousGuesses.append(playerGuess)
        if compSmart == 4:
            compGuess = toGuess
        while compGuess in previousGuesses or compGuess == 0:
            if len(previousGuesses) == toGuess:
                compGuess = "nothing because of the lack of remaining available guesses"
            elif compSmart == 4:
                compGuess = compGuess - 1
            else:
                compGuess = random.randint(1, toGuess)
        previousGuesses.append(compGuess)
        if playerGuess == GUESS_ME:
            playerScore += GUESS_ME
            playerCorrect += 1
            print "Good job, you guessed the number            " + str(GUESS_ME) + " correctly! Your new total score is " + str(playerScore) + "!"
        elif compGuess == GUESS_ME:
            compScore += GUESS_ME
            compCorrect += 1
            print "Unfortunately for you, the computer guessed " + str(GUESS_ME) + " correctly! It's new total score is " + str(compScore) + "!"
        else:
            print "Your guess of " + str(playerGuess) + " and the computer's guess of " + str(compGuess) + " were both wrong! Guess again!"
        random.seed(compGuess)
           
if playerScore >= toWin:
    print "Congratulations, you are awarded " + str(toWin/5) + " bonus points! Good guessing! The computer had " + str(compScore) + " points! You had " + str(playerCorrect) + " correct guesses. Now your scores will be totaled!"
    playerScore += (toWin/5)
else:
    print "Aw, Shucks, the computer was awarded with " + str(toWin/5) + " bonus points. Better luck next time... You had " + str(playerScore) + " points. You had " + str(compCorrect) + " correct guesses. Now your scores will be totaled!"
    compScore += (toWin/5)

playerScore += (playerCorrect*4)
compScore += (compCorrect*4)

if playerScore > compScore:
    print "YOU WON WITH " + str(playerScore) + " POINTS! NICE!"
elif playerScore < compScore:
    print "CRAP, you lost by " + str(compScore-playerScore) + " points :("
elif playerScore == compScore:
    print "You both tied with " + str(playerScore) + " points. "

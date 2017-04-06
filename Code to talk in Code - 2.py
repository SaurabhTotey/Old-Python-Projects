#Random is imported to "randomly" select letters
#Because the computer doesn't ever truly randomly select anything
#We are relying on a set seed to figure out how the message was encoded
#This is done by doing the same thing the encoding part of the prgm does
import random

#Time is needed to find when the message was written
#The time of when the message was written will become the seed for random
#But it will be stored in a variable, so that it can be used as the seed to decode the message
#From this, the message letters and length will change by when the message was written
import time

#Pyperclip is installed to copy the encoded message as to save time
import pyperclip

#This function returns a random letter from the list of possible letters
#The list of possible letters is stored in the variable "alphabet"
#A random character from "alphabet" is returned "randomly"
def randletter():
    alphabet = "abcdefghijklmnopqrstuvwxyz' .ABCDEFGHIJKLMNOPQRSTUVWXYZ()*&^%$#@!?><`~][}{=-+_/|\"\\"
    return alphabet[random.randint(0, 81)]

#This function is solely used for the decoding part of the prgm
#It takes the message of "message:seed(time it was written during):length"
#And seperates it out on each element
def codeToList(code):
    message = ""
    seed = ""
    length = ""
    hasreachedcolon = 0
    for i in range(0, len(code), 1):
        if code[i] == ":":
            hasreachedcolon += 1
        elif hasreachedcolon == 0:
            message += code[i]
        elif hasreachedcolon == 1:
            seed += code[i]
        elif hasreachedcolon == 2:
            length += code[i]
    return [message, seed, length]

#This if statement figures which half of the prgm to run: decoding, or encoding
#If the first letter of their response is "y" or "Y", then it will do this encoding
#Otherwise, it will just default to the decoding section
if raw_input("Do you want to write a message in code? ")[0].lower() == "y":

    #This just takes the text they want to encode as a string
    #If they enter in any number (eg. 1, 2, 3, ...) or a colon (:), the prgm will break
    message = raw_input("What message do you want to encrypt? ")

    #The output string starts off as nothing, but it is set to a string to begin with so it can be added to
    output = ""
    #The time of when the prgm was run is taken to later be used as a seed and is stored in a variable for later
    time = time.time()
    #The time which the prgm was run is set as the seed
    #This makes it so that one message won't encode into the same thing more than once unless under the circumstances of extreme luck
    random.seed(time)
    #The message is turned into a list for convenience purposes
    #This is completely unecessary, and can be removed later if needed
    listmessage = list(message)
    #The list "numberused" is used to only draw new numbers
    #There are more simpler ways to do this, except the problem is that this method makes decoding much simpler
    numbersused = []
    #This variable is just to run the encoding part the correct number of times
    letters = len(listmessage)

    #This loop runs the prgm the correct amount of times based off of how many letters were in the original message
    while letters > 0:
        #To the final string, it adds a random letter with the randletter function
        output += randletter()
        #After having at least 1 random letter, a "random" amount of random letters are also added in
        while random.randint(0, 1) == 1:
            output += randletter()
        #Then, a "random" number is generated based off of the amount of characters in the original message
        random_number = random.randint(0, len(listmessage) - 1)
        #If/While the previously generated random number has been generated more than once, it will draw another random number that hasn't been drawn
        while str(random_number) in numbersused:
            random_number = random.randint(0, len(listmessage) - 1)
        #When finally a new random number has been drawn, it will add that number to the list of previously drawn numbers
        #This makes it so that this random number can't be drawn again
        numbersused.append(str(random_number))
        #Because the randomly generated number was made so that it would correspond to a letter of the original message
        #It takes the corresponding letter of the original message and adds it to the final output
        output += listmessage[random_number]
        #This variable decreases by 1 to signify one less letter is needing to be added to the final output
        #While this variable is greater than 0, meaning there exist letters that still need to be added to the final output,
        #This process will run over
        letters -= 1
    #After all letters have been added, it adds a random amount of letters to the end of the output
    while random.randint(0, 1) == 1:
        output += randletter()
    #Just in case the random amount of added letters was 0, another random letter is added in for good cause
    output += randletter()

    #The output is given as the message, seed (time of prgm usage), and length of message
    #This is all the necessary information to replicate this process to decode the message
    print output + ":" + str(time) + ":" + str(len(message))
    #This line just copies the previous printed thing to the clipboard
    pyperclip.copy(output + ":" + str(time) + ":" + str(len(message)))

#If the user doesn't want to encode a message, the prgm defaults to them wanting to decode a message
else:
    #The to-be-decoded message is obtained from the user and turned promptly to a list
    message = list(raw_input("What message do you want me to decode? "))
    #The output variable is initialized and turned into a list, except it is empty
    #This is where the pseudo-final construct of the code will go
    #From this, the encoded message will be compared with the pseudo-final construct, and analyzed for differences
    #The differences will be un-anagrammed and turned into the final string of what the original message was
    output = []
    #From the output of the encoding section, the message, seed (time of original prgm usage), and length are obtained
    #The above are obtained and separated into separate variables for convenience and ease of usage
    codelength = codeToList(message)
    message = codelength[0]
    code = codelength[1]
    length = int(codelength[2])

    #The code (time of original prgm usage) obtained from the previous process will then be seeded for the random
    #This will simulate the same exact random calls as previously happened when encoding said messsage
    #The only difference between this one and the simulated version is that instead of the original message's characters,
    #This version will have integers (which is why entering integers in the original message would break it)
    #The integers will then be compared with the original message's characters to find where in the string those characters went
    random.seed(float(code))
    #As with the encoding portion, this variable is also needed; it is used to track which integers have been "randomly" called,
    #and is used so that they won't be called again so each letter from the original message was only placed in the code once
    numbers_called = []
    #The finalmessage variable is initialized as a string so that the original message can be stored in it and displayed
    finalmessage = ""

    #See the encoding section to figure out how this works; this is exactly the same except for one key difference
    #In the encoding section, it would take the randomnumbered letter of the original message (eg. randomnumber = 4, message = "stuff", it would take "f")
    #Instead, in this section, it will just store the number in the string, not the letter corresponding to the number
    #This will be used when comparing the encoded message with the pseudo-encoded message, the numbers in the pseudo-final version
    #correspond to original letters from the first message; they tell which numbered letter they were in the original saving time from figuring out anagrams
    for i in range(0, length, 1):
        output.append(randletter())
        while random.randint(0, 1) == 1:
            output.append(randletter())
        random_number = random.randint(0, length - 1)
        while str(random_number) in numbers_called:
            random_number = random.randint(0, length - 1)
        numbers_called.append(str(random_number))
        output.append(str(random_number))
    while random.randint(0, 1) == 1:
        output.append(randletter())
    output.append(randletter())

    #Now that the original message and pseudo-final message have been generated, this block of code compares each list to find the original string
    #It repeats the following for every letter of the encoded message
    for a in range(0, len(message), 1):
        #This loop checks each letter of the pseudo-final string, if it is the same as the number it needs (eg. It will look for 1 first, then 2, then 3)
        #To understand which number it will look for, it will look at the bigger loop above
        #Once it finds that number in the pseudo final message, it knows that the same spot in the encoded message is an actual letter of the original message
        #To find out why there are numbers in the pseudo-final message, check the above code
        #Because every number in the pseudo-final code corresponds to the same-placed letter in the encoded message's place in the original string
        #(eg. 4 maps to "f", therefore "f" is the fourth letter of the original message)
        #We can reconstruct the original message and in order
        for b in range(0, len(message) - 1, 1):
            if output[b] == str(a):
                #Each letter in order is added to the finalmessage string (eg. first letter added first, second letter added second)
                finalmessage += message[b]

    #Now that the original message has been stored in a variable, the only remaining step is to display the original message to the user
    print "\"" + str(finalmessage) + "\""

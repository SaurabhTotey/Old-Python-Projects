import math

#Setting all these variables to 0
#The numerator and denominator are both 0 to begin with
num = 0
denom = 0

#This function just does the factorial of a number so I won't need to import the math module
#Currently unused because it makes the program run slower
'''
def factorialOf(takeFof):

    #Factorial is set default to 1 instead of zero so that it can be multiplied with correctly in the following loop
    factorialResult = 1

    #Standard factorial: takes a number and multiplies it with all positive non-zero integers before it
    #This excludes multiplying the result by 1 because that is unecessary and it already gets multiplied by 1 because that is what factorialResult is set to
    for i in range(0, takeFof - 1, 1):
        factorialResult *= takeFof - i

    #Gives back the factorial
    return factorialResult


#This function is used to make sure that fractions numerators and denominators are simplifying to integers and not floats
def isInt(Float):
    #stringOfNumber is a string of the number with a decimal afterwards
    #if the number is an int, the decimal afterwards should just be .0
    stringOfNumber = str(Float)

    #This just checks if the last part of the string is a 0
    #If it is, the number is an integer that was converted to a float with an end of .0
    #Otherwise, the number isInt an int
    if stringOfNumber[len(stringOfNumber) - 1] != "0":
        return False
    else:
        return True

#This function simplifies the fraction to decrease the length of the output and make it easier to understand
def factorFraction(numerator, denominator):

    #A number can at max only be divisible by its half
    #Because both the numerator and denominator have to be divisible by the same number, I will take the half of the denominator
    #This is because the denominator tends to be smaller than the numerator and therefore is less things to check 
    highestIntToCheck = int(denominator / 2)

    #This loop will try to divide the numerator and denominator by the greatest int
    #If they aren't ints, the fraction can't be simplified by that factor, and then the factor gets reduced by 1 and the loop tries again
    #Eventually, this loop will reach the number 1, which the numerator and denominator are always factorable with, so thats what will get returned if the fraction can't be simplified
    for i in range(0, highestIntToCheck, 1):
        if isInt(numerator/float(highestIntToCheck - i)) and isInt(denominator/float(highestIntToCheck - i)):
            return [int(numerator/(highestIntToCheck - i)), int(denominator/(highestIntToCheck - i))]
    #Just in case
    return [numerator, denominator]
'''

#The main part of the program is ready to run
#This part runs 170 times because after that, the variables get too large for the memory to hold
#This part of the program is run repeatedly, as a sum is being calculated
#The larger x gets, the more accurate the sum is
for x in range(0, 171, 1):

    #The numerator and the denominator are calculated from the previous results as well as how many times this part has run
    '''    
    denom = factorialOf(x)
    '''
    denom = math.factorial(x)
    num = (num * x) + 1

    #This will be the fraction in its simplified form
    '''
    simpleFrac = factorFraction(num, denom)
    simpleNum = simpleFrac[0]
    simpleDenom = simpleFrac[1]
    '''
    
    GCD = math.gcd(num, denom)
    simpleNum = int(num / GCD)
    simpleDenom = int(denom / GCD)

    #The output of the current stage is shown in fractional and decimal form
    #A lot of this print statement is just formatting things to make the output pretty
    print("\n" + (" " * (len(str(x)) + 2)) + str(simpleNum) + "\n" + str(x) + ". " + ("-" * len(str(simpleNum))) + " = " + str(float(simpleNum * (simpleDenom ** (-1)))) + "\n" + (" " * (len(str(x)) + 2)) + str(simpleDenom) + "\n")
    #This is the old print statement that would do unsimplified form
    #print("\n" + (" " * (len(str(x)) + 2)) + str(num) + "\n" + str(x) + ". " + ("-" * len(str(num))) + " = " + str(float(num * (denom ** (-1)))) + "\n" + (" " * (len(str(x)) + 2)) + str(denom) + "\n")

#Just so the output won't close out until the user presses "Enter"
input("Press Enter to continue... ")

# ------------------------------------------------------
#        Name: Rebecca Morrison
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Gets an input from the user and determines if it's either the secret word or the word dog.
    If it is one those, it will print that. If it is not, it will print 'Try again.'"""
    
    # Setting up an infinite loop
    x = 1
    while x == 1:
        # Getting an input from the user
        i = input("Give me a sentence: ")
        # If the secret word is typed, printing that the secret word was used and breaking the loop
        if secret_word in i:
            print("You used the secret word!")
            break
        # If the word 'dog' or 'Dog' is used, printing that the word was used and breaking the loop
        elif "dog" in i or "Dog" in i:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        # If neither is typed, printing 'Try again' and the loop remains unbroken thus it repeats
        else:
            print("Try again")

# Task 2
def check_greater():
    """ Getting two variables and printing their relatinoship if they are not equal, otherwise
    telling the user to try again. """
    
    # Setting up an infinite loop
    z = 1
    while z == 1:
        # Getting two variable inputs
        x = input("Enter a variable: ")
        y = input("Enter another variable: ")
        #Printing if the first is greater than the second number, or vice versa
        if x > y:
            print("First is Greater")
            break
        elif x < y:
            print("Second is Greater")
            break
        # Telling the user to try again if the numbers are equal
        elif x == y:
            print("Try again")

# Task 3
def get_special_numbers():
    """ Printing numbers that are between 1 and 40, even, divisible by 3, and not divisible by 5. """
    
    # Setting the base value of n
    n = 1
    # Looping for the range (1, 40)
    for n in range(1,41):
        # If a number is fails any of the requirements, the next number is tried and loop repeats
        if n%2 == 0:
            n=n+1
            continue
        if n%3 != 0:
            n=n+1
            continue
        if n%5 == 0:
            n=n+1
            continue
        # If a number does not fail any of the requirements, the number is printed and the next number is tried
        else:
            print(n)
            n=n+1

# Task 4.a
def my_for_loop():
    """ Getting a 2-5 letter long word and printing each letter and if it is a vowel
    or a consonant. """
    
    # Getting the input
    i = input("Give me a word from 2 to 5 letters long: ")
    # Exits the code if the input is not in the range or is multiple words
    if len(i) < 2 or len(i) > 5:
        print("bad word")
        return
    if " " in i:
        print("bad word")
        return
    # If the input is good, prints each letter in the word and whether it is a consonant or a vowel
    else:
        for let in i:
            if let == "a" or let == "A" or let == "e" or let == "E" or let == "i" or let == "I" or let == "o" or let == "O" or let == "u" or let == "U":
                print(f"{let} is a vowel")
            else:
                print(f"{let} is a consonant")

# Task 4.b
def my_while_loop():
    """ Doing various actions depending on user input a, b, c, or none of those. """
    
    # Setting up an infinite loop
    x = 1
    while x == 1:
        # Getting user input
        i = input("Choose a, b, or c: ")
        # Repeating input phase if 'a' is chosen
        if i == "a":
            continue
        # Printing 'Goodbye' and breaking the loop if 'b' is chosen
        if i == "b":
            print("Goodbye")
            break
        # Exiting the entire program if 'c' is chosen
        if i == "c":
            exit()
        # Printing 'try again' and  repeating the loop if anything else is written
        else:
            print("try again")
# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

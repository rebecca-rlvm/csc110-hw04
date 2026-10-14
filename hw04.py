# ------------------------------------------------------
#        Name: Rebecca Morrison
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Add your docstring """
    x = 1
    while x == 1:
        i = input("Give me a sentence: ")
        if secret_word in i:
            print("You used the secret word!")
            break
        elif "dog" in i or "Dog" in i:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        else:
            print("Try again")

# Task 2
def check_greater():
    """ Add your docstring """
    z = 1
    while z == 1:
        x = input("Enter a variable: ")
        y = input("Enter another variable: ")
        if x > y:
            print("First is Greater")
            break
        elif x < y:
            print("Second is Greater")
            break
        elif x == y:
            print("Try again")

# Task 3
def get_special_numbers():
    """ Add your docstring """
    n = 1
    for n in range(1,40):
        if n%2 == 0:
            n=n+1
            continue
        if n%3 != 0:
            n=n+1
            continue
        if n%5 == 0:
            n=n+1
            continue
        else:
            print(n)
            n=n+1

# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

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

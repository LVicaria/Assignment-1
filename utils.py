"""
Utility module for supporting the bouncing ball programme.
"""
import os

ETA = "\u03B7"

H_MIN = "h{}{}{}".format('\N{LATIN SUBSCRIPT SMALL LETTER m}',
                         '\N{LATIN SUBSCRIPT SMALL LETTER i}',
                         '\N{LATIN SUBSCRIPT SMALL LETTER n}')
FORMULA = "mg" + H_MIN + " = mgh" + ETA + "\u207F"


def cls():
    """
    Clears the console before starting the program.
    Checks first if we are running on Windows or Linux
    """
    os.system('cls' if os.name == 'nt' else 'clear')


Style = {'BLACK': '\033[30m', 'RED': '\033[31m', 'GREEN': '\033[32m',
         'YELLOW': '\033[33m', 'BLUE': '\033[34m', 'MAGENTA': '\033[35m',
         'CYAN': '\033[36m', 'WHITE': '\033[37m', 'UNDERLINE': '\033[4m',
         'RESET': '\033[0m'}


def print_title():
    """
    Prints the title message for the programme
    """
    # cls()
    print(Style['GREEN'] + "\n************************************************"
          + Style['RESET'])
    print(Style['YELLOW'] + " PHYS20161 1st assignment: Bouncy Ball")
    print(" September 6, 2022")
    print(" By Luca Vicaria")
    print(Style['GREEN'] + "************************************************\n"
          + Style['RESET'])


def print_explanation():
    """
    Prints the presentation/explanation of the programme
    """
    print("This programme makes a series of calculations regarding a bouncy "
          "ball bouncing above some minimum height.")
    print("We can calculate the number of bounces analytically using "
          "conservation of energy.")
    print("At height h the ball will have a potential energy of mgh, where the"
          " symbols have their usual meanings.\n")
    print("After one bounce the ball reaches a height h" + ETA +
          " (0 < " + ETA + " < 1) where " + ETA
          + " takes into account energy lost during each bounce "
            "(an efficiency if you will)."
          + " After a second bounce the ball will reach a height h" + ETA
          + "\u00b2, and so on.\n")
    print("We can find the number of bounces above some minimum height, "
          + H_MIN + ", by examining the energy loss:\n")
    print(Style['GREEN'] + "  " + FORMULA + "\n" + Style['RESET'])
    print('where n represents the number of bounces.\n')


def validate_float_input(value):
    """
    Validate float input
    """
    try:
        _ = float(value)
        return True
    except ValueError:
        print(Style['RED'] + "ERROR: " + Style['RESET']
              + "Input must be a number! (Ex. 5, 2.35 etc.) Please try again.")
        return False


def validate_positive_input(value: float):
    """
    Validate positive value. Assumes value is a float.
    """
    if float(value) <= 0.0:
        print(Style['RED'] + "ERROR: " + Style['RESET']
              + "Input must be a positive value! Please try again.")
        return False
    return True


def validate_greater_than_input(value: float, minvalue: float):
    """
    Validate grater than value. Assumes value and minvalue are floats.
    """
    if float(value) <= float(minvalue):
        print(Style['RED'] + "ERROR: " + Style['RESET']
              + f"Input must be greater than {minvalue}! Please try again.")
        return False
    return True


def validate_smaller_than_input(value: float, maxvalue: float):
    """
    Validate greater than value. Assumes value and maxvalue are floats.
    """
    if float(value) >= float(maxvalue):
        print(Style['RED'] + "ERROR: " + Style['RESET']
              + f"Input must be smaller than {maxvalue}! Please try again.")
        return False
    return True


def print_cancelled_by_user():
    """
    Prints message when user cancels programme.
    """
    print(Style['RED'] + "\nCancelled by user." + Style['RESET'])


def validate_y_n_input(question):
    """
    Ensures the questions are answered correctly.
    """
    while True:
        answer = input(question).lower()
        if answer not in ('y', 'n'):
            print(Style['RED'] + "ERROR: " + Style['RESET']
                  + "Input must be y or n.")
        else:
            return answer
        

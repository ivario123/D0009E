from Labb2Del1_4 import *
from Labb2Del5 import *

def option(selection):
    ValidInput = ["bounce","tvärsumman","lös","avsluta programmet"]
    if selection not in ValidInput:
        raise Exception("Invalid input")
    if(sellection == "bounce"):
        return bounce(int(input("Vilket tal ska vi starta på?\n"),))
def menu():
    message = """
    Meny lista
    -------------------------------------------------------------------------
    Välj ett alternativ genom att skriva namnet
    -------------------------------------------------------------------------
    1 : bounce
    2 : tvärsumman
    3 : lös (löser f(x) = x^2-1)
    4 : avsluta programmet
    -------------------------------------------------------------------------
    """
    return input(message)
def ping():
    try:
        return option(menu())
    except:
        print("Felaktig input",)
        ping()
if __name__ == "__main__":
    ping()
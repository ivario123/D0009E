#En fin liten funktion som bara skriver ut förklaringen av ett ord
def Explain(ord,exp):
    #Skriver ut förklaringen på ett lite trevligare sätt
    return "Förklaring av {} > {}".format(ord,exp)
#Funktionen som tar bort en instans i en lista
def pop1(ord):
    ord = ord.lower()
    try:
            Exp.pop(Ord.index(ord))
            Ord.pop(Ord.index(ord))
            return "\"pop\""
    except:
            return "Ordet finns inte"
        
def Append1(ord,exp):
    ord = ord.lower()
    if ord in Ord:
            print("Finns redan i listan")
            return
    #Lägger till ett nytt ord i ordlistan
    Ord.append(ord)
    Exp.append(exp)
    #Lägger till en ny förklaring i förklarings listan
def lookup1(ord):
    ord = ord.lower()
    return Explain(ord,Exp[Ord.index(ord)]) if ord in Ord else "Finns inte i listan"
def meny1():
    message = """
    Alternativ (ange nummret för alternativet)
    -------------------------------------------------------------------------
    1 : Lägg till nytt ord
    2 : Hitta ord
    3 : Ta bort ord
    4 : Tillbaka till toppen
    -------------------------------------------------------------------------
    Ange index > """
    #testar att läsa användarens input so ett heltal
    #misslyckas detta skrivs ett felmedelande och menyn startar om
    try:
        resp = int(input(message))
    except:
        print("Du måste ange en siffra\n")
        meny1()
        return
    #kollar vad användaren vill göra
    if(resp == 1):
        #Vill användaren lägga till ett nytt ord frågas den samme om ord och förklaring
        
        Append1(input("Vilket ord vill du lägga till\nAnge ord > ")
            ,input("Vad är förklaringen?\nAnge förklaring > "))
    elif resp == 2:
        print(lookup1(input("Vilket ord?\nAnge ord > ")))
    elif resp == 3:
        print(pop1(input("Vilket ord vill du ta bort?\nAnge ord > ")))
    else :
        return
    meny1()

def pop2(ord):
    ord = ord.lower()
    for el in Ord1:
        if el[0] == ord :
            Ord1.pop(Ord1.index(el))
            return "\"pop\""
        return "Ordet finns inte"
def Append2(ord,exp):
    ord = ord.lower()
    for el in Ord1:
        if el[0] == ord :
            print("Finns redan i listan")
            return
    #samma sak fast för tupple metoden
    Ord1.append((ord,exp))
def lookup2(ord):
    ord = ord.lower()
    for el in Ord1:
            if el[0] == ord :
                return Explain(ord,el[1])
    return "Finns inte i listan"
def meny2():
    message = """
    Alternativ (ange nummret för alternativet)
    -------------------------------------------------------------------------
    1 : Lägg till nytt ord
    2 : Hitta ord
    3 : Ta bort ord
    4 : Tillbaka till toppen
    -------------------------------------------------------------------------
    Ange index > """
    #testar att läsa användarens input so ett heltal
    #misslyckas detta skrivs ett felmedelande och menyn startar om
    try:
        resp = int(input(message))
    except:
        print("Du måste ange en siffra\n")
        meny2()
        return
    #kollar vad användaren vill göra
    if(resp == 1):
        #Vill användaren lägga till ett nytt ord frågas den samme om ord och förklaring
        
        Append2(input("Vilket ord vill du lägga till\nAnge ord > ")
            ,input("Vad är förklaringen?\nAnge förklaring > "))
    elif resp == 2:
        print(lookup2(input("Vilket ord?\nAnge ord > ")))
    elif resp == 3:
        print(pop2(input("Vilket ord vill du ta bort?\nAnge ord > ")))
    else :
        return
    meny2()

def pop3(ord):
    ord = ord.lower()
    try:
        Ord2.pop(ord)
        return "\"pop\""
    except:
        return "Ordet finns inte"
def Append3(ord,exp):
    ord = ord.lower()
    if ord in Ord2:
            print("Finns redan i listan")
            return
    #samma sak fast för dictonary metoden
    Ord2[ord]=exp
def lookup3(ord):
    return Explain(ord,Ord2[ord]) if ord in Ord2 else "Finns inte i listan"

def meny3():
    message = """
    Alternativ (ange nummret för alternativet)
    -------------------------------------------------------------------------
    1 : Lägg till nytt ord
    2 : Hitta ord
    3 : Ta bort ord
    4 : Tillbaka till toppen
    -------------------------------------------------------------------------
    Ange index > """
    #testar att läsa användarens input so ett heltal
    #misslyckas detta skrivs ett felmedelande och menyn startar om
    try:
        resp = int(input(message))
    except:
        print("Du måste ange en siffra\n")
        meny3()
        return
    #kollar vad användaren vill göra
    if(resp == 1):
        #Vill användaren lägga till ett nytt ord frågas den samme om ord och förklaring
        
        Append3(input("Vilket ord vill du lägga till\nAnge ord > ")
            ,input("Vad är förklaringen?\nAnge förklaring > "))
    elif resp == 2:
        print(lookup3(input("Vilket ord?\nAnge ord > ")))
    elif resp == 3:
        print(pop3(input("Vilket ord vill du ta bort?\nAnge ord > ")))
    else :
        return
    meny3()
    
        
def pingInt(message):
    inp = input(message)
    try:
        return int(inp)
    except:
        print("Du måste ange en siffra\n")
        pingInt(message)

if __name__ == "__main__":
    startping = """
    Vilken metod vill du använda?
    -------------------------------------------------------------------------
    1. två separata listor
    2. lista av tupler
    3. Dictionary
    allt annat avslutar programmet
    -------------------------------------------------------------------------
    Välj metod >"""
    
    Ord = ["Ord"]
    Exp = ["Förklaring"]
    Ord1 = [("Ord","Förklaring")]
    Ord2 = {
        "Ord" : "Förklaring"
    }
    while 1:
        mode = pingInt(startping)
        if(mode == 1):
            meny1()
        elif mode == 2:
            meny2()
        elif mode == 3:
            meny3()
        if(int(mode)>3):
            break
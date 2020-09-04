#En fin liten funktion som bara skriver ut förklaringen av ett ord
def Explain(ord,exp):
    #Skriver ut förklaringen på ett lite trevligare sätt
    return "Förklaring av {} > {}".format(ord,exp)



#region funktioner för två separata listor

#följande är funktionerna för fallet två separata listor
#Funktionen som tar bort en instans i listorna
def pop1(ord):
    #normaliserar strängen för att slippa skrivfel
    ord = ord.lower().strip(' ')
    try:
            #tar bort ordet och dess förklaring
            Exp.pop(Ord.index(ord))
            Ord.pop(Ord.index(ord))
            return "\"pop\""
    except:
            #finns inte ordet skrivs ett felmedelande ut
            return "Ordet finns inte"
#Funtkionen som lägger till ett nytt ord och en ny förklaring i listorna
def Append1(ord,exp):
    #normaliserar strängen för att slippa skrivfel
    ord = ord.lower().strip(' ')
    #kollar om ordet redan finns
    if ord in Ord:
            print("Finns redan i listan")
            return
    #Lägger till ett nytt ord i ordlistan
    Ord.append(ord)
    Exp.append(exp)
    #Lägger till en ny förklaring i förklarings listan
    
#funktionen som hittar ett ords förklaring i listan
def lookup1(ord):
    #normaliserar strängen för att slippa skrivfel
    ord = ord.lower().strip(' ')
    #om ordet finns i listan returneras dess förklaring annars returneras "finns inte i listan"
    return Explain(ord,Exp[Ord.index(ord)]) if ord in Ord else "Finns inte i listan"
#meny funktionen för två separata listor fallet
def meny1():
    #Huvud menyn för fallet separata listor
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
    resp = pingInt(message)
    #kollar vad användaren vill göra
    if(resp == 1):
        #Vill användaren lägga till ett nytt ord frågas den samme om ord och förklaring
        Append1(input("Vilket ord vill du lägga till\nAnge ord > ")
            ,input("Vad är förklaringen?\nAnge förklaring > "))
    elif resp == 2:
        #Vill användaren leta upp ett ord frågas den samme om vilket ord den vill hitta
        print(lookup1(input("Vilket ord?\nAnge ord > ")))
    elif resp == 3:
        #Vill am
        print(pop1(input("Vilket ord vill du ta bort?\nAnge ord > ")))
    else :
        return
    meny1()
#endregion
#region lista av tupler
#funktionen som tar bort en tupple ur listan
def pop2(ord):
    #normaliserar ordet för att slippa skrivfel
    ord = ord.lower().strip(' ')
    #letar efter ordet i listan, hittas det inte skrivs ett felmedelande ut
    for el in Ord1:
        if el[0] == ord :
            Ord1.pop(Ord1.index(el))
            return "\"pop\""
        return "Ordet finns inte"
#Funktionen som lägger till en ny tuppel i listan av tuppels
def Append2(ord,exp):
    #normaliserar ordet för att slippa skrivfel
    ord = ord.lower().strip(' ')
    #kollar om ordet redan finns i listan
    #nytjar lookup funktionen
    if lookup2(ord) != "Finns inte i listan":
        print("Finns redan i listan")
        return 
    #om ordet inte fanns i listan så läggs det till i listan
    Ord1.append((ord,exp))
#funktionen som kollar upp om ordet finns i listan
def lookup2(ord):
    #normaliserar ordet för att slippa skrivfel
    ord = ord.lower().strip(' ')
    for el in Ord1:
            if el[0] == ord :
                return Explain(ord,el[1])
    return "Finns inte i listan"
#funkar exakt lika dant som meny1 funktionen bara med andra index efter funktionenrna
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
    #ping int används för att jag skrev samma kod tre fyra gånger
    #ränkte att det blev mer läsbart att sätta den i en egen funktion
    resp = pingInt(message)
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
#endregion
#region dictionary
#funktionen som tar bort ett ord ut dict
def pop3(ord):
    #normaliserar ordet för att slippa skrivfel
    ord = ord.lower().strip(' ')
    try:
        #försöker ta bort ordet, funkar det inte finns inte ordet
        Ord2.pop(ord)
        return "\"pop\""
    except:
        return "Ordet finns inte"
#funktionen som lägger till ett nytt ord i dict
def Append3(ord,exp):
    #normaliserar ordet för att slippa skrivfel
    ord = ord.lower().strip(' ')
    #kollar om ordet redan finns i dict Ord2
    if ord in Ord2:
            print("Finns redan i listan")
            return
    #lägger till ett nytt värde i dict
    Ord2[ord]=exp
#funktionen som letar upp ett ord i dict
def lookup3(ord):
    #normaliserar ordet för att slippa skrivfel
    ord = ord.lower().strip(' ')
    #om ordet finns i listan returnerar den förklaringen annars returnerar den ett felmedelande
    return Explain(ord,Ord2[ord]) if ord in Ord2 else "Finns inte i listan"
#menyn för dict metoden funkar på precis samma vis som de förra bara annat index på funktionerna
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
    resp = pingInt(message)
    #kollar vad användaren vill göra
    if(resp == 1):
        #Vill användaren lägga till ett nytt ord frågas den samme om ord och förklaring
        
        Append3(input("Vilket ord vill du lägga till\nAnge ord > ")
            ,input("Vad är förklaringen?\nAnge förklaring > "))
    elif resp == 2:
        #frågar om ett ord att leta upp
        print(lookup3(input("Vilket ord?\nAnge ord > ")))
    elif resp == 3:
        #frågar om ett ord att ta bort
        print(pop3(input("Vilket ord vill du ta bort?\nAnge ord > ")))
    else :
        #om man angav ett värde > 3 så terminerar funktionen
        return
    #kallar på sig själv
    meny3()
#endregion
#en funktion som enbart används för att göra koden mer läsbar
#den frågar användaren om ett nummer
#anger användaren inte ett heltal så frågar den igen
#fram tills att användaren har angett ett heltal
def pingInt(message):
    try:
        return int(input(message))
    except:
        print("Du måste ange en siffra\n")
        return pingInt(message)
#huvudfunktionen
#initierar alla listor osv
if __name__ == "__main__":
    #medelandet som ska användas för att se vilken av metoderna användaren vill använda
    startping = """
    Vilken metod vill du använda?
    -------------------------------------------------------------------------
    1. två separata listor
    2. lista av tupler
    3. Dictionary
    allt annat avslutar programmet
    -------------------------------------------------------------------------
    Välj metod >"""
    #region listor för metoden två separata listor
    Ord = ["Ord"]
    Exp = ["Förklaring"]
    #endregion
    #listan av tuppler för metoden lista av tupler
    Ord1 = [("Ord","Förklaring")]
    #dictionary för dict metoden
    Ord2 = {
        "Ord" : "Förklaring"
    }
    #startar en loop
    #detta är enbart så att man kan testa alla olika metoder utan att starta om programmet
    while 1:
        #frågar användaren vilken metod de vill använda
        mode = pingInt(startping)
        if(mode == 1):
            meny1()
        elif mode == 2:
            meny2()
        elif mode == 3:
            meny3()
        #ger man inte en giltig metod terminerar funktionen
        if(int(mode)>3):
            break
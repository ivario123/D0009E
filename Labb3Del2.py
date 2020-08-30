
Ord = ["Ord"]
Exp = ["Förklaring"]
Ord1 = [["Ord","Förklaring"]]
Ord2 = {
    "Ord" : "Förklaring"
}
def add(ord,exp,metod):
    if(metod == 1):
        Ord.append(ord)
        Exp.append(exp)
    if metod == 2:
        Ord1.append([ord,exp])
    if metod == 3:
        Ord2[ord]=exp
def lookup(ord,metod):
    if(metod == 1):
        return Exp[Ord.index(ord)] if ord in Ord else "Finns inte i listan"
    if metod == 2:
        for el in Ord1:
            if el[0] == ord :
                return el[1]
        return "Finns inte i listan"

    if metod == 3:
        return Ord2[ord] if ord in Ord2 else "Finns inte i listan"
    return "felaktig metod"
    
def meny(metod):
    
    message = """
    Alternativ (ange nummret för alternativet)
    -------------------------------------------------------------------------
    1 : Lägg till nytt ord
    2 : Hitta ord
    3 : Tillbaka till toppen
    -------------------------------------------------------------------------
    """
    try:
        resp = int(input(message))
    except:
        print("Du måste ange en siffra\n")
        meny()
    if(resp == 1):
        add(input("Vilket ord vill du lägga till\n")
            ,input("Vad är förklaringen?\n"),metod)
    elif resp == 2:
        print(lookup(input("Vilket ord?\n"),metod))
    else :
        return
    meny(metod)
        
def pingInt(message):
    inp = input(message)
    try:
        return int(inp)
    except:
        print("Du måste ange en siffra\n")
        pingInt(message)
def init():
    mode = pingInt("Vilken metod vill du använda?\nDu kan välja mellan 1,2,3")
    meny(mode)
    init()
if __name__ == "__main__":
    init()
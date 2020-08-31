
Ord = ["Ord"]
Exp = ["Förklaring"]
Ord1 = [["Ord","Förklaring"]]
Ord2 = {
    "Ord" : "Förklaring"
}
def Explain(ord,exp):
    return "Förklaring av {} > {}".format(ord,exp)
def Pop(ord,metod):
    ord = ord.lower()
    if(metod == 1):
        try:
            Exp.pop(Ord.index(ord))
            Ord.pop(Ord.index(ord))
            return "\"pop\""
        except:
            return "Ordet finns inte"
    if metod == 2:
        for el in Ord1:
            if el[0] == ord :
                Ord1.pop(Ord1.index(el))
                return "\"pop\""
        return "Ordet finns inte"
    if metod == 3:
        try:
            Ord2.pop(ord)
            return "\"pop\""
        except:
            return "Ordet finns inte"
def Append(ord,exp,metod):
    ord = ord.lower()
    if(metod == 1):
        Ord.append(ord)
        Exp.append(exp)
    if metod == 2:
        Ord1.append([ord,exp])
    if metod == 3:
        Ord2[ord]=exp
def lookup(ord,metod):
    ord = ord.lower()
    if(metod == 1):
        return Explain(ord,Exp[Ord.index(ord)]) if ord in Ord else "Finns inte i listan"
    if metod == 2:
        for el in Ord1:
            if el[0] == ord :
                return Explain(ord,el[1])
        return "Finns inte i listan"

    if metod == 3:
        return Explain(ord,Ord2[ord]) if ord in Ord2 else "Finns inte i listan"
    return "felaktig metod"
    
def meny(metod):
    
    message = """
    Alternativ (ange nummret för alternativet)
    -------------------------------------------------------------------------
    1 : Lägg till nytt ord
    2 : Hitta ord
    3 : Ta bort ord
    4 : Tillbaka till toppen
    -------------------------------------------------------------------------
    Ange index > """
    try:
        resp = int(input(message))
    except:
        print("Du måste ange en siffra\n")
        meny()
    if(resp == 1):
        Append(input("Vilket ord vill du lägga till\nAnge ord > ")
            ,input("Vad är förklaringen?\nAnge förklaring > "),metod)
    elif resp == 2:
        print(lookup(input("Vilket ord?\nAnge ord > "),metod))
    elif resp == 3:
        print(Pop(input("Vilket ord vill du ta bort?\nAnge ord > "),metod))
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
    mode = pingInt("Vilken metod vill du använda?\nDu kan välja mellan 1,2,3\nVälj metod > ")
    if(int(mode)>3):
        return
    meny(mode)
    init()
if __name__ == "__main__":
    init()


#region användar klassen
class user:
    def __init__(self,name="Användarens namn",nick="Smeknamn",num="Telefonnummer"):
        #Namnet på användaren
        self.Name = name
        #Smeknamnet på användaren
        self.Nick = nick
        #Användarens telefonnummer
        self.Num = num
    #Så att jag slipper ha printen senare i koden
    def __repr__(self):
        #Om man vill printa objektet så får man
        return "{}'s elller om man vill {}'s nummer är : {}".format(self.Name,self.Nick,self.Num)
#endregion


#region List modifierings funktionerna
#------------------------------------------.....---------------------------------------
#Funktionen som lägger till ett element i listan
#Den tar input phonebook och args
#Args är värdena som ska läggas till
#Phonebook är teleboken
def add(args=[],Phonebook=[]):
    #dubbelkollar så att man gav rätt mängd argument
    assert len(args)==2
    #Kollar så att det inte finns någon med det namnet
    for el in Phonebook:
        #Om någon har samma namn så bryts funktionen
        if el.Name==args[0]:
            #Skriver ut ett felmedelande
            print('Det finns redan en användare med det namnet\n')
            return Phonebook
    #Lägger till en ny användare i listan
    Phonebook.append(user(args[0],args[0],args[1]))
    #ger tillbaka den modifierade listan
    return Phonebook

#------------------------------------------.....---------------------------------------
#Funktionen som letar efter en användare i listan
def lookup(args=[],Phonebook=[]):
    #Verifigerar att antalent argument stämmer
    assert len(args)==1
    #går igenom listan med användare 
    for el in Phonebook:
        #kollar om namnet eller smeknamnet för användaren stämmer överens med argumententet
        if el.Name == args[0] or el.Nick == args[0]:
            #Skriver ut elementet med hjälp av __repr__ i klassen
            print(el)
            #Returnerar listan
            return Phonebook
    #om det inte hittades en användare med det namnet så skrivs ett felmedelande ut
    print("Hittade inte den användaren")
    #Returnerar listan
    return Phonebook

#------------------------------------------.....---------------------------------------
#Funktionen som ändrar en avnändares smeknamn
def alias(args,Phonebook):
    #Verifigerar att antalent argument stämmer
    assert len(args)==2
    # Går igenom listan med användare
    for el in Phonebook:
        #om man hittar någon med samma namn
        if el.Name == args[0]:
            #ändrar man den användarens smeknamn
            Phonebook[Phonebook.index(el)].Nick = args[1]
            #Skickar tillbaka den nya listan
            return Phonebook
    #om man inte hittar någon skrivs ett felmedelande
    print("Den användaren finns inte")
    #Skickar tillbaka den gamla listan
    return Phonebook

#------------------------------------------.....---------------------------------------
#Funktionen som tar bort ett element ur listan
def pop(args,Phonebook):
    #Verifigerar att antalent argument stämmer
    assert len(args)==1
    #går igenom listan
    for el in Phonebook:
        #om man hittar något element med samma smeknamn eller namn som det angivna
        if el.Name == args[0] or el.Nick == args[0]:
            #tar bort det elementet
            Phonebook.pop(Phonebook.index(el))
            #printar ett lite roligt medelande, föreställ er ljudet
            print("\"pop\"")
            #Returnerar listan
            return Phonebook
    #om man inte hittar en användare med det namn/smeknamn printas ett medelande
    print( "Hittade inte den användaren",)
    #returnerar listan
    return Phonebook

#------------------------------------------.....---------------------------------------
#Funktionen som ändrar telefonnummer för en användare
def change(args,Phonebook):
    #Verifigerar att antalent argument stämmer
    assert len(args)==2
    #går igenom listan
    for el in Phonebook:
        #kollar om det finns någon användare med det användarnamnet/smeknamnet
        if el.Name == args[0] or el.Nick == args[0]:
            #ändrar nummret för användaren
            Phonebook[Phonebook.index(el)].Num = args[1]
            #Skriver ut infon om användaren så att man kan se det nya numret
            print(Phonebook[Phonebook.index(el)])
            #Returnerar listan
            return Phonebook
    #Hittade man inte användaren så skrivs ett felmedelande
    print( "Hittade inte den användaren",)
    #Returnerar listan
    return Phonebook
#------------------------------------------.....---------------------------------------
#Funktionen som sparar listan till en fil
#Arg är filnamnet och Phonebook är listan med användare
def save(arg="FileName",Phonebook=[]):
    #Öppnar filen med förlängningen ".Telfeonbok"
    f = open("{}.Telfeonbok".format(arg),"w")
    #Skapar en tom sträng som ska hålla informationen om objekten
    s = ""
    #Om listan inte är tom
    if Phonebook:
        #Går igenom listan
        for el in Phonebook:
            #Lägger till användarens data till strängen
            s = "{}{};{};{};\n".format(s,el.Num,el.Nick,el.Name)
    #Skriver datan i s till filen f
    f.write(s)
    #Stänger filen f
    f.close()
    #Skriver ut ett litet medelande
    print("Skrev data till : {}.Telfeonbok".format(arg))
    
#------------------------------------------.....---------------------------------------
#Funktionen som laddar data från en fil
def load(arg="Filename"):
    #Öppnar filen med filnamn arg och förlängdningen .Telefonbok
    f = open("{}.Telfeonbok".format(arg),"r")
    #Raderna i texten separeras ut till en lista
    rows = f.read().split('\n')
    #skapar en tom lista
    temp = []
    #går igenom raderna
    for row in rows:
        #om raden inte är tom
        if row:
            #delar upp raden i collumner
            cols = row.split(';')
            #lägger till en ny användare i listan
            temp.append(user(cols[2],cols[1],cols[0])) 
    #Skriver ut datan i listan
    print(temp)
    #Stänger filen
    f.close()
    #Returnerar filen
    return temp
    
#endregion
#region huvudfunktioner
#------------------------------------------.....---------------------------------------
#Funktionen jag skrev bara för att jag inte ville kopiera kod en massa gånger
#Den testar om man gav rätt antal argument eller inte då det är ett av få exceptions koden borde kunna ge
def TryTask(task,inp,expectedargs):
    try:
        #kör uppgiften med inputen
        p = task(inp[0],inp[1])
        #om det funkade returnerar vi returnen
        return p
    except:
        #Om det inte funkade så skriver vi ett fint litet felmedelande
        print("Du måste ange {} argment separerade med mellanrum".format(expectedargs),)
        #returnerar det som borde vara telefonboken
        return inp[1]
    
#Main funktionen
if __name__ == "__main__":
    #skapar en tom Telefonbok
    Phonebook = []
    #Loopar i all oändlighet
    while 1:
        #Läser in ny input och splitar den på mellanslag
        arg = input("Telebok > ").split()
        #Kollar vad commandot var
        if arg[0] == "add":
            #kallar på TryTask funktionen för att lägga till en ny användare
            Phonebook = TryTask(add,[arg[1:3],Phonebook],2)
        elif arg[0]=="lookup":
            #Same fast för att kolla upp en användare
            Phonebook = TryTask(lookup,[arg[1:2],Phonebook],1)
        elif arg[0]=="alias":
            #Same fast för att byta alias på användaren
            Phonebook = TryTask(alias,[arg[1:3],Phonebook],2)
        elif arg[0]=="change":
            #Same fast för att byta telefonnummer
            Phonebook = TryTask(change,[arg[1:3],Phonebook],2)
        elif arg[0]=="save":
            #om man inte angav två argument så skriver man bara datan till save
            if(len(arg)==2):
                #Skriver data till det valda filnamnet
                Phonebook = save(arg[1],Phonebook)
            else:
                #Skriver datan till save
                Phonebook = save("save",Phonebook)
        elif arg[0]=="load":
            #om man inte angav två argument så läser man data från save
            if(len(arg)==2):
                #Läser data från det valda filnamnet
                Phonebook = load(arg[1])
            else:
                #Läser data från save
                Phonebook = load("save")
        #Om man säger quit så avbryts programmet
        elif arg[0]=="quit":
            break
        #Tycker att pop är ett bättre argument så accepterar det också
        elif arg[0]=="remove" or arg[0]=="pop":
            #tar bort det valda elementet
            Phonebook = TryTask(pop,[arg[1:2],Phonebook],1)
        #skrev man fel så skriver den att man skrev fel
        else:
            print("Invalid request\n")
#endregion

class user:
    Name = ""
    Nick = ""
    Num = ""
    def __init__(self,name,nick,num):
        self.Name = name
        self.Nick = nick
        self.Num = num
    def __repr__(self):
        return self.num
    
        

def add(args,Phonebook):
    assert len(args)==2
    for el in Phonebook:
        if el.Name==args[0]:
            print('Det finns redan en användare med det namnet\n')
        if el.Nick==args[0]:
            print('Det finns redan en användare med det namnet\n')
            
    try:
        Phonebook.append(user(args[0],args[0],args[1]))
        return Phonebook
    except:
        print("Du gav inte tillräckligt många argument för\n lägga till en ny användare")
        return Phonebook
    
def lookup(args,Phonebook):
    assert len(args)==1
    for el in Phonebook:
        if el.Name == args[0] or el.Nick == args[0]:
            print("{}'s elller om man vill {}'s nummer är : {}".format(el.Name,el.Nick,el.Num))
            return Phonebook
    print("Hittade inte den användaren")
    return Phonebook
def alias(args,Phonebook):
    assert len(args)==2
    for el in Phonebook:
        if el.Name == args[0]:
            el.Nick = args[1]
            return Phonebook
    print("Den användaren finns inte")
    return Phonebook
def pop(args,Phonebook):
    assert len(args)==1
    for el in Phonebook:
        if el.Name == args[0] or el.Nick == args[0]:
            Phonebook.pop(Phonebook.index(el))
            print("\"pop\"")
            return Phonebook
    print( "Hittade inte den användaren",)
    return Phonebook
def TryTask(task,inp,expectedargs):
    try:
        p = task(inp[0],inp[1])
        return p
    except:
        print("Du måste ange {} argment separerade med mellanrum".format(expectedargs),)
        return inp[1]
def loop(Phonebook):
    arg = input("Telebok > ").split()
    if(arg[0] == "add"):
        Phonebook = TryTask(add,[arg[1:3],Phonebook],2)
    elif(arg[0]=="lookup"):
        Phonebook = TryTask(lookup,[arg[1:2],Phonebook],1)
    elif(arg[0]=="alias"):
        Phonebook = TryTask(alias,[arg[1:3],Phonebook],2)
    elif(arg[0]=="remove"):
        Phonebook = TryTask(pop,[arg[1:2],Phonebook],1)
    else:
        print("Invalid request\n")
    loop(Phonebook)

if __name__ == "__main__":
    Phonebook = []
    loop(Phonebook)
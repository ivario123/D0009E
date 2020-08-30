
class user:
    Name = ""
    Nick = ""
    Num = ""
    def __init__(self,name,nick,num):
        self.Name = name
        self.Nick = nick
        self.Num = num
    def __repr__(self):
        return num
    
        
Phonebook = []
def add(args):
    for el in Phonebook:
        if el.Name==args[0]:
            print('Det finns redan en användare med det namnet\n')
            return
    try:
        Phonebook.append(user(args[0],args[0],args[1]))
    except:
        print("Du gav inte tillräckligt många argument för\n lägga till en ny användare")
def lookup(args):
    for el in Phonebook:
        if el.Name == args[0] or el.Nick == args[0]:
            return el.Num
    return "Hittade inte den användaren"
def alias(args):
    for el in Phonebook:
        if el.Name == args[0]:
            el.Nick = args[1]
            return
    print("Den användaren finns inte")
def pop(args):
    for el in Phonebook:
        if el.Name == args[0] or el.Nick == args[0]:
            Phonebook.pop(Phonebook.index(el))
            print("\"pop\"")
            return
    return "Hittade inte den användaren"
def loop():
    arg = input("Telebok > ").split()
    if(arg[0] == "add"):
        add(arg[1:3])
    elif(arg[0]=="lookup"):
        print(lookup(arg[1:2]),)
    elif(arg[0]=="alias"):
        alias(arg[1:3])
    elif(arg[0]=="remove"):
        pop(arg[1:3])
    else:
        print("Invalid request\n")
    loop()

if __name__ == "__main__":
    loop()
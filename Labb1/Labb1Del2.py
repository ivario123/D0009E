# en syggare lösning ifall jag hade fått använda lambda
# kostnad = lambda P,r,a:print("Den totala kostnaden efter {}år är {}kr".format(a,P+(a+1)*P*r/2))
def kostnad(P,r,a):
    print("Den totala kostnaden efter {}år är {}kr".format(a,P+(a+1)*P*r/2))
#testar funktionen
kostnad(50000, 0.03, 10)
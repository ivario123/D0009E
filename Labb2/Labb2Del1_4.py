#Snyggare lösning om jag fick använda lambda
#bounce2 = lambda n: [print(*(range(n,0,-1)),sep="\n"),print(*(range(0,n+1)),sep="\n")]
#bounce 2 är den itterativa versionen av bounce
def bounce2(n):
    #går igenom alla värde mellan n och minus n
    for i in range(n,-n-1,-1):
        #skriver ut absolutbeloppet på i
        print(abs(i),)
#bounce är den rekursiva versionen av bounce
def bounce(n):
    print(n,)
    #terminerar om n == 0
    if(n==0): return
    #om n!=0 kallar den på bounce(n-1)
    bounce(n-1)
    #skriver ut n igen, detta gör att man får den fina bounce effekten
    print(n,)
    
#rekursiva metoden för tvärsumma
def tvarsumman(n):
    #om n är större än tio körs rekursionen igen
    if n>=10:
        return n//10+tvarsumman(n-(n//10)*10)
    else:
        #annars returneras n
        return n
#om det är okej att göra om n till en sträng
#en av de itterativa metoderna
def tvarsumman2(n):
    #gör om n till en sträng
    s = str(n)
    Sum = 0
    #lägger till varje bokstavs siffervärde till summan
    for x in s:
        Sum = Sum+int(x)
    return Sum
#om det inte är okej att göra om n till en sträng
def tvarsumman3(n):
    Sum = 0
    #loopar tills n är noll 
    while n != 0:
        #om n är mindre än tio returneras summan
        if n < 10:
            Sum = Sum+n
            n=n-n
        else:
            #annars gör jag typ samma sak som den rekursiva saken
            temp = n
            count = 0
            while temp > 10:
                temp = temp//10
                count = count + 1
            Sum = Sum+ temp
            #multiplicerar med tiopotensen för talet
            n -= (temp)*10**count
    #returnerar summan
    return Sum
#test funktioner      
print("Tvarsumma(32) = {}".format(tvarsumman3(32233)))
print("Tvarsumma2(32) = {}".format(tvarsumman2(32233)))
print("Bounce",)
bounce(1)
print("Bounce2",)
bounce2(1)
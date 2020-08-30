#Snyggare lösning om jag fick använda lambda
#bounce2 = lambda n: [print(*(range(n,0,-1)),sep="\n"),print(*(range(0,n+1)),sep="\n")]
def bounce2(n):
    for i in range(n,-n-1,-1):
        print(abs(i),)
def bounce(n):
    print(n,)
    if(n==0): return
    bounce(n-1)
    print(n,)
    
    
def tvarsumman(n):
    if n>10:
        return n//10+tvarsumman(n-(n//10)*10)
    else:
        return n
def tvarsumman2(n):
    s = str(n)
    sum = 0
    for x in s:
        sum = sum+int(x)
    return sum
       
#print("Tvarsumma(32) = {}".format(tvarsumman(32)))
#print("Tvarsumma2(32) = {}".format(tvarsumman2(32)))
#print("Bounce",)
#bounce(1)
#print("Bounce2",)
#bounce2(1)
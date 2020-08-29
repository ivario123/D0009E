bounce2 = lambda n: [print(*(range(n,0,-1)),sep="\n"),print(*(range(0,n+1)),sep="\n")]
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
    sum = 0
    for i in range(n//10+1,0,-1):
        
print("Tvarsumma 32 = {}".format(tvarsumman(32)))
print("Bounce",)
bounce(10)
print("Bounce2",)
bounce2(10)

def cheksort(a):
    tryy =4
    i=0
    while i< tryy :
        pw= input("enter your password")
        i+=1

        if pw == a :
            return print("cangrat you got the right answer")
    return print ("this is not the right answer")
a = "dragonball"
cheksort(a)
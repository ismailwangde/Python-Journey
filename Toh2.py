nom=0
def Toh(n,S,D,T):
    global nom
    if n == 0:
        return
    elif  n==1:
        print('move disk#',n,"from", S, "to", D)
        nom+=1
        return
    Toh(n-2,S,D,T)
    nom+=1
    print('move disc',n,'from', S, T)
    Toh(n-2, D, T, S)
    nom+=1
    print('move disc',n,'from', D, S)
    Toh(n-2,T,S,D)
    nom+=1
    print('move disc',n,'from', T, D)
    Toh(n-2, S, D, T)

n=int(input("Enter number of disks: "))
Toh(n,"source","destination","temp")
print("Number of Movements",nom)
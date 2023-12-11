def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1]%10 + fibs[-2]%10)
    #print(fibs)
    print(fibs) #fibs
n=int(input("enter no of fibnocci"))
fib_to(n)
class queue:
    c=0
    def __init__(self):
        self.first = None
        self.last = None
    class node:
        def __init__(self, x):
            self.x = x
            self.next = None
    def push(self, x):
        if self.last is None:
            self.first = self.node(x)
            self.last = self.first
        else:
            self.last.next = self.node(x)
            self.last = self.last.next
        self.c+=1
        return x
 
    def pop(self):
        if self.isEmpty() :
            return("is empty")
        else:
            to_return = self.first.x
            self.first = self.first.next
            self.c-=1
            return to_return

    def isEmpty(self):
        return self.first==None
    def ct(self) :
        return self.c
 
line = input("insert keys to push and '-' to pop ").split()
q=queue()
for word in line :
    if word=="-" :
           print("Element popped",q.pop())
    else :
           print("Element pushed",q.push(word))     
x=q.ct()
print("Number of elements left in queue are",x)
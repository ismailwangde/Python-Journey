class Stack:
    c=0
    def __init__(self):
        self.top = None
    class node:
        def __init__(self, x):
            self.x = x
            self.next = None
    def push(self, x):
        if self.top is None:
            self.top = self.node(x)
        else:
            new_node = self.node(x)
            new_node.next = self.top
            self.top = new_node
        self.c+=1
        return x
 
    def pop(self):
        if self.isEmpty() :
            return("is empty")
        else:
            to_return = self.top.x
            self.top = self.top.next
            self.c-=1
            return to_return

    def isEmpty(self):
        return self.top==None
    def ct(self) :
        return self.c
 
line = input("insert keys to push and '-' to pop ").split()
s=Stack()
for word in line :
    if word=="-" :
           print("Element popped",s.pop())
    else :
           print("Element pushed",s.push(word))     
x=s.ct()
print("Number of elements left in stack are",x)

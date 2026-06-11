class Stack:
    def __init__(self,limit=10):
        self.limit=limit
        self.stack=[]
        self.size_stack=0
    def ismpty(self):
        return self.size_stack==0
    def pop(self):
        if self.size_stack==0:
            return "stack mpty please push the item first!"
        else:
            x=self.stack.pop()
            self.size_stack-=1
            return x
    def push(self,value):
        if len(self.stack)==self.limit:
            return "stack overflow"
        else:
            self.stack.append(value)
            self.size_stack+=1
    def __str__(self):
        return " ".join([i for i in self.stack])
# def TADB(n):
#     q=Stack()
#     while n>0:
       
#        x=n%2
#        q.push(x)
#        n=n//2
#     b=" "
#     while not q.ismpty():
#          b=b+str(q.pop())
#     return b
# end=TADB(12)
# print(end)
q=Stack()
q.push("2")
q.push("12")
q.push("-9")
x=q.pop()
print(x)
print(q)

    

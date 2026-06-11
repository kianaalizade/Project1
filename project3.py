
class Stack:
    def __init__(self,limit=1000):
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
def revers_file(f1,f2):
    q=Stack()
    o_f=open(f1,"r")
    for item in o_f:
        x=item.strip("\n")
        q.push(x)
    o_f.close()
    o1_f1=open(f2,"w")
    
    while not q.ismpty():
        y=q.pop()
        o1_f1.write(y + '\n')
    
    o1_f1.close()
    
revers_file(r"C:\Users\naya\Desktop\revers.txt","end1.html")
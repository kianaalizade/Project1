# postfix to to prefix with stack

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
   
def f(i,a,b):
    if i=="+":
        return "a+b"
    elif i=="-":
        return "b-a"
    elif i=="*":
        return "a*b"
    else:
        return "b/a"
def convert(ptoin):
    
    q=Stack()
    for i in ptoin:
        if i.isalpha():
            q.push(i)
        else:
            a=q.pop()
            b=q.pop()
            x=f(i,b,a)
            q.push(x)
    return q.stack
e=convert("ab+c/d")
print(e)

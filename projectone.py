# Generator in python
k=int(input("please enter a number:"))

def one(k):
     _list1=[ i for i in range(k+1)]
     for item in _list1:
          yield item**2

end=one(k)
for value in end:
     print(value)
    


     

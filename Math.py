import math
test=int(input("enter a number:"))
test1=int(input("and enter another number please:"))
def py_math(value1,value2):
    a=math.ceil(value1/value2)
    b=math.floor(value1/value2)
    c=math.pow(value1,3)
    d=math.sqrt(value2)
    e=math.fmod(value1,value2)
    f=math.log(value1)
    print("for",value1," and",value2,"=","ceil: ",a," ","floor: ",b," ","pow 2 for ",value2,":"," ",c," ","sqrt",value2,":",d," ","fmod: ",e," ","log ",value1,":",f)
py_math(test,test1)

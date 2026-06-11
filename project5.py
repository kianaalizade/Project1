#  TOWERHANOI
def h(t,a,b,c):
    if t==1:
        print(t,"move a to c")
        return
    h(t-1,a,c,b)
    print("move",t," a to c")
    h(t-1,b,a,c)
h(3,"A","B","C")
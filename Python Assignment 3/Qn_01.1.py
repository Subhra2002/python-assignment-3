l = [10,20,30,40]
a = l[0]

def myreduce(a):
    return a
 
def add(a,b):
    return a+b

for i in range(1,len(l)):
    b = l[i]
    a = add(a,b)

print(myreduce(a,l))




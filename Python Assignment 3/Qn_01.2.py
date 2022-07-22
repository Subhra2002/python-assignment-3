l =  [34,56,25,67,89,90,103,408]
b =[]

def myfilter():
    for i in l:
        # print(i)
        if i%2==0:
            b.append(i)

    print(b)

myfilter()
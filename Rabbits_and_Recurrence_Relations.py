def Rabbits_and_Recurrence_Relations(n,k):
    i=0
    j=1
    for iter in range(n-1):
        l=j+i*k 
        i=j
        j=l
    return j
print(Rabbits_and_Recurrence_Relations(30,3))


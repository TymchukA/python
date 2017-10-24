import collections
days = []
def appending(ai,bi,N):
    n=N-ai
    n=n//bi
    for i in range(0,n+1):
        days.append(ai+i*bi)
    return days

def weekend(N):
    d_minus=[]
    n=N//6
    k=N//7
    for i in range(0,n):
        d_minus.append(6+i*7)
    for i in range(0,k):
        d_minus.append(7+i*7)
    return d_minus    

N = int(input("Set amount of days in year,N(1<N<1000000)..."))
K = int(input("Set amount of political parties,K(1<K<100)..."))
for i in range(0,K):
    ai = int(input("Set the first day of strike,ai(1<ai<N)..."))
    bi = int(input("Set how often strikes are repeated,bi(1<bi<N)..."))
    appending(ai,bi,N)
duplicate = [item for item, count in collections.Counter(days).items() if count > 1]
minus=weekend(N)
result = list(set(duplicate) - set(minus))
if result :
    result.sort()
    print ("Numbers of days of national strikes are")
    print (result)
else:
    print("There are no days with strikes")

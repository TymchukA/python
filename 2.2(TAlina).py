import math 
def calc(x,k):
    if k == 0:
        return 1
    elif k == 1:
        return x
    else:
        return x*calc(x,k-1)+x**2*calc(x,k-2)/math.factorial(2*k)

x, n = int(input("input x: ")), int(input("input n: "))
y = []
for i in range(0,n+1):
    y.append(int(input("input element: ")))
sum = 0
for i in range(0,n+1):
    sum += ((-y[i])**i) * calc(x,i)

print(sum)

n=eval(input('Numarul este '))
s=0
for n2 in range(0, n+1):
    if ((n2%3==0)) and (n2%5==0):
        s+=n2
print(s)
a=input()

for j in range(a):

    n=input()
    p = 2
    while (p*p <= n):      
        if (n % p == 0): 
            n //= p
        else: 
            p += 2 if p>2 else 1  

    print n


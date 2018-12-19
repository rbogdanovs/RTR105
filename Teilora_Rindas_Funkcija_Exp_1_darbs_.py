'''
#_*_ coding: utf-8 -*-
from math import exp

def mans_exp(x):
    k = 0
    a = (-1)**k*x**(2*k)/(1)
    S = a
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 500:
        k = k + 1
        R = -1*x**2/k
        a = a * R
        S = S + a
        if  k > 498:
            print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
        elif k == 500:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))



    print("Izdruka no liet.f. Beigas!")
    return S

x = float(input("Lietotāj, lūdzu ievadi skaitli argumentu (x): "))
y = exp(-x*x)
print("standarta funkcija (%.2f) = %6.2f"%(x,y))

yy = mans_exp(x)
print("mans exp (%.2f = %6.2f"%(x,yy))


'''
#_*_ coding: utf-8 -*-
from math import exp

def mans_exp(x):
    k = 0
    a = (-1)**k*x**(2*k)/(1)
    S = a
    print("a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 500:
        k = k + 1
        R = -1*x**2/k
        a = a * R
        S = S + a
        if  k == 499:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
        elif k == 500:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
    
    
    return S

print("exp(-x*x) aprekinasana: ")
x = float(input("Lietotāj, lūdzu ievadi skaitli argumentu (x): "))
y = exp(-x*x)
print("exp(-x*x) (%.2f) = %6.2f"%(x,y))

yy = mans_exp(x)
print("exp(-x*x) (%.2f) caur summu: %6.2f"%(x,yy))
                                                           

print(" ")
print("                1000                              ")
print("               ______                             ")
print("               \               k      2*k         ")
print("                \          (-1)   * x             ")
print("     exp(-x*x) = >        _________________       ")
print("                /                                 ")
print("               /_____           k!                ")
print("                 k=0                              ")
print("                                                  ")
print("                                                  ")
print("                                             2    ")
print("                                    (-1) * x      ")
print("     Rekurences reizinatajs:      ______________  ")
print("                                                  ")
print("                                         k        ")


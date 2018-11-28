# 1. N vienmērīgi sadalīti gadījuma skaitļi
# https://www.letonika.lv ; https://www.terminilza.lv
# N uniformly distributed random number

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

import numpy
#print(numpy.random.__doc__)
#print(numpy.random.uniform.__doc__)

a = 0
b = 5
N = 10000

#(pseido)gadījumu skaitļu ģeneratora "grauds"
#numpy.random.seed(1)

x = numpy.random.uniform(a,b,N)
#x = numpy.random.normal(a,b,N)
'''
k = [0, 0, 0, 0, 0]
for i in range(N):
    if x[i] < 1:
        k[0] = k[0] + 1
    elif x[i] < 2:
        k[1] = k[1] + 1
    elif x[i] < 3:
        k[2] = k[2] + 1
    elif x[i] < 4:
        k[3] = k[3] + 1
    else:
        k[4] = k[4] + 1

print(k)
print(sum(k))
'''

y = numpy.random.uniform(a,b,N)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
#plt.plot(x, y, 'ko')
N1 = 0
for i in range(N):
    if y[i] < x[i]:
      plt.plot(x[i], y[i], 'go')
      N1 = N1 + 1
    else:
        plt.plot(x[i], y[i], 'ro')
#print(N1)
S_zinaamais = (b-a) * (b-a)
S_nezinaamais = 1. * S_zinaamais * N1 /N
print(S_nezinaamais)

plt.show()




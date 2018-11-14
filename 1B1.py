import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
# Importē skaitlisko metožu bibliotēkas funkcijas
x = linspace(0, 4, 70)
# Trešais arguments ir ģenerējamo elementu skaits
y = cos(x)
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$cos(x)$')
plt.plot(x, y)
plt.show()
#citi zīmēšanas piemēri
#https://matplotlib.org/gallery/index.html
'''
Krāsu pieraksta kā vienu no metodesplot parametriem. Piemēram:
plt.plot(x, y, color = "#RRGGBB"), kur
•RR– sarkano krāsas daudzumu raksturojošais skaitlis robežās no 0 līdz 255
sedecimāla pierakstā.  Piemēram: 00 – krāsas nav,7F
– vidēja krāsas intensitāte, FF– vislielākā krāsas
intensitāte. Svarīgs ir simbolu skaits - 6 gabali (simbolu # neskaitot).
•GG– zaļo krāsas daudzumu raksturojošais sedecimāls skaitlis.
•BB– zilo krāsas daudzumu raksturojošais sedecimāls skaitlis.
'''




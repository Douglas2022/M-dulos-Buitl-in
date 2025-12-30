from collections import Counter,namedtuple,deque
from operator import itemgetter

# 1- Lista de frutas e quero realizar a contagem
fruits = ["Banana","Maçã","Perâ","Uva","Salada-mista","Graviola","Banana",
          "Perâ","Uva","Salada-mista","Graviola","Banana","Banana","Maçã","Perâ","Uva",
          "Salada-mista","Graviola","Banana",
          ]
print(fruits)
print(Counter(fruits))

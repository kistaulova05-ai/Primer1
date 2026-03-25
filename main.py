#делала с Николаевым
import os
my_secret1=os.environ['S1_Nikolaev']
print(my_secret1)

import os
my_secret2=os.environ['S2_Nikolaev']
print(my_secret2)

import os
my_secret3=os.environ['S3_Nikolaev']
print(my_secret3)


# #1-ый способ
# from sympy import *

# k, T, C, L = symbols('k C T L')

# C_ost = 100000
# Am_lst = []
# C_ost_lst = []
# for i in range(5):
#     Am = (C - L) / T
#     C_ost -= Am.subs({C: 100000, T: 5, L: 0})
#     Am_lst.append(round(Am.subs({C: 100000, T: 5, L: 0}), 2))
#     C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2-ой способ
# Aj = 0
# C_ost = 100000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(5):
#     Am = k * 1 / T * (C - Aj)
#     C_ost -= Am.subs({C: 100000, T: 5, k: 2})
#     Am_lst_2.append(round(Am.subs({C: 100000, T: 5, k: 2}), 2))
#     Aj += Am
#     C_ost_lst_2.append(round(C_ost, 2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# #1-ый способ (пункт 3 общего задания)
# from sympy import *

# k, T, C, L = symbols('k C T L')

# C_ost_3 = 30000
# Am_lst_3 = []
# C_ost_lst_3 = []
# for i in range(8):
#     Am = (C - L) / T
#     C_ost_3 -= Am.subs({C: 30000, T: 8, L: 0})
#     Am_lst_3.append(round(Am.subs({C: 30000, T: 8, L: 0}), 2))
#     C_ost_lst_3.append(round(C_ost_3, 2))
# print('Am_lst_3:', Am_lst_3)
# print('C_ost_lst_3:', C_ost_lst_3)

# #2-ой способ (пункт 3 общего задания)
# Aj = 0
# C_ost_3 = 30000
# Am_lst_2_3 = []
# C_ost_lst_2_3 = []
# for i in range(8):
#     Am = k * 1 / T * (C - Aj)
#     C_ost_3 -= Am.subs({C: 30000, T: 8, k: 2})
#     Am_lst_2_3.append(round(Am.subs({C: 30000, T: 8, k: 2}), 2))
#     Aj += Am
#     C_ost_lst_2_3.append(round(C_ost_3, 2))
# print('Am_lst_2_3:', Am_lst_2_3)
# print('C_ost_lst_2_3:', C_ost_lst_2_3)
# #Таблица
# import pandas as pd

# Y = range(1, 9)
# table1 = list(zip(Y, C_ost_lst_3, Am_lst_3))
# table2 = list(zip(Y, C_ost_lst_2_3, Am_lst_2_3))
# tframe = pd.DataFrame(table1, columns=['Y', 'C_ost_lst_3', 'Am_lst_3'])
# tframe2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2_3', 'Am_lst_2_3'])
# print(tframe)
# print(tframe2)

# #Визуализация
# import numpy as np
# import matplotlib.pyplot as plt

# plt.plot(tframe['Y'], tframe['C_ost_lst_3'], label='Am')
# plt.savefig('chart1.png')
# plt.figure()
# plt.plot(tframe2['Y'], tframe2['C_ost_lst_2_3'], label='Am_2')
# plt.savefig('chart2.png')

# #Круговая диаграмма (данные от 1-го способа)
# vals = Am_lst_3
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#        labels=labels,
#        autopct='%1.1f%%',
#        shadow=True,
#        explode=explode,
#        wedgeprops={
#            'lw': 1,
#            'ls': '--',
#            'edgecolor': "k"
#        },
#        rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart3.png')

# #Круговая диаграмма (данные от 2-го способа)
# vals = Am_lst_2_3
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#        labels=labels,
#        autopct='%1.1f%%',
#        shadow=True,
#        explode=explode,
#        wedgeprops={
#            'lw': 1,
#            'ls': '--',
#            'edgecolor': "k"
#        },
#        rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart4.png')

# #Гистограмма (пункт 3 общего задания)
# table1 = list(zip(Y, Am_lst_3))
# table2 = list(zip(Y, Am_lst_2_3))
# tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst_3'])
# tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2_3'])

# plt.figure()
# plt.bar(tframe['Y'], tframe['Am_lst_3'])
# plt.savefig('chart5.png')

# plt.figure()
# plt.bar(tframe2['Y'], tframe2['Am_lst_2_3'])
# plt.savefig('chart6.png')

#Задание 2 (делала одна, вариант 1)
from sympy import *

k, T, C, L = symbols('k C T L')

C_ost_4 = 15000
Am_lst_4 = []
C_ost_lst_4 = []
for i in range(8):
    Am = (C - L) / T
    C_ost_4 -= Am.subs({C: 15000, T: 8, L: 0})
    Am_lst_4.append(round(Am.subs({C: 15000, T: 8, L: 0}), 2))
    C_ost_lst_4.append(round(C_ost_4, 2))
print('Am_lst_4:', Am_lst_4)
print('C_ost_lst_4:', C_ost_lst_4)

#2-ой способ (индивидуальное задание)
Aj = 0
C_ost_4 = 15000
Am_lst_2_4 = []
C_ost_lst_2_4 = []
for i in range(8):
    Am = k * 1 / T * (C - Aj)
    C_ost_4 -= Am.subs({C: 15000, T: 8, k: 2})
    Am_lst_2_4.append(round(Am.subs({C: 15000, T: 8, k: 2}), 2))
    Aj += Am
    C_ost_lst_2_4.append(round(C_ost_4, 2))
print('Am_lst_2_4:', Am_lst_2_4)
print('C_ost_lst_2_4:', C_ost_lst_2_4)

#Таблица (индивидуальное задание)
import pandas as pd

Y = range(1, 9)
table1 = list(zip(Y, C_ost_lst_4, Am_lst_4))
table2 = list(zip(Y, C_ost_lst_2_4, Am_lst_2_4))
tframe = pd.DataFrame(table1, columns=['Y', 'C_ost_lst_4', 'Am_lst_4'])
tframe2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2_4', 'Am_lst_2_4'])
print(tframe)
print(tframe2)

#Визуализация (индивидуальное задание)
import numpy as np
import matplotlib.pyplot as plt

plt.figure() #что значит? Создает фигуру - ответила Журавлева
plt.plot(tframe['Y'], tframe['C_ost_lst_4'], label='Am')
plt.savefig('chart7.png')
plt.figure()
plt.plot(tframe2['Y'], tframe2['C_ost_lst_2_4'], label='Am_2')
plt.savefig('chart8.png')

#Круговая диаграмма (индивидуальное задание)
vals = Am_lst_4
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1)
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       shadow=True,
       explode=explode,
       wedgeprops={
           'lw': 1,
           'ls': '--',
           'edgecolor': "k"
       },
       rotatelabels=True)
ax.axis("equal")
plt.savefig('chart9.png') #Что значит? Сохраняет график в файл - ответила Журавлева

#Круговая диаграмма (данные от 2-го способа)
vals = Am_lst_2_4
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1)
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       shadow=True,
       explode=explode,
       wedgeprops={
           'lw': 1,
           'ls': '--',
           'edgecolor': "k"
       },
       rotatelabels=True)
ax.axis("equal")
plt.savefig('chart10.png')

#Гистограмма (индивидуальное задание)
table1 = list(zip(Y, Am_lst_4))
table2 = list(zip(Y, Am_lst_2_4))
tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst_4'])
tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2_4'])

plt.figure()
plt.bar(tframe['Y'], tframe['Am_lst_4'])#что значит? Строит график- ответила Журавлева 
plt.savefig('chart11.png')

plt.figure()
plt.bar(tframe2['Y'], tframe2['Am_lst_2_4'])
plt.savefig('chart12.png')

#Все корректно, ставлю оценку 5, проверила Журавлева 
#Ответы на вопросы верны, у Журавлевой оценка 5

#Первое задание
import os
S1_kistaulova = os.environ ['S1_kistaulova']
print(S1_kistaulova)


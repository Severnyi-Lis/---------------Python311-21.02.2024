#повторял то что делали  на уроке
vr=input('Какой сейчас год? ')
from datetime import datetime 
from datetime import timedelta 

dt= datetime.now()  # текущий момент времени 
print(dt.strftime("%Y"))#текущий год

tr= input('А какой месяц?')
print(dt.strftime('%m'))#текущий месяц

#Узнал как сделать календарь на год
lr=input('Питон,давай сюда календарь на текущий год ')
import calendar
calendar.prcal(2024)#prcal-используется для печати календаря на целый год

print('А любой месяц любого другого года?')
year=int(input('Укажите год'))
mth=int(input('Укажите месяц'))
print(calendar.month(year,mth))#month - принимает месяц и год









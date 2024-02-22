#Создал календарь с условиями,чтобы потренировать while
import calendar
from datetime import datetime
r=input('Укажите год')
l=input('Укажите месяц')
r=int(r)
l=int(l)
while r== 1995 and r ==1:
    ttt=input('Это год моего Рождения!')
while r> datetime.now().year:
   ttt=input('Вы в будущем!Вернитесь в настоящее!')
   if r>datetime.now().year:
       r=input('Укажите год')
       l=input('Укажите месяц')
       r=int(r)
       l=int(l)
if r<= 1901:
 print('Добро пожаловать в 20 ый век!')
print(calendar.month(r,l))   

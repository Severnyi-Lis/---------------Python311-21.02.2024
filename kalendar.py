#Игрался с модулем calendar
#Задача- Спросить месяц и год
#Вывести "календарь"
import calendar
r=int(input('Укажите год'))#Знаю что так лучше не писать ,не бейте меня 
l=int(input('Укажите месяц'))
print(calendar.month(r,l))#Узнал что нельзя записать (r,l,m,a)!

#тут написал как учили,чтобы не побили 
r=input('Укажите год')
l=input('Укажите месяц')
r=int(r)
l=int(l)
print(calendar.month(r,l))
  



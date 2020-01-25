 #1 задание
x = 2
y = 5
print('Переменная 1 = x ','Переменная 2 = y')

x= int(input('Введите число '))
y = str(input('Введите текст '))
print(x,y)

#2 задание
sec = int(input('Введите секунды, а я переведу  их в часы и минуты '))
#while sec < 86400 :
minuts = sec // 60
hours = (minuts // 60)
minuts1 = sec // 60 - hours*60
sec_new = sec - hours*60*60 - minuts1*60
print("Время " "{:.0f}".format(hours),"часа :" ,
        "{:.0f}".format(minuts1),"минуты" ,
        "{:.0f}".format(sec_new)," секунд" )

#3 задание
n = input('Введите число')
x = int(n)
n1 = n+n
n2 = n+n+n
x1 = int(n1)
x2 = int(n2)
print(x+x1+x2)

#4 задание
x = int(input("Введите число "))
maxim = 0
while x > 0 :
    y = x%10
    if y > maxim:
        maxim = y
    x = x // 10
print('Самое большое значение', maxim)

#5 задание
earn = int(input('Введите выручку '))
loss = int(input('Введите расходы '))
x = earn - loss
y = x/earn * 100
if loss  > earn:
    print('У Вас все плохо')
else: print('Хорошие показатели')
print('Прибыльность бизнеса',y,'%')
num = int(input('А сколько сотруднков в компани '))
prof = x / num
print('Каждый сотрудник приносит',prof,'у.е')

#6 Задание
l = int(input('Сколько сегодня вы пробежали '))
l_top = int(input('Сколько хотите пробегать '))
day = 1
while l < l_top :
    l = l * 1.1
    day = day + 1
    #print(l , day)
print( 'На',day,'вы достигните результата')
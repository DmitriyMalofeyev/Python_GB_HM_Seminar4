# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

#Считаем число ПИ по формуле в зависимости от необхоимой точности после запятой, 
def Pi(k):
    k8=8*k
    pi = 1/(16**k) * (4/(k8+1) - 2/(k8+4) - 1/(k8+5) - 1/(k8+6))
    if k: pi+=Pi(k-1)
    return pi

# Выводим ПИ с указанным количеством знаков после запятой
def dotPi(n):
    if n==1:
        tochno=Pi(n)*10//1/10
    else:
        tochno=Pi(n)*(10**n)//1/(10**n)
    print(tochno)

# СБОРКА

N = int(input("Введите количество знаков (от 1)\nпосле запятой для числа ПИ -> ") or 0)
while  N<=0:
    N = int(input('Число должно быть больше 0 -> ') or 0)


dotPi(N)
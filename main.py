# start
# Завдання 1.
#
# Написати рекурсивну функцію знаходження ступеня числа.
def step_num(number,stepen):
    if stepen==1:
        return number
    if stepen ==0:
        return 1
    return number * step_num(number,stepen-1)
try:
    number=int(input("enter a number"))
    stepen=int(input("enter a stepen of number"))
    print(step_num(number,stepen))
except Exception as error:
    print(error)


#num=2 step=3
#step_num(2,3) => 2 * step_num(2,2) =8
#step_num(2,2) => 2 * step_num(2,1) =4
#step_num(2,1) => if stepen==1 =>return 2
# Завдання 2.
#
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
#
# Проілюструйте роботу функції прикладом. (Протестувати)
def count_of_stars(n):
    if n>0:
        print("*")
    elif n==0:
        return " "
    return count_of_stars(n-1)
try:
    n=int(input("enter a count of stars"))
    print(count_of_stars(n))
except Exception as e:
    print("error")
#count_of_stars(3)
#count_of_stars(3)=>print"*"=>count_of_stars(2)
#count_of_stars(2)=>print"*"=>count_of_stars(1)
#count_of_stars(1)=>print"*"=>count_of_stars(0)
#count_of_stars(0)=>elif n==0 =>return " "
# Завдання 3.
#
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
#
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.

def count_num(a:int,b:int):


    if a>b:
        return 0
    return a+count_num(a+1,b)
try:
    a=int(input("enter a first number of range"))
    b=int(input("enter a last number of range"))

    print(count_num(a,b))
except Exception as e:
    print("error")
#count_num(2,4)
#2 +
# count_num(3,4) +3 =>
# count_num(4,4) +4 =>
# count_num(5,4) if 5>4 return 0
#lab №5(Cycles construction and interation algorithms. Cycle while)int = int(input("Введите 2ую границу диапозона: ")
#The main task(Try ro Guess the number)

#Authors Dubodelov A.V. and Lebed A.S.
#Version v.1.0.0
#Group 10701118
#Date 01/10/2018

import string
import random
def game():
    guess = int(input("Введите число от 1 до 100: "))
    tries = 0
    while guess <= 100 and guess >= 1:
        tries += 1
        border_1 = 1
        border_2 = 100
        number = random.randint (border_1, border_2)
        if number > guess:
            print("Компьютер взял больше, чем нужно было: ", number)
            border_1 = guess
            guess = random.randint(border_1,border_2)
        elif number < guess:
            print("Компьютер взял меньше, чем нужно было: ", number)
            border_2 = guess
            guess = random.randint(border_1,border_2)
        elif number == guess:
            print("Компьютер отгадал число ", number, "за ", tries, "попытку(-ок).")
            break
    else:
        print("Ввержите верное число из промежутка!")
        game()
while True:
    choice = int(input(" Введите 1 , чтобы начать игру;\n Введите 2, чтобы закончить игру.\n"))
    if choice == 1:
        game()
    elif choice == 2:
        print("До скорой встречи.")
        input("Нажмите Enter , чтобы закончить сеанс.")
        break
    else:
        print("Неверный пункт меню.")




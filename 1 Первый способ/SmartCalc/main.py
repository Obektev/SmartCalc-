# Основной задачей было показать, на что способны веб-интерфейсы, поэтому над логикой здесь я не очень запаривался,
# и основную работу делает функция eval()
import eel
from math import *
from win32api import GetSystemMetrics

# Переменные/константы
miss_list = ['+', '-', '/', '√', '*'] # Символы, которые могут быть оставлены по ошибке в конце строки


@eel.expose
def equals(input, is_radian_active):

    print(input, is_radian_active) # Тестовый вывод input

    # Переменные/константы
    output = ''
    brackets = 0
    previous_sym = ''
    trigonometry = 0

    # Защита от "дурака"
    if '/0' in input: # Избежание деления на ноль
        return 'Деление на ноль???'

    if input[-2] in miss_list: # Избежание лишнего символа на конце строки
        input = input[0:-2]


    # Замена символов мат. операций на функции из python math
    input = input.replace('²','**2') # Замена второй степени
    input = input.replace('π',"pi")  # Замена π символа 
    if not is_radian_active: # Если режим радиан отключен, градусы переводим в радианы
        input = input.replace('cos(',"cos(pi/180*")
        input = input.replace('sin(',"sin(pi/180*")
        input = input.replace('tan(',"tan(pi/180*")

    for i in input:
        if i=='🔜':
            if brackets>0:
                output+=')'*brackets
            break
        if i=='√':
            if previous_sym.isnumeric():    
                output += '*'
            output += 'sqrt('
            brackets += 1
            continue
        if brackets > 0 and not(i<='9' and i>='0' or (i=='i' and previous_sym!='s') or i==')'):
            brackets -= 1
            output += ')' + i
            continue

        # Реализация умножения тригонометрических выражений без *
        if previous_sym.isnumeric() and (i == 's' or i == 'c' or i == 't' or i == 'e' or i=='p'):
            output += '*'

        output += i # Добавление текущего символа из input в output
        previous_sym = i # Изменение предыдущего символа на текущий

    try:
        print(output) # Тестовый вывод output
        return str(round(eval(output), 9)) # возвращение решённого выражения, с округлением к 10 * 10^-9 
                                      # для избежания проблемы c 0.5000000000000001
    except:
        return 'Что-то не так ' + input[0:-1] # В случае ошибки, возвращается это сообщение


@eel.expose
def change_config(URL):
    open("web\config.txt", "w").write(URL)

def start_program(URL):
    eel.init("web") # Инициализация папки с вёрсткой
    eel.start(f"{URL}", # Старт окна
            size=(420, 720),
            port=8000)

def main():
    start_program(open("web\config.txt", "rt").read())

if __name__ == "__main__":
    main()


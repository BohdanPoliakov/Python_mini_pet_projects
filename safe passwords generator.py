import sys
from random import randint, choice, shuffle


def yes_or_not(answer):   # Функция проверяющая, что пользователь ввел ДА или НЕТ
    while True:

        if answer == 'да':
            answer = True
            return answer
        elif answer == 'нет':
            answer = False
            return answer
        else:
            answer = input('Пожалуйста дайте ответ в формате: да или нет: ')
            print()


def numbers(numb):     # Функция проверяющая, что пользователь ввел цифру
    while not numb.isdigit():
        numb = input('Пожалуйста дайте ответ целой цифрой: ')
    numb = int(numb)
    return numb


def generator(num):    # Функция генерирующая хитрый список, на основе которого будет сгенерирован пароль
    generat_list = []
    remainder = num
    for i in range(count):
        if remainder == 0:
            break
        if i == count - 1:
            rand_num = remainder
        else:
            rand_num = randint(1, min(remainder - (count - i - 1), length - len(generat_list)))
        remainder -= rand_num
        generat_list.append(rand_num)

    return generat_list


def pass_generator(r_list):  # Функция генерации пароля на основе хитрого списка из generator(num)
    flag = False
    password = []
    r_list_count = r_list
    if exclusion:
        for _ in range(len(r_list)):
            if abs_UP:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(abs_clear_UP_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if abs_down:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(abs_clear_down_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if digits:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(digits_clear_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if symbols:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(symbols_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break
    else:
        for _ in range(len(r_list)):
            if abs_UP:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(abs_UP_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if abs_down:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(abs_down_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if digits:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(digits_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if symbols:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(symbols_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break
    shuffle(password)
    return password


# ИНИЦИАЛИЗАЦИЯ ЛИСТОВ И ПЕРЕМЕННЫХ
digits_case = '0123456789'
digits_clear_case = '23456789'
abs_UP_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abs_clear_UP_case = 'ABCDEFGHJKMNPQRSTUVWXYZ'
abs_down_case = 'abcdefghijklmnopqrstuvwxyz'
abs_clear_down_case = 'abcdefghjkmnpqrstuvwxyz'
symbols_case = '!#$%&*+-=?@^_'
count = 0
case_count = 0

# ОСВНОВНЫЕ ПРИНТЫ, ВВОДЫ, ИСКЛЮЧЕНИЯ
print('Привет. Моя программа поможет тебе сгенерировать пароль.')
print()
how = input('Напиши цифрой, сколько паролей тебе требуется сгенерировать: ').strip()
how = numbers(how)

abs_UP = input('''Скажите, должен ли Ваш пароль включать заглавные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ) ?
Ответ дайте в формате: да или нет: ''').lower().strip()
abs_UP = yes_or_not(abs_UP)
if abs_UP:
    case_count += 1

abs_down = input('''Скажите, должен ли Ваш пароль включать строчные  буквы (abcdefghijklmnopqrstuvwxyz) ?
Ответ дайте в формате: да или нет: ''').lower().strip()
abs_down = yes_or_not(abs_down)
if abs_down:
    case_count += 1

digits = input('''Скажите, должен ли Ваш пароль включать цифры (0123456789) ?
Ответ дайте в формате: да или нет: ''').lower().strip()
digits = yes_or_not(digits)
if digits:
    case_count += 1

symbols = input('''Скажите, должен ли Ваш пароль включать символы (!#$%&*+-=?@^_) ?
Ответ дайте в формате: да или нет: ''').lower().strip()
symbols = yes_or_not(symbols)
if symbols:
    case_count += 1

count = len([abs_UP_case, abs_down_case, digits_case, symbols_case][:case_count])
if count == 0:
    print('Ты не выбрал не одного модификатора. Следовательно, пароль будет пустым. Посему, дальнейшая работа программы не имеет смысла.')
    print('Попробуйте начать заново, выбрав хотя бы один модификатор')
    sys.exit()

exclusion = input('''Исключать ли неоднозначные символы (il1Lo0O) ?
Ответ дайте в формате: да или нет: ''').lower().strip()
exclusion = yes_or_not(exclusion)

length = input('Ок. А теперь, давай определимся с максимальной длинной пароля. Задай это значение цифрой: ')
length = numbers(length)
while True:
    if length < case_count:
        length = input('Максимальная длина пароля не может быть меньше минимального количества модификаторов, которые вы выбрали. Пожалуйста, повторите ввод: ')
        length = numbers(length)
    else:
        break
if length:
    count += 1

for i in range(how):    # Основной цикл генератора паролей

    random_list = generator(length)

    print(*pass_generator(random_list), sep='')

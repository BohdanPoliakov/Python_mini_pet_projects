import random

print('Приветствую в моей числовой угадайке!')

def is_valid(s, border):
    return s.isdigit() and 1 <= int(s) <= border

new_game = 'да'
while new_game == 'да':
    print('Какое максимальное число мы можем загадать?')
    border = int(input())
    y = random.randint(1, border)
    attempts = 0
    print('Я загадал число, угадывай)')
    while True:
        num = input()
        if is_valid(num, border):
            num = int(num)
            attempts += 1
            if y < num:
                print('Ваше число больше загаданного, попробуй еще раз.')
            elif y > num:
                print('Ваше число меньше загаданного, попробуй еще раз.')
            else:
                print('Вы угадали, мои поздравления!')
                print(f'Кол-во потраченных попыток: {attempts}')
                break
        else:
            print(f'А может стоит ввести целое число от 1 до {border}?')
    print('Если хотели бы сыграть еще раз напишите "да", если нет - любое другое сообщение.')
    new_game = input()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

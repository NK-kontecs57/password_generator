from random import *
length = int(input('(^__^) Введите длину пароля:'))
count_pass = int(input('Введите количество паролей:'))
ans_digits = int(input('Цифры(1 - "да", 2 - "нет"):'))
ans_l = int(input('Буквы с нижним регистром:'))
ans_up = int(input('Буквы с верхним регистром:'))
ans_pun = int(input('Символы:'))
def generate_password():
    char = ''
    gen_password = []
    if ans_digits == 1:
        gen_password.append(choice('0123456789'))
        char += '0123456789'
    if ans_l == 1:
        gen_password.append(choice('abcdefghijklmnopqrstuvwxyz'))
        char += 'abcdefghijklmnopqrstuvwxyz'
    if ans_up == 1:
        gen_password.append(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        char += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if ans_pun == 1:
        gen_password.append(choice('!# $%&*+-=?@^_'))
        char += '!#$%&*+-=?@^_'
    while len(gen_password) != length:
        gen_password.append(choice(char))
    shuffle(gen_password)
    print('Ваш пароль: ', *gen_password, sep='',)
for i in range(count_pass):
    generate_password()
# import libs
from random import choice
import passgencfg


# print intro
print('~'*3, 'PASSGEN', '~'*3)


try:
    password_length = int(input('password length: '))
except ValueError:
    print('error. password length must be an integer.')
except:
    print('error.')

password_symbols_pull = ''.join([
    passgencfg.numbers if passgencfg.include_numbers else '',
    passgencfg.letters if passgencfg.include_letters else '',
    passgencfg.capital_letters if passgencfg.include_capital_letters else '',
    passgencfg.special_chars if passgencfg.include_special_chars else ''
])

if not password_symbols_pull:
    print('error. no symbols selected in passgencfg.py')
else:
    password = ''.join([choice(password_symbols_pull)
                       for _ in range(password_length)])
    print(password, '\n')

# import libs
from random import randint
from rich.console import Console
import passgencfg

# print intro
console = Console()
console.print('~ PASSGEN ~', style='bold red')

try:
    password_length = int(input('password length: '))
except ValueError:
    print('error. password length must be an integer.')

password_symbols_pull = str()

if passgencfg.include_numbers:
    password_symbols_pull += passgencfg.numbers
if passgencfg.include_letters:
    password_symbols_pull += passgencfg.letters
if passgencfg.include_capital_letters:
    password_symbols_pull += passgencfg.capital_letters
if passgencfg.include_special_chars:
    password_symbols_pull += passgencfg.special_chars

password = str()

try:
    for i in range(password_length):
        symbol = password_symbols_pull[randint(
            0, len(password_symbols_pull)-1)]
        password += symbol
except ValueError:
    print('error. no symbols selected in passgencfg.py')
except:
    print('error.')

print(password)

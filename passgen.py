# import libs
from random import randint
from rich.console import Console
import passgencfg

#
console = Console()
console.print('~ passgen ~', style='bold red')

password_length = int(input('password length: '))

password_symbols_pull = str()

if passgencfg.include_digits:
    password_symbols_pull += passgencfg.digits
if passgencfg.include_letters:
    password_symbols_pull += passgencfg.letters
if passgencfg.include_capital_letters:
    password_symbols_pull += passgencfg.capital_letters
if passgencfg.include_special_chars:
    password_symbols_pull += passgencfg.special_chars

password = str()
# for symbol in password_symbols_pull:
#     password = password_symbols_pull[randint(0, len(password_symbols_pull) - 1)]

print(password_symbols_pull.split(''))

print(password)

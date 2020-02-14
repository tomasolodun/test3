from enum import Enum


class converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


while True:
    while True:
        try:
            x = float(input('amount of money:'))
            p = int(input('currency:'))
            break
        except ValueError or NameError:
            print('it must be digits')
    if p == converter.USD.value:
        print(x * 24.3)
    elif p == converter.EUR.value:
        print(x * 26.6)
    elif p == converter.CZK.value:
        print(x * 1.1)
    elif p == converter.PLN.value:
        print(x * 6.3)
    else:
        print('Would you try again? Write yes or no')
        answer = input('')
        if answer == 'yes':
            continue
        else:
            break

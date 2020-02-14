while True:
    while True:
        try:
            d, m, y = int(input('day:')), \
                      int(input('mounth:')), \
                      int(input('year:'))
        except ValueError or NameError:
            print("It must be digits")
            if 1<=m<=12:
                if m==2:
                    if 1<=d<28:
                        print(f'{d+1}/{m}/{y}')
                    elif d==28:
                        print(f'01/{m+1}/{y}')
                    else:
                        print('Error2')
                elif m==4 or m==6 or m==9 or m==11:
                    if 1<=d<30:
                        print(f'{d+1}/{m}/{y}')
                    elif d==30:
                        print(f'01/{m+1}/{y}')
                    else:
                        print('Error3')
                else:
                    if 1<=d<31:
                       print(f'{d+1}/{m}/{y}')
                    elif d==31:
                       print(f'1/{m+1}/{y}')
                    else:
                       print('Error4')
            else:
                print('Error1')

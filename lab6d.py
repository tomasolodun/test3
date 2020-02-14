while True:
    while True:
        try:
            t = int(input("Введіть хв:"))
            break
        except ValueError:
            print("it must be digits: ")

    while t > 6:
        t -= 6
        t = t % 10
        if t <= 3:
            print("green")
        elif t == 4:
            print("yellow")
        else:
            print("red")

    print('Would you try again? Write yes or no')
    answer = input('')
    if answer == 'yes':
        continue
    else:
        break

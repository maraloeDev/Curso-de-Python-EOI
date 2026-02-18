print("Start café menu program... Press q to exit")
cafe_menu = {'Ice coffee' : 3000}

while True:
    input_str = input('$ ')
    if input_str.startswith('q'):
        break

    command = input_str[0]

    if command == '<':
        input_str = input_str.replace('<', "")
        parts = input_str.split(':')
        if len(parts) < 2:
            print('input error')
            continue
        else:
            cafe_menu[parts[0].strip()] = parts[1].strip()

    elif command == '>':
        input_str = input_str.replace('>', "")
        item_name = input_str.strip() #El strip es como el trim() en Java, quita los espacios
        if item_name in cafe_menu:
            print(cafe_menu[item_name])
        else:
            print('{} not in the menu.'.format(item_name))

    elif command == 'q':
        break
    else:
        print('input error.')

print("exiting cafe menu program.")
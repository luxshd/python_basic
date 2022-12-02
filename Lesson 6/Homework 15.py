days_text = ['дней', 'день', 'дня']
time_values = dict.fromkeys(['days', 'hours', 'minutes', 'seconds'], None)
dd_text = ''
user_input = int(input('Введите число в диапазоне от 0 до 8639999: '))

while not 0 <= user_input <= 8639999:
    print('Введённое число вне допустимого диапазона.')
    user_input = int(input('Повторите ввод: '))
else:
    x, time_values['seconds'] = divmod(user_input, 60)
    x, time_values['minutes'] = divmod(x, 60)
    time_values['days'], time_values['hours'] = divmod(x, 24)

    for key, value in time_values.items():
        if key != 'days':
            time_values[key] = str(value).zfill(2)
    dd = time_values['days']
    hh = time_values['hours']
    mm = time_values['minutes']
    ss = time_values['seconds']

    if dd > 20 and dd % 10 == 1:
        dd_text = days_text[1]
    elif dd > 20 and 1 < dd % 10 < 5:
        dd_text = days_text[2]
    elif dd > 10:
        dd_text = days_text[0]
    elif dd % 10 == 1:
        dd_text = days_text[1]
    elif 1 < dd % 10 < 5:
        dd_text = days_text[2]
    else:
        dd_text = days_text[0]

    print(f'{user_input} -> {dd} {dd_text}, {hh}:{mm}:{ss}')
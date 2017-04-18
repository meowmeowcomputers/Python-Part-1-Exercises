while True:
    try:
        tempC = int(input('What\'s the temperatire in Celsius?' ))
        tempF = tempC * 1.8 + 32
        print('It\'s {} degrees Fahrenheit'.format(tempF))
        break
    except ValueError:
        print('Enter a valid number')

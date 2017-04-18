bill = int(input('Please enter the total bill: '))
while True:
    service = str(input('How was the service? (good, fair, or bad)? '))
    if str.lower(service) == 'good':
        bill = bill * 1.2
    elif str.lower(service) == 'fair':
        bill = bill * 1.15
    elif str.lower(service) == 'bad':
        bill = bill * 1.1
    else:
        print('Please put in a proper service evaluation')
    print('The bill is ', str(bill))
    break

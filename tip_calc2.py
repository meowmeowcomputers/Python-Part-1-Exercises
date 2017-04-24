def main():
    bill = int(input('Please enter the total bill: '))
    while True:
        try:
            service = str(input('How was the service? (good, fair, or bad)? '))
            people = int(input('Split how many ways? '))
            if str.lower(service) == 'good':
                bill = bill * 1.2
            elif str.lower(service) == 'fair':
                bill = bill * 1.15
            elif str.lower(service) == 'bad':
                bill = bill * 1.1
            else:
                print('Please put in a proper service evaluation')
            print('The bill is ', str(bill/people), ' per person')
            break
        except ValueError:
            print("Enter a valid number")

if __name__ == '__main__':
    main()

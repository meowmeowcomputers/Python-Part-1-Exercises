def main():
    day = int(input('Day (0-6)? '))
    daystr = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day <= 4:
        print('It\'s ', daystr[day], ', go to work')
    else:
        print('It\'s ', daystr[day], ', sleep in')

if __name__ == '__main__':
    main()

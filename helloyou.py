def main():
    name = input('WHAT\'S YOUR FIRST NAME? ')
    print('HELLO, ' + name + '!')
    countchar = len(name)
    print('DANG, YOU HAVE ' + str(countchar) + ' LETTERS IN THAT NAME')

if __name__ == '__main__':
    main()

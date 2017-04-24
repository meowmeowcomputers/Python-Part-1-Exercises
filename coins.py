def main():
    coinQ = ""
    coin = 0
    while True:
        print('You have ', str(coin), 'coins')
        coinQ = str(input("Do you want another coin? "))
        if str.lower(coinQ) == 'yes':
            coin += 1
        elif str.lower(coinQ) == 'no':
            print('Bye!')
            break
        else:
            print('Please input \"yes\" or \"no\"!')

if __name__ == '__main__':
    main()

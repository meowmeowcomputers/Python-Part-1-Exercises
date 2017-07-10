import count1to10, coins, hello, helloyou, madlibs, workorsleep, dayofweek, temp, tip_calc, tip_calc2

options = {
#    0: guess.main,
    1: hello.main,
    2: helloyou.main,
    3: madlibs.main,
    4: dayofweek.main,
    5: workorsleep.main,
    6: temp.main,
    7: tip_calc.main,
    8: tip_calc2.main,
    9: count1to10.main,
    10: coins.main,
    11: quit
    }


def exSelect():
    while True:
        try:
            exercise = int(input('Which exercise would you like to see? (Enter 1-10)\n Ex 1: Hello, you! (print name)\n Ex 2: HELLO YOU!(print name in CAPS)\n Ex 3: Madlibs\n Ex 4: Day of the Week\n Ex 5: Work or Sleep In?\n Ex 6: Celsius to Fahrenheit\n Ex 7: Tip Calculator\n Ex 8: Tip Calculator with Divided Check\n Ex 9: 1 to 10\n Ex 10: How many coins?\n Enter 11: Quit\n'))
            options[exercise]()
        except ValueError:
            print('\n**********************\n*Enter a valid number*\n**********************\n\n\n\n')


exSelect()

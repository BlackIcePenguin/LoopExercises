#1
def name_loop():
    list = range(0, 10)
    for num in list:
        print("Jack Bonney")
    print('Done')


name_loop()


#2
def red_gold_loop():
    list = range(0, 20)
    for num in list:
        print('Red')
        print('Gold')


red_gold_loop()


#3
def even_for():
    list = range(0, 100)
    for num in list:
        if num % 2 == 0:
            print(num)
        else:
            continue


even_for()


#4
def even_while():
    count = 0
    list = range(0, 100)
    while count < 101:

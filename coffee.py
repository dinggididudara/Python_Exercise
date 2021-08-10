
coffee_price = 0
while True: #first letter is capital

    print('''
        Coffee machine
            -menu-

        1: Americano     $2
        2: Latte         $3.5
        3: Hot Chocolate $3
    ================================''')


    order = input("Choose your coffee: ")

    if order == 1:
        coffee_price = 2
    elif order == 2:
        coffee_price = 3.5
    elif order ==3:
        coffee_price = 3

    cups = input("how many cups? : ")
    total_price = coffee_price * cups

    received = int(input(f"total price is {total_price } dollar. >>"))

    if received >= total_price:
        change = received - total_price
        print(f"Your change will be {change}")
    else:
        print("Not enough. please try again")
else:
    print("False?")

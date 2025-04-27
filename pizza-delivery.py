# Variables
def prices():
    print('The Prices:\n--Sizes of Pizza:--\nSmall Pizza $15\nMedium Pizza $20\nLarge Pizza $25\n\n--Additional--\nKetchup $1\nExtra Cheese $5\n')
print(prices())
def menu():
    size_of_pizza = input('What Size pizza do you want?: S,M or L: ')
    ketchup = input('Do you want ketchup? [Y/n] ')
    extra_cheese = input('Do you want Extra Pizza for your Pizza?: [Y/n] ')
    bill = 0


    if ketchup.lower() == 'y':
        bill += 1
    if extra_cheese.lower() == 'y':
        bill += 5
    if size_of_pizza.lower() == 's':
        bill += 15
        print('The Small Pizza Is $15 dollars')
    elif size_of_pizza.lower() == 'm':
        bill += 20
        print('The Medium Pizza is $20 dollars')
    elif size_of_pizza.lower() == 'l':
        bill += 25
        print('The Large Pizza Is $25')
    else:
        print('The Option is not Founded!')
        print(menu())
    print(f'Your Bill is ${bill} dollars')
    print('\n\n')
    form_of_payment = input("What's the form of payment PIX,Debit or Credit?: ")
    if form_of_payment.lower() == 'pix':
        print('The Pix is:\n\nType of Pix: 🔗 CNPJ: 31.511.227/0001-25')
        print(f"The value is ${bill}")
    elif form_of_payment.lower() == 'credit':
        print("Complete with your informations of your Credit Card 🪪:")
        n_card = input('Number of the Credit Card: ')
        cvv = input('CVV of the Credit Card: ')
        validated_card = input("What's the validated of the Credit Card: ")
    elif form_of_payment.lower() == 'debit':
        print("Complete with your informations of your Debit Card 🪪:")
        n_card = input('Number of the Debit Card: ')
        cvv = input('CVV of the Debit Card: ')
        validated_card = input("What's the validated of the Debit Card: ")
    else:
        print(f"The option \"{form_of_payment}\" isn't founded!")
        print(menu())
print(menu())
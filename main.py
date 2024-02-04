MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report(dic):
    for key in dic:
        print(f'{key}: {dic[key]}')


def out_of_resources(choice):
    if 'milk' in MENU[choice]:
        if resources['water'] < MENU[choice]['ingredients']['water'] or resources['milk'] < MENU[choice]['ingredients']['milk'] or resources['coffee'] < MENU[choice]['ingredients']['coffee']:
            return True
    else:
        if resources['water'] < MENU[choice]['ingredients']['water'] or resources['coffee'] < MENU[choice]['ingredients']['coffee']:
            return True

    return False


def manage_res(choice):
    if 'milk' in MENU[choice]:
        resources['milk'] -= MENU[choice]['ingredients']['milk']
        resources['water'] -= MENU[choice]['ingredients']['water']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[choice]['ingredients']['water']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']


def show_report(res):
    print('\nResources Available in Machine:')
    for key in res:
        print(f'{key}: {res[key]}')
    print('\n')


run = True
while run:

    choice = input('What would you like to have?(espresso/latte/cappuccino): ').lower()

    if choice == 'report':
        show_report(resources)
    elif choice == 'off':
        run = False
        print('Machine is Turned OFF')
    elif choice == 'latte' or choice == 'espresso' or choice == 'cappuccino':
        if out_of_resources(choice):
            print('Sorry! machine is out of resources')
        else:
            penny = float(input('Enter number of coins: ')) * 0.01
            nickel = float(input('Enter number of coins: ')) * 0.05
            dime = float(input('Enter number of coins: ')) * 0.10
            quarter = float(input('Enter number of coins: ')) * 0.25

            total_amount = round(penny + nickel + dime + quarter, 2)

            if total_amount > MENU[choice]['cost']:
                change = round(total_amount - MENU[choice]['cost'], 2)
                print(f'Here\'s your change {change}. Enjoy your {choice}')
                manage_res(choice)
                show_report(resources)
            elif total_amount == MENU[choice]['cost']:
                print(f'Enjoy your {choice}')
                manage_res(choice)
                show_report(resources)
            else:
                print('Given amount is not sufficient. Here\' your refund.')

    else:
        print(f'Sorry we don\'t have {choice}.  Choose from the given options.')

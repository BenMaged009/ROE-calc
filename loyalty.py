def greet(user_name):
    print('hello there', user_name, 'welcome to the ROE calculater app!')

def cop_points():
    cop_days = ['1-gathering day', '2-building day', '3-reserch day', '4-hero day', '5-training day']
    for cop_day in cop_days:
        print(cop_day)
    user_option = input('enter cop day: ')
    while user_option not in ('1', '2', '3', '4', '5'):
        print('wrong input, write your option correctly.')
        user_option = input('enter cop day: ')
#GATHERING DAY
    if user_option == '1' or user_option == 'gathering day':
        rss_list = ['wood', 'food', 'iron', 'marble']
        for rss in rss_list:
            print(rss)
        rss_type = input('enter resources type: ')
        while rss_type not in (rss_list):
            print('wrong input, write your option correctly.')
            rss_type = input('enter resources type: ')
        if rss_type == 'wood':
            amount = int(input('enter the amount: '))
            total = amount * 2 * 6
            print('total points = ', total)
        elif rss_type == 'food':
            amount = int(input('enter the amount: '))
            total = amount * 2 * 6
            print('total points = ', total)
        elif rss_type == 'marble':
            amount = int(input('enter the amount: '))
            total = amount * 3 * 6
            print('total points = ', total)
        elif rss_type == 'iron':
            amount = int(input('enter the amount: '))
            total = amount * 4 * 6
            print('total points = ', total)


#BUILDING DAY

    elif user_option == '2' or user_option == 'building day':
        amount = int(input('enter the amount: '))
        total = amount * 1000 * 6
        print('total poinst = ', total)

#RESERCH DAY

    elif user_option == '3' or user_option == 'reserch day':
        amount = int(input('enter the amount: '))
        total = amount * 400 * 6
        print('total points = ', total)

#HERO DAY

    elif user_option == '4' or user_option == 'hero day':
        print('still under development!')
        pass

#TRAINING DAY

    elif user_option == '5' or user_option == 'training day':
        print('Troops tiers: ')
        troops_tier = ['t10', 't9', 't8', 't7', 't6']
        print(troops_tier)
        tier_type = input("enter troops tier: ")
        while tier_type not in (troops_tier):
            print('wrong input, write your option correctly.')
            tier_type = input('enter troops tier: ')
        if tier_type == 't10':
            amount = int(input('enter amount of troops trained per round: '))
            print(amount * 400 * 6)
        elif tier_type == 't9':
            amount = int(input('enter amount of troops trained per round: '))
            print(amount * 300 * 6)
        elif tier_type == 't8':
            amount = int(input('enter amount of troops trained per round: '))
            print(amount * 250 * 6)
        elif tier_type == 't7':
            amount = int(input('enter amount of troops trained per round: '))
            print(amount * 200 * 6)

def hourly_challenges():
    print('coming soon, stay toned(;')
    pass

def main():
    options_list = ['1- COP points', '2- hourly challenges']
    for option in options_list:
        print(option)
    user_option = input('enter your option: ')
    while user_option not in ('1', '2', 'COP', 'hourly'):
        user_option = input('enter your option: ')
    if user_option == '1' or user_option == 'COP' or user_option == 'cop':
        cop_points()
    elif user_option == '2' or user_option == 'hourly':
        hourly_challenges()

def calculate_something_else_option():
    global calc_again
    calc_again = input('do you wanna calculate something else? y = yes n = no \n')
    while calc_again not in ('Y', 'N', 'n', 'y'):
        calc_again = input('do you wanna calculate something else? y = yes n = no \n')
    if calc_again == 'Y' or calc_again == 'y':
        main()
    elif calc_again == 'N' or calc_again == 'n':
        print('come back soon(:')
        exit()


user_name = input('enter your name: ')
greet(user_name)


main()

calculate_something_else_option()

print('thanks for using the app!')

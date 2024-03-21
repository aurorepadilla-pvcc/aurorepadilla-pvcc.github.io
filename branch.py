# Name: Aurore Padilla
# Prog Purpose: This program finds the coost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############## define global variables ##############
# define tax rate, service fee, and prices
SALES_TAX_RATE = .062
SERVICE_FEE = .10
ADULT_MEAL = 19.95
KID_MEAL = 11.95



# define global variables
num_adult_meals = 0
num_kid_meals = 0
adult_meals_cost = 0
kids_meals_cost = 0
subtotal = 0
service_fee = 0
sales_tax = 0
total = 0


############## define program functions ##############
def main ():
    more_meals = True
    
    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno.lower() == "n" or yesno == "N":
            more_meals = False
            print("Thank you for your order. Enjoy your meals!")


def get_user_data():
    global num_adult_meals, num_kid_meals
    num_adult_meals = int(input("Enter the number of adults in the party: "))
    num_kid_meals = int(input("Enter the number of children in the party: "))


def perform_calculations():
    global subtotal, service_fee, sales_tax, total
    adult_meals_cost = (num_adult_meals * ADULT_MEAL)
    kids_meals_cost = (num_kid_meals * KID_MEAL)
    subtotal = (num_adult_meals * ADULT_MEAL) + (num_kid_meals * KID_MEAL)
    service_fee = subtotal * SERVICE_FEE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax


def display_results():
    print("-------------------------------")
    print('**** Branch Barbeque Buffet****')
    print("-------------------------------")
    print('Adult Meals      $ ' + format(adult_meals_cost, '8,.2f'))
    print('Kids Meals       $ ' + format(kids_meals_cost
                                         , '8,.2f'))
    print('subtotal         $ ' + format(subtotal, '8,.2f'))
    print('service_fee      $ ' + format(service_fee, '8,.2f'))
    print('sales_tax        $ ' + format(sales_tax, '8,.2f'))
    print("-------------------------------")
    print('total            $ ' + format(total, '8,.2f'))
    print("-------------------------------\n")
    print(str(datetime.datetime.now()))

########## call on main program to execute #########
main()


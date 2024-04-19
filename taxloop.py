# Name: Aurore Padilla
# Program Purpose: This program loops and siplays personal property tax for vehicles in Charlottesville.
#
# Personal property tax:
#    -- Personal property tax rate: 4.20% per year
#    -- Personal property is paid every six months
# Personal Property Tax Relief (PPTR)
#    -- Eligibility: Owned or leased vehicles which are predominately used for non-business purposes & have
#       passenger license plates. (These vehicles do not have to pay a license fee.)
#    -- Tax relief for qualified vehicles is 33%

import datetime

########## define global variables ##########
PERSONAL_PROPERTY_TAX_RATE = 0.042 #4.20% annual rate
TAX_RELIEF_RATE = 0.33 #33% tax relief

############# define program functions ##########

def main():
    while True:
        try:
            assessed_value = float(input("\nWhat is the assessed value of the vehicles? $"))
            eligible_for_relief = input("Eligible for tax relief (Y/N)? ").strip().upper()

            if eligible_for_relief not in ['Y', 'N']:
                    print("Invalid input. Please enter 'Y' or 'N'.")
                    continue

            annual_tax_amount, six_month_tax_amount, relief_amount, total_due = perform_calculations(assessed_value, eligible_for_relief)

            display_results(assessed_value, annual_tax_amount, relief_amount, total_due)
            
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            isncontinue
    

        continue_response = input("\nCalculate another vehicle's tax (Y/N)? ").strip().upper()
        if continue_response != 'Y':
            break
            
def perform_calculations(assessed_value, eligible_for_relief):
    annual_tax_amount = assessed_value * PERSONAL_PROPERTY_TAX_RATE
    six_month_tax_amount = annual_tax_amount / 2

    if eligible_for_relief == 'Y':
        relief_amount = six_month_tax_amount * TAX_RELIEF_RATE
    else:
        relief_amount = 0

    total_due = six_month_tax_amount - relief_amount
    return annual_tax_amount, six_month_tax_amount,relief_amount, total_due


def display_results(assessed_value, annual_tax_amount, relief_amount, total_due):
    print("\nPersonal Property Tax Bill")
    print("----------------------------")
    print(f'Assessed value of the vehicle:         $ {assessed_value:,.2f}')
    print(f'Full annual amount owed:               $ {annual_tax_amount:,.2f}')
    print(f'Relief amount:                         $ {relief_amount:,.2f}')
    print(f'Total due for the next six months:     $ {total_due:,.2f}')
    print("----------------------------")
    print(datetime.datetime.now().strftime("%Y-%m-%d"))
 
############ call on main program to execute #########

main()
    

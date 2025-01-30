def main():

    try:
        income = float(input("Enter your total income this year: "))

        owed_taxes = 0

        if income >= 0 and income <= 11600:
            owed_taxes = income * 0.1
        elif income >= 11601 and income <= 47150:
            owed_taxes = income * 0.12
        elif income >= 47150 and income <= 100525:
            owed_taxes = income * 0.22
        elif income >= 100526 and income <= 191950:
            owed_taxes = income * 0.24
        elif income >= 191951 and income <= 243725:
            owed_taxes = income * 0.32
        elif income >= 243726 and income <= 609350:
            owed_taxes = income * 0.35
        elif income >= 609351:
            owed_taxes = income * 0.37
            
        round(owed_taxes, 2)

        print(f'You owe ${owed_taxes:.2f} this year.')

    except:
        print('Value Error')

main()
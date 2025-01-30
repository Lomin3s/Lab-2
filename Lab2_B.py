def main():

    try:
        income = float(input("Enter your total income this year: "))

        owed_taxes = 0


        if income >= 0:
            if income <= 11600:
                owed_taxes = income * 0.10
            elif income > 11600:
                income2 = 11600
                owed_taxes += income2 * 0.10
                income -= (income2)
                if income > 0 and income < 35550:
                    owed_taxes += income * 0.12
                elif income >= 35550:
                    income2 = 35550
                    owed_taxes += income2 * 0.12
                    income -= (income2)
                    if income > 0 and income < 53375:
                        owed_taxes += income * 0.22
                    elif income >= 53375:
                        income2 = 53375
                        owed_taxes += income2 * 0.22
                        income -= (income2)
                        if income > 0 and income < 91425:
                            owed_taxes += income * 0.24
                        elif income >= 91425:
                            income2 = 91425
                            owed_taxes += income2 * 0.24
                            income -= (income2)
                            if income > 0 and income < 51775:
                                owed_taxes += income * 0.32
                            elif income >= 51775:
                                income2 = 51775
                                owed_taxes += income2 * 0.32
                                income -= (income2)
                                if income > 2 and income < 365625:
                                    owed_taxes += income * 0.35
                                elif income >= 365625:
                                    income2 = 365625
                                    owed_taxes += income2 * 0.35
                                    income -= (income2)
                                    if income >=0:
                                        owed_taxes += income * 0.37


        round(owed_taxes, 2)


        print(f'You owe ${owed_taxes:.2f} this year.')

    except:
        print('Something went wrong.')

main()
def main():

    try:

        unit1 = str(input("Enter the unit you are converting from: "))
        unit2 = str(input("Enter the unit you are converting to: "))
        temp1 = float(input(f'Enter the temperature in {unit1}: '))

        temp2 = 0

        if unit1 == 'Fahrenheit':

            if unit2 == 'Celsius':
                temp2 = (temp1 -32) * 5/9
            if unit2 == 'Kelvin':
                temp2 = (temp1 - 32) * 5/9 + 273.15
            if unit2 == 'Fahrenheit':
                temp2 = (temp1 * 1.0)

        if unit1 == 'Celsius':

            if unit2 == 'Fahrenheit':
                temp2 = (temp1 * 9/5) + 32
            if unit2 == 'Kelvin':
                temp2 = (temp1 + 273.15)
            if unit2 == 'Celsius':
                temp2 = (temp1 * 1.0)

        if unit1 == 'Kelvin':
            if unit2 == 'Celsius':
                temp2 = (temp1 - 273.15)
            if unit2 == 'Fahrenheit':
                temp2 = (temp1 - 273.15) * 9/5 + 32
            if unit2 == 'Kelvin ':
                temp2 = (temp1 * 1.0)

        round(temp2, 1)

        print(f'That is {temp2:.1f} degrees {unit2}.')

    except:
        print('Something went wrong')

main()
def main():

    try:
        side1 = float(input("Side length 1:  "))
        side2 = float(input("Side length 2:  "))
        side3 = float(input("Side length 3:  "))

        if side1 == side2 and side1 > 0 and side2 > 0 and side3 > 0:
            if side1 == side3:
                print("This is an equilateral triangle!")
            else:
                print("This is an isosceles triangle!")



        if side1 != side2 and side1 > 0 and side2 > 0 and side3 > 0:
            if side1 == side3:
                print("This is an isosceles triangle!")
            elif side1 != side3:
                print("This is a scalene triangle!")

        if side1 > 0 or side2 > 0 or side3 > 0:
            print("One of your sides is invalid!")

    except:
        print("Value Error")

main()
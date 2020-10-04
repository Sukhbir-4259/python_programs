def leap_year(x):
    if(x%4==0):
        if(x%100==0):
            if(x%400==0):
                return f"{x} is a leap year \nit contains 366 days"
            else:
                return f"{x} is not a leap year \n it contains 365 days"
        else:
             return f"{x} is a leap year \nit contains 366 days"
    else:
        return f"{x} is not a leap year \nit contains 365 days"
def main():
    try:
      year=int(input('Enter any year => '))
      print(leap_year(year))
    except:
        print('Write only in numeric values\nAnd run again !')
        main()        
main()
while True:
    answer = input("Run again? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye")
        break

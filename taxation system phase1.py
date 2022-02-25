#welcomeing front
print("||*********************************||")
print("\tWelcome to taxation system")
print("||*********************************||")
print("please select the county:")
print("  1. Amereica\n  2. Australia")

chose_num=int(input("Please enter your choise (1 or 2):"))
#determine which number did the user choose
if chose_num== 1:
    print("------------------------------")
    #take information form user
    ITIN=input("Enter Taxpayer Identification Number(ITIN):")
    full_name=input("Enter your Full Name:")
    annual_salary=float(input("Enter your annual Salary:"))
    #calculate the TPA for America  
    TPA_A1=(35/100)*annual_salary
    TPA_A2=(33/100)*annual_salary
    TPA_A3=(28/100)*annual_salary
    TPA_A4=(25/100)*annual_salary
    TPA_A5=(15/100)*annual_salary
    TPA_A6=(10/100)*annual_salary
    if annual_salary>=388351:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_A1, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    elif annual_salary<=388350 and annual_salary>=178651:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_A2, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    elif annual_salary<=178650 and annual_salary>=85651:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_A3, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    elif annual_salary<=85650 and annual_salary>=35351:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_A4, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    elif annual_salary<=35350 and annual_salary>=8701:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_A5, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    elif annual_salary<=8700 and annual_salary>=0:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_A6, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    else:
        print('Incorrect salary value:\nTry Again')
        print('--------------------------')
        print("Thanks for Useing Taxation system")
#determine which number did the user choose        
elif chose_num==2:
    print("------------------------------")
    ITIN=input("Enter Taxpayer Identification Number(ITIN):")
    full_name=input("Enter your Full Name:")
    annual_salary=float(input("Enter your annual Salary:"))
    #calculate the TPA for Australia 
    TPA_AU1=(45/100)*annual_salary
    TPA_AU2=(37/100)*annual_salary
    TPA_AU3=(30/100)*annual_salary
    TPA_AU4=(15/100)*annual_salary
    TPA_AU5="None"
    if annual_salary>=180001:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_AU1, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    elif annual_salary<=180000 and annual_salary>=80001:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_AU2, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    elif annual_salary<=80000 and annual_salary>=37001:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_AU3, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    elif annual_salary<=37000 and annual_salary>=6001:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",format(TPA_AU4, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    elif annual_salary<=6000 and annual_salary>=0:
        print("----------------------------")
        print("Welcome!",full_name)
        print("Your ITIN is:",ITIN)
        print("Your annual Salary is:",format(annual_salary, '.2f'),end='')
        print('$')
        print("----------------------------")
        print("Dear citizen ! Your Tax-payable ammount is:",TPA_AU5)
        print("----------------------------")
        print("Thanks for Useing Taxation system")
    else:
        print('Incorrect salary value:\nTry Again')
        print('--------------------------')
        print("Thanks for Useing Taxation system")
#determine which number did the user choose
#for negative numbers and other numbers (except for 1-2) 
else:
    print('''You should enter either 1 or 2:\nTry Again''')
    print('--------------------------')
    print("Thanks for Useing Taxation system")
    


def main():
    print("||***********************************||")
    print("\twelcome to taxation System")
    print("||***********************************||")
    print()
    display_menu()
    choice=input("Enter your choice(A or B or C):")
    print("-------------------------------------")
    cho=['a','A','B','b','C','c']
    #if the user enter anything exept for A-a-B-b-C-c
    while choice not in cho:
        print("Wrong entry!\nYou should enter A for Amereica or B for Australia or C to exit!")
        print("Try again!")
        print("-------------------------------------")
        choice=input("Enter your choice(A or B or C):")
    if choice=='a' or choice=='A':
        ITIN=str(input("Enter the Individual Taxpayer Identification Number (ITIN): "))
        isValid_ITIN(ITIN)
    elif choice=='B' or choice=='b':
        TFN=str(input("Enter the Tax file Number (TFN): "))
        isValid_TFN(TFN)
    else: #if choice=C or c
        print("You have choosen to End the program!")
        print("-------------------------------------")
        print("Thanks for Using Taxation System")
        
    while choice!='C' or choice!='c':     
        while choice=='a' or choice=='A' or choice=='b' or choice=='B':     
            name=input("Enter your Full Name: ")
            salary=float(input("Enter your annual Salary: "))
            print("-------------------------------------")
            while salary<0:
                print("Incorrect salary value!\nTry Again")
                print("-------------------------------------")
                salary=float(input("Enter your annual Salary: "))
            if choice=='a' or choice=='A':
                print("The Entered data:")
                print("Full name: ",name)
                print("ITIN: ",ITIN)
                print("The annual salary:",format(salary, '.2f'),'$')
                UTP=US_TaxPaid(salary)
                Tax_pay_amount=CalculateTax(salary,UTP)
                print("-------------------------------------")
                print("The citizen's Tax-payable amount is: ",format(Tax_pay_amount, ',.1f'),'$')
                WriteToFile(name,ITIN,salary,Tax_pay_amount)
            if choice=='B' or choice=='b':
                print("The Entered data:")
                print("Full name: ",name)
                print("TFN: ",TFN)
                print("The annual salary:",format(salary, '.2f'),'$')
                ATP=AU_TaxPaid(salary)
                try:
                    Tax_pay_amount=CalculateTax(salary,ATP)
                    print("-------------------------------------")
                except:
                    print("-------------------------------------")
                try:
                    print("The citizen's Tax-payable amount is: ",format(Tax_pay_amount, ',.1f'),'$')
                except:
                    print("The citizen's Tax-payable amount is: ",ATP)
                try:
                    WriteToFile(name,TFN,salary,Tax_pay_amount)
                except:
                    WriteToFile(name,TFN,salary,ATP)
                    
                
            main()
#the definition of the functions :-        
def display_menu():
    print("||**************Menu*****************||")
    print("Please select the country:")
    print("  A. Amereica\n  B. Australia\n  C. Exit")
    print("||***********************************||")
    
def isValid_ITIN(ITIN):
#    ITIN=str(input("Enter the Individual Taxpayer Identification Number (ITIN): "))
    while len(ITIN)!=9:
        print("Wrong entry, #####ITIN does not follow the rules!")
        print("Try again!")
        ITIN=str(input("Enter the Individual Taxpayer Identification Number (ITIN): "))
        while ITIN[0]!='9':
            print("Wrong entry, $$$$$$ITIN does not follow the rules!")
            print("Try again!")
            ITIN=str(input("Enter the Individual Taxpayer Identification Number (ITIN): "))
            list1=['70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','90','91','92','94','95','96','97','98','99']
            while ITIN[3:5] not in list1:
                print("Wrong entry, %%%%%%%ITIN does not follow the rules!")
                print("Try again!")
                ITIN=str(input("Enter the Individual Taxpayer Identification Number (ITIN): ")) 
                   
def isValid_TFN(TFN):
    while len(TFN)!=9:
        print("Wrong entry, TFN should be 9 digits!")
        print("Try again!")
        TFN=str(input("Enter the Tax file Number (TFN): "))
        
def US_TaxPaid(salary):
    if salary>=388351:
        ustax_per=(35/100)
    elif salary<=388350 and salary>=178651:
        ustax_per=(33/100)
    elif salary<=178650 and salary>=85651:
        ustax_per=(28/100)
    elif salary<=85650 and salary>=35351:
        ustax_per=(25/100)
    elif salary<=35350 and salary>=8701:
        ustax_per=(15/100)
    else:
        ustax_per=(10/100)
    return ustax_per

def AU_TaxPaid(salary):
    if salary>=180001:
        autax_per=(45/100)
    elif salary<=180000 and salary>=80001:
        autax_per=(37/100)
    elif salary<=80000 and salary>=37001:
        autax_per=(30/100)
    elif salary<=37000 and salary>=6001:
        autax_per=(15/100)
    else:
        autax_per='None'
    return autax_per

def CalculateTax(salary,TP):
    cal_tax=salary*TP
    return cal_tax
    
        
        
        
        
def WriteToFile(name,ID,salary,Tax_pay_amount):
    TPR=open('TaxPayableReport.txt','a')
    TPR.write(name + '\n')
    TPR.write(ID + '\n')
    #convert the numbers into string to add \n
    TPR.write(str(salary) + '\n')
    TPR.write(str(Tax_pay_amount) + '\n')
    TPR.close()
    print("The citizen's record has been written to the output file.")
    print("-------------------------------------")
    print()
        

main()
#the end
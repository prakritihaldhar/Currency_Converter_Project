#Python Currency Converter
def ind_to_euro(n):
    euro=n*0.0097
    print(euro," Euro :) ")

def ind_to_dol(n):
    dol=n*0.011
    print (dol," dollar :)")

def ind_to_pound(n):
    pound=n*0.0086
    print(pound," pound :)")

def ind_to_yen(n):
    yen=n*1.73
    print(yen," yen :)")

def ind_to_dir(n):
    dirham=n*0.042
    print(dirham," dirham :)")

def euro_to_ind(n):
    print(n *102.86,"Indian Rupee :) ")

def dol_to_ind(n):
    print(n*88.49," Indian Rupee :)")

def pound_to_ind(n):
    print(n*116.91, " Indian Rupee :)")

def yen_to_ind(n):
    print(n*0.58," Indian Rupee :)")

def dir_to_ind(n):
    print(n*24.04," Indian Rupee :)")


ans="Yes"

while (ans in ("Yes","yes")):
    print("Example want to convert to indian to dollar so kindly enter 'Rupee to dollar ' :)")
    user_input=input("From which to which currency do want to convert : ")
    l=user_input.split()
    if l[0] in ("Rupee","rupee") and l[2] in ("Euro","euro"):
        input_currency=int(input("Kindly enter amount in Indian Rupee : "))
        print("----->",end="")
        ind_to_euro(input_currency)

    elif l[0] in ("Rupee","rupee") and l[2] in ("Dollar","dollar"):
        input_currency1=int(input("Kindly enter amount in Indian Rupee : "))
        print("----->",end="")
        ind_to_dol(input_currency1)

    elif l[0] in ("Rupee","rupee") and l[2] in ("Pound","pound"):
        input_currency2=int(input("Kindly enter amount in Indian Rupee : "))
        print("----->",end="")
        ind_to_pound(input_currency2)

    elif l[0] in ("Rupeen","rupee") and l[2] in ("Yen","yen"):
        input_currency3=int(input("Kindly enter amount in Indian Rupee : "))
        print("----->",end="")
        ind_to_yen(input_currency3)

    elif l[0] in ("Rupee","rupee") and l[2] in ("Dirham","dirham"):
        input_currency4=int(input("Kindly enter amount in Indian Rupee : "))
        print("----->",end="")
        ind_to_dir(input_currency4)

    elif l[0] in ("Euro","euro") and l[2] in ("Rupee","rupee"):
        input_currency5=int(input("Kindly enter amount in Euros : "))
        print("----->",end="")
        euro_to_ind(input_currency5)

    elif l[0] in ("Dollar","dollar") and l[2] in ("Rupee","rupee"):
        input_currency6=int(input("Kindly enter amount in Dollar : "))
        print("----->",end="")
        dol_to_ind(input_currency6)

    elif l[0] in ("Pound","pound") and l[2] in ("Rupee","rupee"):
        input_currency7=int(input("Kindly enter amount in Pound : "))
        print("----->",end="")
        pound_to_ind(input_currency7)

    elif l[0] in ("Yen","yen") and l[2] in ("Rupee","rupee"):
        input_currency8=int(input("Kindly enter amount in Yen : "))
        print("----->",end="")
        yen_to_ind(input_currency8)

    elif l[0] in ("Dirham","dirham") and l[2] in ("Rupee","rupee"):
        input_currency9=int(input("Kindly enter amount in Dirham : "))
        print("----->",end="")
        dir_to_ind(input_currency9)

    else:
        print("Invalid input :(")

    ans=input("Wants to convert currency (Yes/No) : ")
    if (ans in ("No","no")):
        print("    THANK YOU   ")
    
    

            


        
    
    
    

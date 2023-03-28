'''Program za sada izvrsava u konzoli
Funkcionalnosti:
1. Izbornik
2. Otvaranje racuna tvrtke
3. Prikaz stanja racuna
4. Prikaz prometa po racunu
5. Polog novca na racun
6. Podizanje novca sa racuna
7.Izlaz iz programa (program se nakon svake akcije vrati na pocetni izbornik u kojem postoji opcija Izlaz)
'''
import random
import os
import sys

os.system("cls")

print()
print("\t" + "*" * 60)
print("\t\t\t    PyBank by Algebra")
print()
print()
print()

# declared variables 
string_of_numbers = "0123456789"
shuffle_string = "".join(random.sample(string_of_numbers,len(string_of_numbers)))
account_balance = 0
a = 0
list_of_spendings = []
currency_check = ""
#account_information = " "

# declared functions
def show_bank_account_balance():
    """Ova funkcija pokazuje stanje racuna"""
    
    os.system("cls")
    
    global account_balance
    print()
    print(f'Na racunu imate raspolozivo {account_balance} sredstava.')
    print()
    
def show_account_spendings():
    """Ova funkcija prikazuje transakcije sa racuna"""
    
    os.system("cls")
    
    global list_of_spendings
    if len(list_of_spendings) == 0:
        print("Jos niste napravili nikakvu transakciju!")
        print()
    else:
        print(list_of_spendings) 
        print()

def money_pay_down():
    """Ova funkcija sluzi za uplatu novca na racun"""
    
    os.system("cls")
    global currency_check
    global account_balance
    currency_check = input("Zelite li uplatiti u kunama ili euru? Ukoliko zelite u kunama upisite HRK, a ukoliko zelite u euru napisite EUR\n").lower()
    if currency_check == "hrk":
        money_depositing = int(input("Koliko novaca zelite uplatiti?\n"))
    else:
        pass
    if currency_check == "eur":
        money_depositing = int(input("Koliko novaca zelite uplatiti?\n"))
    else:
        pass
        
    print()
    account_balance = account_balance + money_depositing
    return account_balance, list_of_spendings.append('Uplata: ' + str(money_depositing) + " " + f"{currency_check.upper()}")

def money_pay_up():
    """Ova funckija sluzi za podizanje sredstava sa racuna"""
    
    os.system("cls")
    
    global account_balance
    print(f'Preostalo sredstava na racunu: {account_balance}')
    if account_balance == 0:
        print("Nedovoljno sredstava na racunu!")
        print()
    elif account_balance > 0:
        money_from_account = int(input("Koliko novaca zelite podici? "))
        account_balance = account_balance - money_from_account
        print(f'Preostalo sredstava na racunu: {account_balance}')
        print()
        return account_balance, list_of_spendings.append('-' + str(money_from_account))

def exit():
    """Kada se pozove ova funkcija, prekida se aplikacija"""
    
    os.system("cls")
    sys.exit()

def open_company_account():
    """Ovdje uzimam podatke od usera za otvaranje bankovnog racuna"""
    
    global a
    global shuffle_string
    global account_information
    
    os.system("cls")
    print("\t" + "-" * 50)
    print("\t\t     OTVARANJE RACUNA TVRTKE")
    print("\t" + "-" * 50)
    print()
    print()
    company_name = input("Naziv:\t\t\t\t")
    company_street_and_number = input("Adresa:\t\t\t\t")
    company_OIB = input("OIB:\t\t\t\t")
    
    while company_OIB.isnumeric() != True or len(company_OIB) != 11:
        print()
        print("OIB mora sadrzavati 11 brojeva ne ukljucujuci znakove! Pokusajte ponovno: ")
        company_OIB = input("OIB:\t\t\t\t")
            
    company_owner = input("Vlasnik:\t\t\t")
    company_status = input("Status:\t\t\t\t")
    company_capital = input("Temeljni kapital:\t\t")
    
    while company_capital.isnumeric() != True:
        print()
        print("Unos kapitala moze sadrzavati samo brojeve bez razmaka ili ostalih znakova! Pokusajte ponovno! ")
        company_capital = input("Temeljni kapital:\t\t")
    
    
    
    company_IBAN_generated = ("IBAN:  BA" + f"{shuffle_string}")
    print()
    print("Uspjesno ste popunili podatke !")
    print("Dodijeljen Vam je IBAN ! ")
    print()
    print(company_IBAN_generated)
    print()
    print()
    a += 1
    account_information ="Naziv:\t" + company_name + "\n" + "Adresa:\t" + company_street_and_number + "\n" + "OIB:\t" + company_OIB + "\n"  + "Vlasnik:\t" + company_owner + "\n" + "Status:\t" + company_status + "\n" + "Temeljni kapital:\t" + company_capital
    return account_information
   
def already_opened():
    global account_information
    os.system("cls")
    print()
    print(f'Vec imate napravljen racun !') 
    print(account_information)  
    print()  
    print("Vracamo vas na izbornik...")        
    print()
    print()
    
def user_input():
    print("""1. OTVARANJE RACUNA TVRTKE\n
2. PRIKAZ STANJA RACUNA\n
3. PRIKAZ PROMETA PO RACUNU\n
4. POLOG NOVCA NA RACUN\n
5. PODIZANJE NOVCA SA RACUNA\n
6.IZLAZ IZ APLIKACIJE\n""")

    choice = int(input("Odaberite radnju iz glavnog izbornika: "))

    print()
    if choice == 1:
            if a == 0:
                open_company_account()
            else:
                already_opened()
    elif choice == 2:
            show_bank_account_balance()
    elif choice == 3:
            show_account_spendings()
    elif choice == 4:
            money_pay_down()
    elif choice == 5:
            money_pay_up()
    elif choice == 6:
            exit()


# main while loop
while True:
    user_input()

    
    
    
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
print("Dobrodosli!")
print()

# declared variables 
string_of_numbers = "0123456789"
shuffle_string = "".join(random.sample(string_of_numbers,len(string_of_numbers)))
account_balance = 0
a = 0
list_of_spendings = []

# declared functions
def show_bank_account_balance():
    global account_balance
    print(f'Na racunu imate raspolozivo {account_balance} sredstava.')

def show_account_spendings():
    global list_of_spendings
    print(list_of_spendings)
    pass

def money_pay_down():
    global account_balance
    money_depositing = int(input("Koliko novaca zelite uplatiti? "))
    print()
    account_balance = account_balance + money_depositing
    return account_balance, list_of_spendings.append('+' + str(money_depositing))

def money_pay_up():
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
    os.system("cls")
    sys.exit()

def open_company_account():

    global new_bank_account
    global name_and_IBAN
    global new_bank_account_IBAN
    global a
                
    if a == 0:
        global b
        new_bank_account = input("Upisite naziv firme: ")
        print()     
        new_bank_account_IBAN = f"Naziv firme: {new_bank_account}\n" + "IBAN: HR" + shuffle_string
        print(new_bank_account_IBAN)
        print()    
        a = a + 1
        return a 
    
    elif a == 1:
        os.system("cls")
        print()
        print(f'Vec imate napravljen racun: \n\n{new_bank_account_IBAN}\n')
        print("Vracamo vas na izbornik:")
        print()
    
def user_input():
    print(""" \t\t  1. Otvaranje racuna tvrtke\n
                  2. Prikaz stanja racuna\n
                  3. Prikaz prometa po racunu\n
                  4. Polog novca na racun\n
                  5. Podizanje novca sa racuna\n
                  6.Izlaz iz programa\n""")

    choice = int(input("Odaberite radnju iz glavnog izbornika: "))
    os.system("cls")
    print("2. Otvaranje racuna tvrtke ")
    print()
    
    if choice == 1:
            open_company_account()
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

    
    
    
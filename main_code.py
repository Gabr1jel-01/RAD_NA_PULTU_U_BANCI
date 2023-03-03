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

print()
print("Dobrodosli!")
print()

list_of_numbers = [1,2,3,4,5,6,7,8,9,0]
a = 0

if a == 0:
    
    def open_company_account():
        global new_bank_account 
        new_bank_account = input("Upisite naziv firme: ")
        global new_bank_account_IBAN 
        new_bank_account_IBAN = "HR" + random.shuffle(list_of_numbers)
        global name_and_IBAN
        name_and_IBAN = print(new_bank_account + "\n" + new_bank_account_IBAN)
        a = a + 1
        return a
else:
    print(f"""Vec imate napravljen bankovni racun: \n
          {name_and_IBAN}""")

def show_bank_account_balance():
    global account_balance 
    account_balance = 0 - money_pay_up() + money_pay_down()
    return account_balance

def show_account_spendings():
    pass

def money_pay_down():
    money_depositing = int(input("Koliko novaca zelite uplatiti? "))
    account_balance = account_balance + money_depositing
    return account_balance

def money_pay_up():
    if account_balance == 0:
        print("Nedovoljno sredstava na racunu!")
    elif account_balance >= 0:
        money_from_account = int(input("Koliko novaca zelite podici? "))
        account_balance = account_balance - money_from_account
        return account_balance

def exit():
    pass


def user_input():
    print(""" 2. Otvaranje racuna tvrtke\n
              3. Prikaz stanja racuna\n
              4. Prikaz prometa po racunu\n
              5. Polog novca na racun\n
              6. Podizanje novca sa racuna\n
              7.Izlaz iz programa\n""")
    
    choice = int(input("Odaberite radnju iz glavnog izbornika: "))
    if choice == 2:
        open_company_account()
    elif choice == 3:
        show_bank_account_balance()
    elif choice == 4:
        show_account_spendings()
    elif choice == 5:
        money_pay_down()
    elif choice == 6:
        money_pay_up()
    else:
        exit()
        


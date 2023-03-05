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

string_of_numbers = "0123456789"
shuffle_string = "".join(random.sample(string_of_numbers,len(string_of_numbers)))


account_balance = 0
a = 0

while True:
    
    def open_company_account():
            global new_bank_account 
            new_bank_account = input("Upisite naziv firme: ")
            print()
            global new_bank_account_IBAN 
            new_bank_account_IBAN = f"Naziv firme: {new_bank_account}\n" + "IBAN: HR" + shuffle_string
            global name_and_IBAN
            name_and_IBAN = print(new_bank_account_IBAN)
            #global a 
            a = a + 1
            return a
    if a == 0:
        open_company_account()
        
    else:
        print(f"""Vec imate napravljen bankovni racun:{name_and_IBAN}""")

    def show_bank_account_balance():
        account_balance = 0
        account_balance = 0 - money_pay_up() + money_pay_down()
        return account_balance

    def show_account_spendings():
        pass

    def money_pay_down():
        money_depositing = int(input("Koliko novaca zelite uplatiti? "))
        account_balance = account_balance + money_depositing
        return account_balance

    def money_pay_up():
        global account_balance
        if account_balance == 0:
            print("Nedovoljno sredstava na racunu!")
        elif account_balance >= 0:
            money_from_account = int(input("Koliko novaca zelite podici? "))
            account_balance = account_balance - money_from_account
            return account_balance

    def exit():
        return False


    def user_input():
        print(""" \t\t2. Otvaranje racuna tvrtke\n
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
        elif choice == 7:
            exit()


    user_input()
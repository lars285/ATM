import random
import pwinput # pip install pwinput
from modules.json import Json
from colorama import Fore, Style # pip install colorama

JSON = Json()
JSON.LoadFromJSON()
class OptionParts:

    menuNumber = 0
    tries = 3

    def Beginning(self):
        print(Style.RESET_ALL + "Welcome to lars bank!") 
        print ("Please Enter, what you want to do?")
        print(Fore.GREEN + "1. Create new Bank Account")
        print(Fore.BLUE + "2. Deposit money")
        print(Fore.MAGENTA + "3. Withdraw money")
        print(Fore.CYAN + "4. Show Account History")
        print(Fore.YELLOW + "5. Exit Bank" + Style.RESET_ALL)
        self.menuNumber = input()

    def CreateAccount(self):
        JSON.LoadFromJSON()
        JSON.bankStatementCounter.append(0)
        print(Fore.GREEN + "Please enter your first name " + Style.RESET_ALL)
        firstNamesTmp = input()
        JSON.firstNames.append([firstNamesTmp])
        print(Fore.GREEN + "Please enter your last name " + Style.RESET_ALL)
        lastNamesTmp = input()
        JSON.lastNames.append([lastNamesTmp]) 
        print(Fore.GREEN + "Please enter your value " + Style.RESET_ALL)
        JSON.bankAccountHistory.append(['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])
        valueTmp = float(input())
        JSON.value.append([str(valueTmp)])
        print("You successfully created an account ")
        pinTmp = random.randint(1111,9999)
        JSON.pin.append([pinTmp])
        for i in range(len(JSON.pin)):
            if JSON.pin[int(i)] == [int(pinTmp)]:
                JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]] = str(valueTmp)
                JSON.bankStatementCounter[i] +=1

        print("Her is your PIN: " + Fore.RED + str(pinTmp) + Style.RESET_ALL + ". Remember it and don't tell anyone about it!")
        JSON.SaveToJSON()
    
    def DepositMoney(self):
        print (Fore.RED + "Please Enter your PIN." + Style.RESET_ALL)
        pinTmp = pwinput.pwinput(prompt='PIN: ', mask='*')
        for i in range(len(JSON.pin)):
            if JSON.pin[int(i)] == [int(pinTmp)]:
                print(Fore.BLUE + "Hello " + str(*JSON.firstNames[int(i)]) + " " + str(*JSON.lastNames[int(i)]) + "!" + Style.RESET_ALL)
                print ("Your current bank balance is: " + Fore.RED + str(*JSON.value[int(i)]) + "€")
                print (Fore.BLUE + "How many do you want do deposite ?" + Style.RESET_ALL)
                deposite = input()
                JSON.value[int(i)] = [str(round(float(*JSON.value[int(i)]) + float(deposite), 2))]
                print("Your new balace is: " + Fore.RED + str(*JSON.value[int(i)]) + "€." + Style.RESET_ALL)
                if int(JSON.bankStatementCounter[i]) >= 10:
                     del JSON.bankAccountHistory[i][0]
                     JSON.bankAccountHistory[i].append('-')
                     JSON.bankAccountHistory[i][9] = str(*JSON.value[i])
                else:
                    JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]] = str(*JSON.value[i])
                    JSON.bankStatementCounter[i] +=1
                JSON.SaveToJSON()
                break
            if (i < len(JSON.pin)-1):
                continue
            else:
                self.tries-=1
                print("Wrong PIN! Try Again. Times left: " + Fore.RED + str(self.tries) + Style.RESET_ALL + ".")
                if (self.tries == 0):
                    print(Fore.RED + "You entered the wrong PIN too many times!" + Style.RESET_ALL)
                    exit()
                self.DepositMoney()
        

    def WithdrawMoney(self):
        print (Fore.RED + "Please Enter your PIN." + Style.RESET_ALL)
        pinTmp = pwinput.pwinput(prompt='PIN: ', mask='*')
        for i in range(len(JSON.pin)):
            if JSON.pin[int(i)] == [int(pinTmp)]:
                print(Fore.MAGENTA + "Hello " + str(*JSON.firstNames[int(i)]) + " " + str(*JSON.lastNames[int(i)]) + "!" + Style.RESET_ALL)
                print ("Your current bank balance is: " + Fore.RED + str(*JSON.value[int(i)]) + "€" + Style.RESET_ALL)
                print (Fore.MAGENTA + "How many do you want do withdraw ?" + Style.RESET_ALL)
                withdraw = input()
                JSON.value[int(i)] = [str(round(float(*JSON.value[int(i)]) - float(withdraw), 2))]
                print("Your new balace is: " + Fore.RED + str(*JSON.value[int(i)]) + "€." + Style.RESET_ALL)
                if int(JSON.bankStatementCounter[i]) >= 10:
                     del JSON.bankAccountHistory[i][0]
                     JSON.bankAccountHistory[i].append('-')
                     JSON.bankAccountHistory[i][9] = str(*JSON.value[i])
                else:
                    JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]] = str(*JSON.value[i])
                    JSON.bankStatementCounter[i] +=1
                JSON.SaveToJSON()
                break
            if (i < len(JSON.pin)-1):
                continue
            else:
                self.tries-=1
                print("Wrong PIN! Try Again. Times left: " + Fore.RED + str(self.tries) + Style.RESET_ALL + ".")
                if (self.tries == 0):
                    print(Fore.RED + "You entered the wrong PIN too many times!" + Style.RESET_ALL)
                    exit()
                self.WithdrawMoney()

    def AccountHistory(self):
        print (Fore.RED + "Please Enter your PIN." + Style.RESET_ALL)
        pinTmp = pwinput.pwinput(prompt='PIN: ', mask='*')
        for i in range(len(JSON.pin)):
            if JSON.pin[int(i)] == [int(pinTmp)]:
                print(Fore.CYAN + "Hello " + str(*JSON.firstNames[int(i)]) + " " + str(*JSON.lastNames[int(i)]) + "!" + Style.RESET_ALL)
                print(Fore.CYAN + "Here is your Bank Account History: " + Style.RESET_ALL)
                a = 9
                vergleich = 0
                f = 0
                while f < (JSON.bankStatementCounter[i]):
                    if (float(vergleich) < float(JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]-f-1]) and a < 9 and float(JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]-f -1]) > 0): 
                        print("   " + Fore.GREEN + "+" + str(-(round(float(vergleich) - float(JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]-f-1]), 2))) + "€" + Style.RESET_ALL)
                        print(str(JSON.bankStatementCounter[i]-f) + ". " + JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]-f-1] + "€" + Style.RESET_ALL)
                    elif (float(vergleich) > float(JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]-f-1]) and a < 9) or float(JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]-f-1]) < 0:
                         print("   " + Fore.RED + str(-(round(float(vergleich) - float(JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]-f-1]), 2))) + "€" + Style.RESET_ALL)
                         print(str(JSON.bankStatementCounter[i]-f) + ". "  + JSON.bankAccountHistory[i][JSON.bankStatementCounter[i]-f-1] + "€" + Style.RESET_ALL)
                    else:
                        print(str(JSON.bankStatementCounter[i]-f) + ". " + JSON.bankAccountHistory[i][(JSON.bankStatementCounter[i]-f-1)] + "€")
                    vergleich = JSON.bankAccountHistory[i][(JSON.bankStatementCounter[i]-f-1)]
                    a -= 1
                    f += 1
                JSON.SaveToJSON()
                break
            
            if (i < len(JSON.pin)-1):
                continue
            else:
                self.tries-=1
                print("Wrong PIN! Try Again. Times left: " + Fore.RED + str(self.tries) + Style.RESET_ALL + ".")
                if (self.tries == 0):
                    print(Fore.RED + "You entered the wrong PIN too many times!" + Style.RESET_ALL)
                    exit()
                self.AccountHistory()

    def exitBank(self):
        exit()
        
from modules.json import Json
from modules.optionParts import OptionParts

JSON = Json()
OP = OptionParts()

while True:
    OP.Beginning()
    if int(OP.menuNumber) == 1:
        OP.CreateAccount()
    if int(OP.menuNumber) == 2:
        OP.DepositMoney()
    if int(OP.menuNumber) == 3:
        OP.WithdrawMoney()
    if int(OP.menuNumber) == 4:
        OP.AccountHistory()
    if int(OP.menuNumber) == 5:
        OP.forgotPin()
    if int(OP.menuNumber) == 6:
        OP.exitBank()
    

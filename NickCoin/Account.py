from hashingfunctions import makeahash
from Transaction import maketrx

class Account:
    def __init__(self,name,bc_copy,balance=0):
        self.name = name
        self.addy = makeahash(name)
        self.trx_history = []
        self.balance = balance
        self.prompts = ["You do not have enough NickCoins to make this transaction"]
    
    def make_trx(self):
        trx_amount = float(input("Insert your transaction amount"))
        sendto = str(input("Enter the address that you would like to send coin to:"))
        message = str(input("Insert a message you would like to attach to your transaction"))
        if self.balance < trx_amount:
            print(self.prompts[0])
            new_trx = None
        elif self.balance >=trx_amount:
            new_trx = maketrx(self.addy,sendto,trx_amount,message)
            new_trx.print_trx()
        else:
            print("Transaction error")
        return new_trx

newperson = Account("Malachi",[])

print(newperson.name)

newperson.make_trx()
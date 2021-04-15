class Budget:

    def __init__(self,**categories):
        self.categories = categories
        print(self.categories)

    def deposit(self, amount, category):
        self.categories[category] = self.categories[category] + amount
        print(f'''  You deposited the sum of {amount} to {category.upper()}
        Your {category.upper()} Balance is now {self.categories[category]}
********************************************************************''')
        
    
    def withdraw(self,amount,category):
        if amount > self.categories[category]:
            print("Insufficient Balance")
        else:

            self.categories[category] = self.categories[category] - amount
            print(f''' You withdrew the sum of {amount} from {category.upper()}
        Your {category.upper()} Balance is now {self.categories[category]}
********************************************************************''')

    def transfer(self, amount, debit_category, credit_category):
        if amount > self.categories[debit_category]:
            print('Insufficient Balance')
        else:
            self.categories[debit_category] = self.categories[debit_category] - amount
            self.categories[credit_category] =  self.categories[credit_category] + amount
            print(f''' You transfered the sum of {amount} from {debit_category.upper()} to {credit_category.upper()}  
********************************************************************''')
    
    def checkBalance(self,category):
        print(f''' Your {category.upper()} budget balance is : {self.categories[category]} 
********************************************************************''')
        

mybudget= Budget(food = 1000, clothing = 1000, entertainment = 1000)
mybudget.deposit(400,'entertainment')
mybudget.deposit(400,'clothing')
mybudget.deposit(400,'food')

mybudget.withdraw(600,'clothing')
mybudget.withdraw(600,'food')
mybudget.withdraw(600,'entertainment')

mybudget.transfer(500,'food','clothing')

mybudget.checkBalance('food')
mybudget.checkBalance('clothing')
mybudget.checkBalance('entertainment')

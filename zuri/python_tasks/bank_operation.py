import random

database = {} 

def welcome():

    print('''  Welcome to World Bank ''')
 
    have_account = int(input("""  Do you have account with us: 
                            If YES press:  1  
                            if NO press:   2  """ ))
    if(have_account == 1):
        login()
        
    elif(have_account == 2):
        register()
        
    else:
        print("""  You have selected invalid option  """)
        welcome()



def register():

    print(""" --------- Register -------------""" )

    email = input("What is your email address?: ")
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    password = input("create a password for yourself: ")
    acount_balance = 0

    account_number = generation_account_number()

    database[account_number] = [ first_name, last_name, email, password, acount_balance]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()
    
    return None
	
def login():
    
    print("""  ********* Login ***********  """)

    account_number_from_user = int(input("""  What is your account number?: """ ))
    password = input("What is your password ")
    
    try:
        for account_number, user_details in database.items():
            if(account_number == account_number_from_user) and (user_details[3] == password):
                bank_operation(database, account_number)
            else:
                print('Invalid account or password')
                login()

                    
    except:
        pass
		

def withdrawal_operation(database, account_number):
    print(''' *************withdrawal ************* ''')
    withdrawal_amount = float(input("How much would you like to withdrawal?: "))
    
    fist_name = database[account_number][0]
    last_name = database[account_number][1]
    email = database[account_number][2]
    password = database[account_number][3]
    amount = database[account_number][4]
    
    account_balance = amount - withdrawal_amount
    
    database[account_number] = [fist_name, last_name, email, password, account_balance]
    
    
    print('processing..')
    print('take your cash') 
    print(f""" Your balance is {account_balance}""")
    
    bank_operation(database, account_number)
    
    return None


def deposit_operation(database, account_number):
    print(''' *************Deposit ************* ''')
    deposit_amount = float(input("How much would you like to Deposit?: "))
    
    fist_name = database[account_number][0]
    last_name = database[account_number][1]
    email = database[account_number][2]
    password = database[account_number][3]
    amount = database[account_number][4]
    
    account_balance = deposit_amount + amount
    
    database[account_number] = [fist_name, last_name, email, password, account_balance]
    print(f""" Your balance is {account_balance}""")   
    
    bank_operation(database, account_number)
    
    return None

def balance_operation(database, account_number):
    print(''' ************* Balance ************* ''')
    
    account_balance = database[account_number][4]
    print(f""" Your balance is {account_balance}""")
    bank_operation(database, account_number)
    
    return None

def generation_account_number():
    return random.randrange(1111111111,9999999999)

def logout():
    login()
	
	
def bank_operation(database, account_number):

    first_name = database[account_number][0]
    last_name = database[account_number][1]
    

    users_option = int(input(f"""  
        Welcome {first_name.upper()} {last_name.upper()}
        (1) Deposit 
        (2) Withdrawal
        (3) Balance
        (4) Logout 
        (5) Exit     
        
    What would you like to do?"""))

    if(users_option == 1):
        deposit_operation(database, account_number)
        
    elif(users_option == 2):
        withdrawal_operation(database, account_number)
        
    elif users_option ==3:
        balance_operation(database, account_number)
        
    elif(users_option == 4):
        logout()
        
    elif(users_option == 5):
        pass
        #exit()
        
    else:
      
        print("Invalid option selected")
        bank_operation(user, database, account_number)

welcome()


import logging as lg
lg.basicConfig(filename="app.log",
               level=lg.DEBUG,
               format="[%(asctime)s-%(levelname)s]-%(message)s")

#operations
operations=(
    "1.balance enquriy/n",
    "2.withdrawal/n",
    "3.deposte/n",
    "4.transfer/n",
    "5.history/n",
    "6.exit/n"
)


#account table
account_details={12345:2000,
                 123456:3000}
#users table
users_table={12345:['srinubabu','date of birth',1000],
             123456:['babu','01-01-2000',1250]}

#transcation table
transcation_table={12345:[],
                   123456:[]}

#checking user login
def check_login(account_no:int,pin:int):
    #check user are present in accounts table
    if account_no in account_details:
        #pin validation
        if account_details[account_no]==pin:
            lg.info("user sucessfully logined")
            return True
        else:
            lg.warning("user credientials incorrect")
    else:
        lg.warning("user not found")
        return False
    
#balance enquiry function   
def balance_enquiry(account_no):
    lg.debug("user in balance_enquiry page ")
    if account_no in users_table:
        amount=users_table[account_no][2]
        lg.info(f'(account_no) user current amount{amount}')
        print(f'(account_no) user current amount{amount}')
    else:
        lg.warning("user not found")
        print("user not found")
    

#withdrawal function
def withdrawal(account_no):
    lg.debug("user in withdrwal  page ")
    amount=users_table[account_no][2]
    withdrawal_amount=int(input("please enter withdraw amount:"))
    if amount >= withdrawal_amount:
        users_table[account_no][2] -= withdrawal_amount
        lg.info(f'(withdraw_amount) withdraw sucessfully and  current amount {users_table[account_no][2]}')
        print(f'(withdraw_amount) withdraw sucessfully and  current amount {users_table[account_no][2]}')
    else:
        lg.warning("insuffecient amount")
        print("insuffecient amount")
    
    

#deposit function
def deposit(account_no):
    lg.debug("user in deposit page ")
    deposit_amount=int(input("please enter deposite amount:"))
    if account_no in users_table:
        users_table[account_no][2] += deposit_amount
        lg.info(f'(deposit_amount) deposit sucessfully and  current amount{users_table[account_no][2]}')
        print(f'(deposit_amount) deposit sucessfully and  current amount{users_table[account_no][2]}')
    
    

#transfer function
def transfer(account_no:int):
    lg.debug("user in transfer page")
    transfer_account=int(input("enter the transfer account number:"))
    transfer_amount=int(input("enter the transfer amount:"))
    lg.info(f"receiver account is {transfer_account} and amount is {transfer_amount}")
    current_amount=users_table[account_no][2]
    if transfer_account in users_table:
        if transfer_amount <= current_amount:
        #amount update in account
         users_table[account_no][2]-=transfer_amount
         users_table[transfer_account][2]+=transfer_amount
         lg.info(f'(transfer_amount) transfer sucessfuly and current balance is{users_table[account_no][2]}')
         print(f'(transfer_amount) transfer sucessfuly and current balance is{users_table[account_no][2]}')
        else:
         lg.warning("insufficient amount")
         print("insufficient amount")
    else:
        lg.warning(f'{transfer_account} user not found')
        print(f'{transfer_account} user not found')     
      

#history function
def history(account_no):
    lg.debug("user in history page ")
    print("function developing under processing")
    

#exit function
def exit_fun():
     lg.debug("user in exit page")
     print("succefully exited ,thank you for using online bank servies")
     return True



#select operation
def choose_operation(account_no:int,choice:int):
    val =False
    if choice == 1:
        balance_enquiry(account_no=account_no)
    elif choice == 2:
        withdrawal(account_no=account_no)
    elif choice == 3:
        deposit(account_no=account_no)
    elif choice == 4:
        transfer(account_no=account_no)
    elif choice == 5:
        history(account_no=account_no)
    elif choice == 6:
        val = exit_fun()
    else:
        print("invaild choice,please select between 1-6:")
    if val:
        return val
        



#main function
if __name__ == "__main__":
    print("welcome to online codegnan banking ")
    lg.info("welcome to online codegnan banking ")
    account_no=int(input("please ,enter your account number:"))
    pin=int(input("please ,enter your pin:"))
    lg.info(f"user account number is {account_no} and pin is {pin}")
    while True:
      if check_login(account_no=account_no,pin=pin):
         print(*operations)
         lg.info(operations)
         choice=int(input("select operations(1-6):"))
         exit_fun_val=choose_operation(account_no=account_no,choice=choice)
         if exit_fun_val:
            break
      else:
         lg.warning(f"login credentails incorrect {account_no} and {pin}")
         print(f"login credentails incorrect {account_no} and {pin}")
         break  

   
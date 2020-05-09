import random


def create_account():
    print("welcome to account creation page")
    customer_data =[]
    account_name =input("Enter your account Name: ")
    account_bal =input("Enter your account balance: ")
    account_type =input("Enter your account Type: ")
    account_email =input("Enter your Email: ")
    account_no=''.join(map(str,[random.randint(0, 9) for i in range(0,9)]))
    print("Your Account has been created, and your Account number is  \n" + account_no)
    customer_file=open ("customer.txt","w+")
    customer_file.write("Account Name:%s\n" % account_name)
    customer_file.write("Account Balance:%s\n" % account_bal)
    customer_file.write("Account Type:%s\n" % account_type)
    customer_file.write("Account Email: %s\n" % account_email)
create_account()
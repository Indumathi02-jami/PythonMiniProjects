def varification(email):
    dot=email.find(".")
    at=email.find("@")
    if(dot== -1):
        print("Invalid Email")
    elif(at == -1):
        print("Invalid Email")
    else:
        print(f"Valid Email : {email}")

print("This program will decide if your input is a valid email address")
is_run=True
while(is_run):
    print("1.Continue the process \n2.Exit")
    print("A valid email address needs an '@' symbol and a '.'")
    choice = input("Enter your choice:")
    if(choice == '1'):
        x = input("Input your email address:").lower()
        varification(x)
    else:
        is_run=False
print("Thank You for Using.....")

    
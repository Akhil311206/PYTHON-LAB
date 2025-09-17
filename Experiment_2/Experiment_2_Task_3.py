# Akhil
# 2024UG3008
# CD-2101 - PYTHON PROGRAMMING LAB
# Experiment 2 Task 3 - Password Check

password=input("Enter password: ")

upper,lower,num,splchr=False, False, False, False

if(len(password)>=8):
    if(any(char.isupper() for char in password)):
        upper=True
    if(any(char.islower() for char in password)):
        lower=True
    if(any(char.isdigit() for char in password)):
        num=True
    if(any(not char.isalnum() for char in password)):
        splchr=True
else:
    print("Minimum 8 characters")


if(len(password)>=8):
    if(upper & lower & num & splchr):
        print("Password accepted")
    else:
        print("Enter valid password")

# Akhil
# 2024UG3008
# CD-2101 - PYTHON PROGRAMMING LAB
# Experiment 2 Task 1 - Conditional Statements

age=input("Enter you age: ")

if(age.isdigit()):
    age=int(age)
    if(age<18):
        print("You are a minor")
    elif(age>=18 & age<65):
        print("You are an adult")
    elif(age>=65):
        print("You are a senior")
    else:
        print("Enter valid age")
else:
    print("Enter valid age")

# Akhil
# 2024UG3008
# CD-2101 - PYTHON PROGRAMMING LAB
# EXPERIMENT 1 - TASK 2 : Computing student marks and assigning grade  

n=5
marks=[92,95,91,90,100]
sum=0

for i in marks:
    sum +=i

average = sum/n

if(average>=90): print("Grade A")
elif(average >=80 & average<90): print("Grade B")
elif(average >=70 & average<80): print("Grade C")
elif(average >=60 & average<70): print("Grade D")
else: print("Grade F")

# Akhil
# 2024UG3008
# CD-2101 - PYTHON PROGRAMMING LAB
# Experiment 2 Task 3 - Password Check

import matplotlib.pyplot as plt

sales_data=[25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]

total_sales = 0
for sales in sales_data:
    total_sales += sales

average_sales=total_sales/len(sales_data)


max_sales = sales_data[0]  
for sales in sales_data:
    if sales > max_sales:
        max_sales = sales

month_with_highest_sales=sales_data.index(max_sales)+1
print("Month with Highest Sales:", month_with_highest_sales)
print("Maximum Sales:", max_sales)
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
plt.plot(sales_data, marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Data")
plt.show()
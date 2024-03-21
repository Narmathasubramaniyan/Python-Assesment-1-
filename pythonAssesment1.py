#1)Write a program to find the reverse of n digit number using While loop

"""
a = 12345
b = 0
while a > 0:
    x = a % 10
    b = b * 10 + x
    a = a // 10
print(b)
    """



#2)input is 12391 then the output should be displayed as 23402.

"""
a = input("Enter number: ")

if len(a) != 5 or not a.isdigit():
    print("Invalid input! Please enter a five-digit number.")
else:
    new_number = ""
    for i in a:
        digit = (int(i) + 1) % 10
        new_number += str(digit)  
    print(new_number)
"""

#3)The length & breadth of a rectangle and radius of a circle are input through the keyboard.
# Write a program to calculate the area & perimeter of the rectangle, and the area & circumference 
# of the circle.
"""

import math
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))
rectangle_area = length * breadth
rectangle_perimeter = 2 * (length + breadth)
circle_area = math.pi * radius ** 2
circle_circumference = 2 * math.pi * radius
print("Area of the rectangle:", rectangle_area)
print("Perimeter of the rectangle:", rectangle_perimeter)
print("Area of the circle:", circle_area)
print("Circumference of the circle:", circle_circumference)

"""

#4)Two numbers are input through the keyboard into two locations C and D.
# Write a program to interchange the contents of C and D.
"""
C = input("Enter the value of C: ")
D = input("Enter the value of D: ")
C, D = D, C
print("\nAfter swapping:")
print("C =", C)
print("D =", D)
"""

#5)In a town, the percentage of men is 52. The percentage of total literacy is 48. If total percentage of literate men is 35 of the total population,
#write a program to find the total number of illiterate men and women if the population of the town is 80,000.

"""
total_population = 80000
percentage_men = 52
percentage_literacy = 48
percentage_literate_men = 35
total_men = (percentage_men / 100) * total_population
total_literate_men = (percentage_literate_men / 100) * total_population
total_illiterate_men = total_men - total_literate_men
total_women = total_population - total_men
total_literate_women = (percentage_literacy / 100) * total_population - total_literate_men
total_illiterate_women = total_women - total_literate_women

print("Total number of illiterate men:", total_illiterate_men)
print("Total number of illiterate women:", total_illiterate_women)

"""
#6)While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 10.
# If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.

"""
quantity = int(input("Enter the quantity purchased: "))
price_per_item = float(input("Enter the price per item: "))
if quantity > 10:
    discount = 0.1  # 10% discount
else:
    discount = 0

total_expenses = quantity * price_per_item * (1 - discount)

print("Total expenses:", total_expenses)

"""

#7) If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss. 
#Also determine how much profit he made or loss he incurred.

"""
cost_price = float(input("Enter the cost price of the item: "))
selling_price = float(input("Enter the selling price of the item: "))

profit_or_loss = selling_price - cost_price

if profit_or_loss > 0:
    print("The seller has made a profit of", profit_or_loss)
elif profit_or_loss < 0:
    print("The seller has incurred a loss of", -profit_or_loss)
else:
    print("The seller has neither made a profit nor incurred a loss.")

    """

#8)Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is 
#greater than its perimeter. For example, the area of the rectangle with length = 5 and breadth = 4
# is greater than its perimeter

"""
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
if area > perimeter:
    print("The area of the rectangle is greater than its perimeter.")
else:
    print("The area of the rectangle is not greater than its perimeter.")
"""

#9).A five-digit number is entered through the keyboard. Write a program to obtain the reversed number and 
#to determine whether the original and reversed numbers are equal or not.

"""
def main():
    num = input("Enter a five-digit number: ")
    reversed_num = num[::-1]
    
    print("Reversed number:", reversed_num)
    if num == reversed_num:
        print("The original and reversed numbers are equal.")
    else:
        print("The original and reversed numbers are not equal.")

main()
"""

#10) Write a program to check whether a triangle is valid or not, when the three angles of the triangle are
#entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

"""
a = int(input("Enter the first angle (a): "))
b = int(input("Enter the second angle (b): "))
c = int(input("Enter the third angle (c): "))

total = a + b + c

if total == 180:
    print("The sum of the three angles is equal to 180, so it is a valid triangle.")
else:
    print("The sum of the three angles is not equal to 180, so it is not a valid triangle.")

"""

#11)Write a program to find the given number is perfect number

"""
num = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")

"""

#12)Write a program to find the Fibonacci Series of the given number.

"""
n = int(input("Enter a number: "))

fib_series = [0, 1]  

while len(fib_series) < n:
    next_term = fib_series[-1] + fib_series[-2]
    fib_series.append(next_term)

print(fib_series)

"""

#13)Write a Python program to check a list is empty or not

"""
l = []  

if len(l) == 0:
    print("The list is empty.")
else:
    print("The list is not empty.")
"""

#14)Write a program to print the Armstrong numbers between 100 to 999.

"""
print("Armstrong numbers between 100 and 999:")
for num in range(100, 1000):
   
    digit_1 = num // 100
    digit_2 = (num % 100) // 10
    digit_3 = num % 10

    if num == (digit_1 ** 3 + digit_2 ** 3 + digit_3 ** 3):
        print(num)
"""

#15)A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input
# through the keyboard in hundreds, find the total number of currency notes of each denomination the cashier
# will have to give to the withdrawer

"""
amount = int(input("Enter the amount to be withdrawn in hundreds: "))

num_hundreds = 0
num_fifties = 0
num_tens = 0
remaining_amount = 0

if amount >= 100:
    num_hundreds = amount // 100
    remaining_amount = amount - (num_hundreds * 100)

    if remaining_amount >= 50:
        num_fifties = remaining_amount // 50
        remaining_amount = remaining_amount - (num_fifties * 50)
    if remaining_amount >= 10:
        num_tens = remaining_amount // 10
        remaining_amount = remaining_amount - (num_tens * 10)

print("Number of Hundreds:", num_hundreds, "Number of Fifties:", num_fifties, "Number of Tens:", num_tens)
"""

#16)If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary and DA = 90% of basic salary.
# If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. 
#If the employee's salary is input through the keyboard write a program to find his gross salary

"""
salary = int(input("Enter Employee's Salary: "))

if salary < 1500:
    hra = salary / 10
    da = (salary / 100) * 90
else:
    hra = 500
    da = (salary / 100) * 98

gross_salary = salary + hra + da
print("Gross Salary:", gross_salary)
"""

#17)If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine 
#the youngest of the three.

"""
ram_age = int(input("Enter the age of Ram: "))
shyam_age = int(input("Enter the age of Shyam: "))
ajay_age = int(input("Enter the age of Ajay: "))

if ram_age < shyam_age and ram_age < ajay_age:
    print("Ram is the youngest of the three")
elif shyam_age < ram_age and shyam_age < ajay_age:
    print("Shyam is the youngest of the three")
else:
    print("Ajay is the youngest of the three")
"""

#18)Any year is entered through the keyboard, write a program to determine whether the year is leap or not.
# Use the logical operators && and ||.

"""
year = int(input("Enter a year: "))

is_leap_year = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

if is_leap_year:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
"""

#19)A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, 
#for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 days
# your membership will be cancelled. Write a program to accept the number of days the member is late to return 
#the book and display the fine or the appropriate message.

"""
days_late = int(input("Enter the number of days the book is late: "))

if days_late <= 0:
    print("No fine. Thank you for returning the book on time!")
elif days_late <= 5:
    fine = days_late * 0.5  # 50 paise per day
    print("Fine for {} days late: {} rupees.".format(days_late, fine))
elif days_late <= 10:
    fine = (5 * 0.5) + ((days_late - 5) * 1)  # 50 paise for first 5 days, 1 rupee per day after
    print("Fine for {} days late: {} rupees.".format(days_late, fine))
elif days_late <= 30:
    fine = (5 * 0.5) + (5 * 1) + ((days_late - 10) * 5)  # 50 paise for first 5 days, 1 rupee for next 5 days, 5 rupees per day after
    print("Fine for {} days late: {} rupees.".format(days_late, fine))
else:
    print("Your membership will be cancelled. You have returned the book after 30 days.")
"""

#20)In a company, worker efficiency is determined on the basis of the time required for a worker to complete a 
#particular job. If the time taken by the worker is between 2 – 3 hours, then the worker is said to be highly 
#efficient. If the time required by the worker is between 3 – 4 hours, then the worker is ordered to improve
# speed. If the time taken is between 4 – 5 hours, the worker is given training to improve his speed, 
#and if the time taken by the worker is more than 5 hours, then the worker has to leave the company.
# If the time taken by the worker is input through the keyboard, find the efficiency of the worker.

"""
time_taken = float(input("Enter the time taken by the worker to complete the job (in hours): "))

if time_taken >= 2 and time_taken < 3:
    print("Worker is highly efficient.")
elif time_taken >= 3 and time_taken < 4:
    print("Worker needs to improve speed.")
elif time_taken >= 4 and time_taken < 5:
    print("Worker needs training to improve speed.")
elif time_taken >= 5:
    print("Worker has to leave the company.")
else:
    print("Invalid input. Please enter a valid time.")

"""





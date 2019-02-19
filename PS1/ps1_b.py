# -*- coding: utf-8 -*-
"""
MIT: intro to computer science and programming in Python
PS1_c
Created on Wed Dec 12 21:17:02 2018
@author: Kiooola
"""

total_cost = float(input("Enter the cost of your dream home:"))
annual_salary =  float(input("Enter your starting annual salary:"))
portion_saved= float(input("Enter the portion of salary to be saved:"))
semi_annual_raise= float(input("Enter your semiannual raise"))
portion_down_payment = 0.25*total_cost
current_savings = 0
r = 0.04
month_count=0

while current_savings< portion_down_payment:
    current_savings += annual_salary* portion_saved /12 + current_savings*r/12
    month_count+=1
    if month_count%6 == 0:
        annual_salary *= (1+ semi_annual_raise)


print ( month_count, " months or ", int(month_count/12) , "Years and" , month_count%12 , "months")
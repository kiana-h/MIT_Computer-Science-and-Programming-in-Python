# -*- coding: utf-8 -*-
"""
MIT: intro to computer science and programming in Python
PS1_c
Created on Wed Dec 12 21:17:02 2018
@author: Kiooola
"""


######################
#approximation method#
######################

#total_cost = 1000000
#annual_salary =  float(input("Enter your starting annual salary: "))
#semi_annual_raise= 0.07
#years = 3
#
#portion_down_payment = 0.25*total_cost
#portion_saved= 0
#r = 0.04
#current_savings = 0
#iterations = 0
#
## increments saving rate until it meets required down payment
#while  portion_down_payment - current_savings >= 100 :
#    current_savings = 0
##adds salary in 6 month increments to get the total
#    for i in range (years*2):
#        current_savings += (annual_salary/2)*portion_saved*((1+semi_annual_raise)**i)*(1+r/2)
#    portion_saved += .01
#    iterations +=1
#    if portion_saved>1:
#        break
#    
#print ("iterations: ",iterations)  
#if portion_saved > 1:
#    print ("impossible")
#else:
#    print ("approximate saving rate: ", round(portion_saved, 2))



######################
#bisection method#
######################

total_cost = 1000000
start_salary =  float(input("Enter your starting annual salary: "))
semi_annual_raise= 0.07
years = 3

portion_down_payment = 0.25*total_cost
r = 0.04
current_savings = 0
iterations = 0

max_saving = 100.0
min_saving = 0.0
test_saving = int(max_saving+min_saving)/2
possible = False


# increments saving rate until it meets required down payment
while max_saving-min_saving > .01 :
    annual_salary = start_salary
#adds salary in 6 month increments to get the total
    for i in range (1,years*12+1):
        current_savings += (annual_salary*test_saving/100+current_savings*r)/12
        if i%6 == 0:
            annual_salary+= annual_salary*semi_annual_raise
    if abs(portion_down_payment - current_savings) <= 100:
        min_saving = max_saving
        possible = True
        break
    elif portion_down_payment > current_savings:
        min_saving = test_saving
    else:
        max_saving = test_saving
        
    iterations +=1
    current_savings = 0
    test_saving = (max_saving+min_saving)/2
    
    
print ("iterations: ",iterations)  
if not possible:
    print ("impossible")
else:
    print ("approximate saving rate: ", round(test_saving, 4))
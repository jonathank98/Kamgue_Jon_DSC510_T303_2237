#DSC 510
#Week 3
#Programming Assignment Week 3
#Jonathan Kamgue
#6/22/2023
# This program is written by Jonathan Kamgue. It uses user input to calculate the cost of installation for a fiber optical cable

#Change Control log
#Change Made: Added code to calculate the cost of installation based on different cable length values
#Author: Jonathan Kamgue
#Date moved to production: 6/22/2022

print("***** Hello Customer and welcome to your fiber cost installation calculator ***** \n")  #welcome message

compname = input("Please enter your company's name: ")  #COMPANY NAME

fiberlength = input("Please enter the length of fiber cable you will need: \n ") #GETTING FEET LENGTH FROM CUSTOMER

fiberlength = int(fiberlength) #Converting feet length from string to integer

if fiberlength > 100:                       #if the feet length is more than 100 feet
    cost = fiberlength * 0.80

if fiberlength > 250:                       #if the feet length is more than 250 feet
    cost = fiberlength * 0.70

if fiberlength > 500:                       #if the feet length is more than 500 feet
    cost = fiberlength * 0.50

if fiberlength < 100:                       #if the feet length is less than 100 feet
    cost = fiberlength * 0.87

totalcost = cost                            #calculating total cost based on cable feet length value inputed above


print ("Here is your receipt! \n")          #this line and the following 3 lines is to print the receipt according to the customer name and the cost calculated based on the number of cable length entered.

print (compname)
print ("The number of cable feet to be installed is: ", fiberlength)
print ("The total cost of installation is: $", totalcost)









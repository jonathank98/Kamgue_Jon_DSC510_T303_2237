#DSC 510
#Week 2
#Programming Assignment Week 2
#Jonathan Kamgue
#6/12/2023
# This program is written by Jonathan Kamgue. It uses user input to calculate the cost of installation for a fiber optical cable

#Change Control log
#Change Made: Added a newline character to lines 10, 12. and 18)
#Author: Jonathan Kamgue
#Date moved to production: 6/18/2022
print("Hello and welcome to your fiber cost installation calculator \n")
compname = input("Please enter your company's name: ")  #COMPANY NAME
fiberprice = input("Please enter the length of fiber cable you will need: \n ") #GETTING FEET LENGTH FROM CUSTOMER
fiberprice = int(fiberprice) #Converting feet length from string to inte
cost = fiberprice * 0.87
totalcost = cost


print ("Here is your receipt! \n")

print (compname)
print ("The number of cable feet to be installed is: ", fiberprice)
print ("The total cost of installation is: $", totalcost)









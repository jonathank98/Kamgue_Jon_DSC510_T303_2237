# This program is written by Jonathan Kamgue. It uses user input to calculate the cost of installation for a fiber optical cable

print("Hello and welcome to your fiber cost installation calculator")
compname = input("Please enter your company's name: ")  #COMPANY NAME
fiberprice = input("Please enter the length of fiber cable you will need: ") #GETTING FEET LENGTH FROM CUSTOMER
fiberprice = int(fiberprice) #Converting feet length from string to inte
cost = fiberprice * 0.87
totalcost = cost + (0.0825 * cost)
print(fiberprice)

print ("Here is your receipt!")

print (compname)
print ("The number of cable feet to be installed is: ", fiberprice)
print ("The cost of installation is: $", cost)
print ("The total cost of installation, with taxes included (8.25%) is: $ ", totalcost)



#    print(cost)





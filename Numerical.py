#Mason Hamilton & Dylan Nasser
#CST-305-3:20
#Professor Ricardo Citro
#4/26/2020
#Project 8 Numerical Integration
#Our grouped worked with Tanner Williams and Jared group

#get the users input for all 3 variables
part = int(input("Enter the number of partitions for the Riemann sum: "))
low = float(input("Enter the Lower bound value: "))
up = float(input("Enter the Upper bound value: "))

#out numerical intergration function
def Numeric():
    #creating out first return value
    def f(x):
        return 1.6325*x + 444.5

    value = 0
    #adjusting our width for the upper and lower bounds
    width = (up - low) / part
    #for loop to find the end value of iteration
    for i in range(1 , part + 1):
        value += f(low + (i*width)) * width
    return value

#printing out our finally numeric intergration
print("Output is: ", Numeric())

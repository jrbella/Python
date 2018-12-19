#Tools
#Cloud 9
#Visual Studio Code
#pylinter
#oracle box Free stuff
#Python 2.7.12 or python 3.7

#ONEDRIVE, c:\user\documents  <---- one drive

#application
    # we the user enter a (n) number of coins.  Coins to be distinct
    #calculate the total amount of money we currently have from the change
    

def main():
    print("Hello Welcome to our coin calculator!")
    print
    print("Please enter the count of each coin type.")
    quarters = (input("Quarters :"))
    dimes = (input("dimes :"))
    nickels = (input("nickels :"))
    pennies = (input("pennies :"))
    
    #Equation
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print
    print "The total value of your change is: $", total
    #print(pennies)
    #print(nickels)
    #print(dimes)
    #print(quarters)
    #162 + 770 + 2100 + 10000
main()
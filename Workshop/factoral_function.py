#accumulation algorithm

#create a function that finds any factorial on (1)
# 1*2*3*4*5   = !(5)

def main():
    print "Welcome to the factorial function"
    n = input("Please enter a number :")
    fact = 1
    #equation for the range
    equation = n + 1
    for factor in range(1, equation):
        fact = fact * factor
    print " The factorial of" , n , "is", fact
    
    

main()

#systems
#subsystems
#components
#units



# n = 6    [1,2,3,4,5,6] 
# first loop fact = 1   factor = 1
# second loop fact = 1  factor = 2
# third loop fact = 2   factor = 3
# fourth loop fact = 6   factor = 4
# fifth loop fact = 24  factor = 5
#sixth loop fact = 120 factor = 6
#final loop fact = 720 factor ends; 
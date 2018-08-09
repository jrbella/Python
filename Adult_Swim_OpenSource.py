#Linear Complexity
#Mowing the lawn can be thought of as a problem with linear complexity. Mowing an area that is double the size of the original takes twice as long.

# reusable roots


#find perfect root function

#find imperfect root function

#test functions

x = 17

def find_sqr_root(x):
    if(x < 0):
        print x, ' is a negative number'
        return
    else:
        ans = 0
        print ans
        while ans * ans < x:
            ans = ans + 1
            print ans
            if ans * ans != x:
                print x, 'is not a perfect square'
            else:
                print x, 'is a perfect square'
          
        
    
find_sqr_root(x)
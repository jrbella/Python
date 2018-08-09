import math
#Linear Complexity
#find perfect root function  ---completed
#find imperfect root function  --completed
#find the square root of x --completed
x = 970225

def find_p_sqr_root(x):
    ans = 0
    if  x >= 0:
        while ans * ans < x:
            ans = ans + 1
        if ans * ans != x:
            print x, ' is not a perfect square'
        else:
            print ans
    else:
        print x, 'is a negative number'
          
def find_sqr_root(x):
    ans = 0
    if x >= 0:
        while ans * ans < x:
            ans = ans + 1
        #ans will always be the higher square
        #ans-1 will give us the lower square in which
        #the root of x exist
        ans = ans - 1
        x = float(x)
        ans = float(ans)
        for something in range(5):
            #our average root
            result = ((x/ans) + ans)/2
            ans = result
        print ans
        return ans

def test_roots(x):
    #gives us the square root
    result = find_sqr_root(x)
    #this mulitplies the square root by itself
    ans = result * result
    #should give x back
    if(ans == x):
        print 'test has passed'
    else:
        print 'test has failed'
        
test_roots(x)
#call the perfect square function on our test ON FRIDAY
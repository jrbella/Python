import math

nbr = 12


def test_p_square(x):
    if(x < 0):
        print x, 'is a negative number'
        return x
    else:
        ans = 0
        while ans * ans < x:
            ans = ans + 1
        if(ans * ans != x):
            x = float(x)
            ans = float(ans-1)
            count = 0
            while count < ans:
                root1 = (x/ans)
                root = ((ans + root1)/2)
                count = count + 1
            print x, ' has a square root of {}'.format(root)
        else:
            root = ans
            print x, 'is a perfect square'
    return root   
        



def test_result(x):
    if(x < 0 ):
        return
    else:
        ans = x * x
        ans = math.floor(ans)
        print(ans, 'is the test result')

test_result(test_p_square(nbr))

    
    
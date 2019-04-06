def is_square(n):    
    y=n**(1/2)
    if n > -1 and  y%1==0 :

            return(True)
        
    else:
        return( False)



import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

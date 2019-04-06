#not working
def count_change(money,counters,targetsum=0):
    count=0
    new_list=[]
    if targetsum==0:
        return (1)
    if targetsum < 0 or money <=0:
        return( 0)
    print( count_change(money-1,counters,targetsum)+count_change(money,counters,targetsum-coins[money-1]))

        
count_change(4,[1,2])


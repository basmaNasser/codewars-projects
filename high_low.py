
def high_and_low(numbers):
    
      maxnum= max([int(x) for x in numbers.split()])
      minnum= min([int(x) for x in numbers.split()])
      print (str(maxnum)+" "+str(minnum))

     # x=map(int,numbers.split())
     # print ()


      
high_and_low("4 5 29 6 54 4 0 -214 542 -64 1 -3 -6")

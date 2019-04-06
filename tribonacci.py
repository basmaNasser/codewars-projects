def tribonacci(signature, n):
    new=[]
    if n ==0:
        new =[]
    if n-len(signature) <0:
      for i in range(0,n):    
        new_val= signature[i]
        new.append(new_val)
    else:
        new=signature

        for i in range(0,n-len(new)):    
            new_val= new[i]+new[i+1]+new[i+2]
            new.append(new_val)
    return(new)
        
    

def tribonacci(signature,n):
    res = signature
    while len(res) < n:
        res.append(sum(res[-3:]))
    return res[:n]        
    

def tribonacci(signature, n):
        new=signature[:n]

        for i in range(n-len(new)):    
            new_val= sum(new[-3:])
            new.append(new_val)
        return(new)

tribonacci([1,1,1], 1)
        
    

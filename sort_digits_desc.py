def Descending_Order(num):
  list_value=list(str(num))
  reveresed= sorted(list_value,reverse = True)
  final=''
  for i,val in enumerate(reveresed):
      final = final+val
  return(final)

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

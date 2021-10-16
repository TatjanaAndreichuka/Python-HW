def ad(a,b):
   return(a+b)
   
def subtract(a, b,):
    return (a - b)
    
def multiple(a,b):
    return (a*b)
    
def div(a,b):
    return (a/b)
  
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
operator = int(input('Choose 1 for Add; 2 for Subtract; 3 for Multiple; 4 for Divide'))

if operator==1:
    print(f'Result is {ad(a,b)}')
elif operator==2:
    print(f'Result is {subtract(a,b)}')
elif operator==3:
    print(f'Result is {multiple(a,b)}')
elif operator==4:
    print(f'Result is {div(a,b)}')
else:
    print('Choose option 1 ,2 , 3 or 4 ')
    
    

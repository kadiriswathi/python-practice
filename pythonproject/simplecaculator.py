def add(x,y):
         print(' The sum of x and y')
         return x+y
def sub(x,y):
         print('The  diffrence between the x and y')
         return x-y     
def mul(x,y):
        print('the mutilpication of x and y') 
        return x*y
def divi(x,y):
        print('the division of x and y')
        if y==0:
          return "error: division  by zero is not allowed" 
        return x / y     
def main():
         print("Welcome to the simple calculator!")
         print("Available operations are:+,-,*,/")
         print("Type 'exit' to quit the program. \n")
         print("Type'exit' to quit the program. \n")
         while True:
          oper=input("enter the operations (+,-,*,/):").strip()
          if oper.lower()=='exit':
               print('bye')
               break
          if oper not in ['+','-','*','/']:
               print('Invalid operation please try again.')
          try :
               num1=float("enter the first number:")
               num2=float("enter the second number:")
          except:
               print("invalid number please enter the numeric numbers.")
               continue    
          if oper=='+':
               res=add(num1,num2)
          elif oper=='-':
               res=sub(num1,num2)
          elif oper=='*':
               res=mul(num1,num2)   
          elif oper=='/':
               res=divi(num1,num2)
          print(res)
          var=input("Do you want continue with another opeations?(yes/no):").strip().lower()
          if var!='yes':
                print('good bye') 
                break
if __name__==main:
   main()
                       
                   
          
     
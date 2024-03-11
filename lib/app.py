import ipdb

print("Hello Flatiron! Class is in session!")

def add(num1, num2):
  if(type(num1) in [int, float]) and (type(num2) in [int, float]):
      return num1 + num2
  else:
     raise Exception
  
def subtract(num1, num2):
   if(type(num1) in [int, float]) and (type(num2) in [int, float]):
      return num1 - num2
   else:
      raise Exception
   
def multiply(num1, num2):
   if(type(num1) in [int, float]) and (type(num2) in [int, float]):
      return num1 * num2
   else:
      raise Exception
   
def divide(num1, num2):
   if(type(num1) in [int, float]) and (type(num2) in [int, float]) and (num2 != 0):
      return num1 / num2
   else:
      raise Exception
   
def calculator(operator, num1, num2):
   if(operator == '+'):
      return add(num1, num2)
   elif(operator == '-'):
      return subtract(num1, num2)
   elif(operator == '*'):
      return multiply(num1, num2)
   elif(operator == '/'):
      return divide(num1, num2)
   else:
      raise Exception
   

def print_greeting_loop(greeting):
   for char in greeting:
      print(char)

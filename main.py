
#def getFactorial(x):
 #factorial= input("enter your number here")
 #for i in range(1, z+1):
   #factorial= factorial * i
 #return getFactorial(factorial)


#def div(numb):
  #number=input(int("enter your number here"))
  #for i in range(1,):
  #numb= number % i
  #print(number[i]) 

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("result")

def find_divisors(n):
    divisors = [input("put your number here")]
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
  
  
def reverse_string(input_string):
    reversed_string = ''
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string

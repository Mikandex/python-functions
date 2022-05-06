'''
@author ifeanyi Onovo
email: ifeanyionovo38@gmail.com

prime number checker
what's prime number: It is a number that can be divided by 1 and itself
example 1, 2, 3.
A none prime number can be divided by 1, one or more numbers then itself
example 4, 6 8
'''


#declare function to check if the number is prime number or not
def prime_number(number):
    is_prime = True  # set a boolean variable 

    for i in range(2,number): #loop through the numbers
     if number % i == 0:
      is_prime = False
    if is_prime == True :
        print('This is a prime number')
    else:
        print('this is not a prime number')


keep_program_running = True
while keep_program_running:
 number = int(input('check for prime number : ')) 
 prime = prime_number(number)
 print(prime)
 
 repeat = input("Do you want to check for another number? type Yes or No: ")
 if repeat == 'yes' or repeat == "Yes" or repeat == 'YES':
     keep_program_running =True
     print('Thumps!!!! =):')
 else:
     keep_program_running = False
     print('Thank you for using our function ')
     print('Thumps!!! =):')
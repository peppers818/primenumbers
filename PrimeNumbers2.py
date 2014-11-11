# Joseph Pannizzo
# Edited 11/5/2014 Samantha Holloway
# 11/3/2014
# Python Prime Numbers

input = int(input("Enter a number: "))

# prime number solver function
def prime(input):
	for num in range(0, input+1):
		if num > 1:
			checkprime(num)
			

# function that checks for prime number
def checkprime(num):
	#Reduced the # of factors looped through
	#Composite Numbers have a factor <= their sqrt
	for i in range(2, int(num ** 0.5)+1):
		if(num % i) == 0:
			break
	else:
		print(num)
	
# call prime number solver function				
prime(input)

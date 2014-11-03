# Joseph Pannizzo
# 11/3/2014
# Python Prime Numbers

input = int(input("Enter a number: "))

# prime number solver function
def prime(input):
	for num in range(0,input + 1):
		if num > 1:
			for i in range(2,num):
				if (num % i) == 0:
					break
			else:
				print(num)

# call prime number solver function				
prime(input)
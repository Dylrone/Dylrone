Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
	celsius = int(input("Enter a temperature in Celsius: "))
	fahrenheit = (9 / 5) * celsius + 32
	print("That is equivalent to", fahrenheit, "degrees Fahrenheit")
main()
SyntaxError: invalid syntax
>>> def main():
	# Prompt the user to provide an input temperature in Celsius
	celsius = int(input("Enter a temperature in Celsius: "))
	# Process the input, converting it to Fahrenheit
	fahrenheit = (9 / 5) * celsius + 32
	# Print the output for the user
	print("That is equivalent to", fahrenheit, "degrees Fahrenheit")
main()	

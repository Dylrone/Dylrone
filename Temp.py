def main():
	# Prompt the user to provide an input temperature in Celsius
	celsius = int(input("Enter a temperature in Celsius: "))
	# Process the input, converting it to Fahrenheit
	fahrenheit = (9 / 5) * celsius + 32
	# Print the output for the user
	print("That is equivalent to", fahrenheit, "degrees Fahrenheit")
main()	

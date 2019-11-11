# Unicode Converter
# It turns Unicode numbers into a string

def unicod():
    print('-'*70)
    print("This program converts a seuence of Unicode numbers into")
    print("the string of text that it represents.\n")
    nums = input("Please input the numbers you wish to convert: ")
    message=""
    for i in nums.split():
        yoo = int(i)
        message = message + chr(yoo)
    print("\nThe decode message is:", message)
unicod()

# month.py
# A program to print the abbreviation of a month, given its number
def mont():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    numb = int(input("Input the month number you wish for: "))

    
    print("Your month is",months[numb-1])
mont()


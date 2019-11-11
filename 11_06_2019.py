# have an input function looping that can be ended on command,
# All the numbers that are inputed are put into a list
# Once the input loop is ended, all the numbers that were put into the list are
# added together and divided by the length of the list

 # Pseudocode for averaging
 
# input count of the numbers
# initialize sum to 0
# loop n times
    # input a number, x
    # add x to sum
# output average as sum/n

def main():
    n = int(input("How many numbers? "))
    SUM = 0
    for i in range(0,n):
        x = float(input("Input a number: "))
        SUM = SUM + x
    print(SUM/n)


def main2():
    x = "y"
    total = 0
    totalnumb = 0
    while x == "y":
        y = float(input("\nEnter a number: "))
        total = total + y
        totalnumb = totalnumb+1
        x = input("\nDo you wish to continue adding?(y/n)")
    print("Your average is",round(total/totalnumb,2))


    
    
            

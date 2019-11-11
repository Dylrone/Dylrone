def main():
    filename = input("What file are the numbers in? ")
    infile = open(filename,'r')
    total = 0
    count = 0
    line = ifile.readline()
    while line != "":
        total = total + float(line)
        count = count + 1
        line = infile.readline()
    print(total/count)
main()

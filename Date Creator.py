# The Power Of months

def monthtime():
    allmonths = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
    inputo = input("Please input the date in mm/dd/yyyy: ")
    day = str(int(inputo[3:5])) + ","
    month = int(inputo[0:2])
    findmonth = allmonths[month-1]
    year = inputo[6:]
    print(findmonth, day, year)
monthtime()

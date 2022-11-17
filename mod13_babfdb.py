import datetime
while(True):
    try:
        stockName = str(input("What is the stock symbol for the company you would like to visualize?: "))
        if((len(stockName) > 7 ) or (stockName.isalnum() == False) or (stockName.isupper() == False)):
            raise Exception
        else:
            break

    except Exception:
        print("Input Error")
    except ValueError:
        print("Input Error")
        
while(True):
    try:
        timeSeries = int(input("Enter time series option (1, 2, 3, 4): "))
    except ValueError:
        print("The value you entered is invalid. Only numerical values are valid. \n")
    if(timeSeries > 4 or timeSeries < 0):
       print("Please Enter a number between 1 and 4 for selection \n")
    else:
        break

while(True):
    try:
        chartType = int(input("Enter the chart type you want: (Bar (1), Line (2)): "))
    except ValueError:
        print("The value you entered is invalid. Only numerical values are valid. \n")
    if(chartType > 2 or chartType < 0):
        print("Please Enter 1 or 2 for selection \n")
    else:
        break

while(True):
    try:
        date1 = input("Enter the start Date (YYYY-MM-DD): ")
        date2 = input("Enter the end Date (YYYY-MM-DD): ")

        broke1 = date1.split('-')
        broke2 = date2.split('-')

        DATE1 = datetime.date(int(broke1[0]),int(broke1[1]),int(broke1[2]))
        DATE2 = datetime.date(int(broke2[0]),int(broke2[1]),int(broke2[2]))
        dateparams = [[date1,date2],[int(broke1[0]),int(broke1[1]),int(broke1[2])],[int(broke2[0]),int(broke2[1]),int(broke2[2])]]
        if(DATE2 < DATE1):
            print("Dates entered incorrectly")
        else:
                #print(dateparams)
                #print(date1+date2)
            break
    except ValueError:
        print("Dates Entered Incorrectly, Make sure the Format is correct.")

import datetime
start_date = "14/10/22"
date_1 = datetime.datetime.strptime(start_date, "%d/%m/%y")

end_date = date_1 + datetime.timedelta(days=11)

def nextDayInputDate(endDate):

    end_nextDay = datetime.datetime.strptime(endDate, "%d/%m/%y")
    
    end_nextDay += datetime.timedelta(days=1)

    end_nextDay = str(end_nextDay.date())
    
    return end_nextDay

print(type(nextDayInputDate(start_date)))
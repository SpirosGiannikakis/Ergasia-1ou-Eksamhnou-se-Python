import datetime

weekday= int(datetime.date.today().isoweekday())
monthday= int(datetime.date.today().isoformat().split("-")[2])
year= int(datetime.date.today().isoformat().split("-")[0])
times= 0
for i in range (1,11):
	for j in range (1, 13):
		if int(datetime.date(year+i, j, monthday).isoweekday())== weekday:
			times+=1
print ("In the next 10 years it will be ",times," times with the same weekday and monthday as today")
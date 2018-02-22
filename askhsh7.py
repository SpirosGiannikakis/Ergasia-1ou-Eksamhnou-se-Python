import datetime

#xrhsh methodwn tou module datetime gia diaxwrismo kai euresh ths shmerinhs hmeras
year= int(datetime.date.today().isoformat().split('-')[0])
month= int(datetime.date.today().isoformat().split('-')[2])
week= int(datetime.date.today().isoweekday())


days= 0
#elegxos ths meras gia ton kathe epomeno mhna gia ta epomena 10 xronia
for i in range (1,11):
	for j in range (1, 13):
		if int(datetime.date(year+i, j, month).isoweekday())== week:
			days+=1

#Test			
print('There will be', days, 'days in the next 10 years that will have the same weekday and monthday value as of today')

import urllib.request
import json
import datetime

current_date = datetime.datetime.now()

NUMBERS = []
pi = 1
#Diavasma arithmwn apto plhktrologio kai prosthikh tous se pinaka
while pi < 11:
	ar = int(input('Please insert a number: '))
	if ar > 80:
		print('Please input a number between 1 and 80')
		continue
	else:
		pi += 1
		NUMBERS.append(int(ar))
		
	
	
#tupwsh tou pinaka
print(NUMBERS[:])
print()

d = datetime.datetime.today().day

#sunarthsh pou sugkrinei tous arithmous tou xrhsth me autous twn apotelesmatwn 
def compare(num1, num2):
	succ = 0
	for i in num1:
		if i in num2:
			succ += 1
	return succ


nums_succ = []
days = []
#enalagh tou url dhladh twn hmerwn gia kathe mera apo thn arxh tou mhna mexri datetime.today
for i in range(0, int(d-1)):
	current_date = current_date - datetime.timedelta(days=1)
	dayy = current_date.strftime("%d-%m-%Y")
	days.append(dayy)
	api = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json' % dayy
	request = urllib.request.Request(api)
	response = urllib.request.urlopen(request)
	json_data = response.read()
	json_data = json.loads(json_data)
	results = json_data['draws']['draw']
	succeses = []
	print(dayy)
	#sugkrish twn arithmwn
	for k in results:
		res = k['results']
		succeses.append(compare(NUMBERS, res))
	ar = 0
	#metrhsh epituxiwn
	for j in range(len(results)):
			
		if succeses[j] > 4:
			ar += 1

	nums_succ.append(ar)
	print('apotelesmata', dayy)
	#tupwsh olwn twn results apto api gia kathe mera
	for o in range(len(results)):
		print(json_data['draws']['draw'][o]['results'])
		print()

max_succ = max(nums_succ)
c = nums_succ.index(max(nums_succ))

#tupwsh telikwn apotelesmatwn
print('The highest number of succeses you had are: ', max_succ,'\n', 'And the day you had them would have been: ', days[c])
print('And your winrate is:', (len(results)/max_succ), '%')
import time #import time

dict ={} #creates an empty dictionary

while  True:

	#Remider menu
	print('\t \t [DSN B-REMINDER APPLICATION]')
	print()
	print('loading...')
	time.sleep(4) #delays option for 4secs
	print('1. View Birthday')
	print('2. Add to Friends Birthday archive')
	print('3. Quit')

	option = int(input('Enter number option (1-3)'))
	if option ==1:

		if len(dict.keys()) == 0:
			print('Nothing to show, kindly add an event')
		else:
			Name = input('Enter name to search for Birthday')
			Birthday = dict.get(Name, 'No data found')
			print(Birthday)

	elif option == 2:
		Name = input('Enter Your Friends Name')
		Date = input('Enter Birthday (e.g dd/mm/year)')
		dict[Name] = Date
		print('\n Birthday Successfully added')

	elif option == 3:
		break

	else:
		print('Not a valid option')
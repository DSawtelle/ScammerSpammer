"""	Author:	 Daniel J. Sawtelle
***	Purpose: Bombard the given URL with randomized form return data
***
***	Source: https://www.youtube.com/watch?v=UtNYzv8gLbs
"""
import os
import random
import string
import json
import time
import requests

""" Function - Return a string object of a date formatted as specified
***		start:	First date possible to select
***		end:	Last date possible to select
***		format:	Structure of the date string being returned
***		prop:	Proportion of the distance to jump into the specified date range
***
*** 	Source: https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
"""
def str_time_prop(start, end, format, prop):
    #Retrieve the start and end dates as a time object
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    #Evaluate the proportion of the date range to jump to
    ptime = stime + prop * (etime - stime)

    #Return a string object of the date tracked
    return time.strftime(format, time.localtime(ptime))

#Seed the random instance for generating data for the bombardment
random.seed = (os.urandom(1024))
#URL of the address to spam with data
url = 'AddressOfScammerGoesHere'

"""---------------- Main Function : Bombard the URL with randomized data ----------------"""
#Get an object of the list of names (first and last), streets, and companies to use for data spamming
fNames = json.loads(open('FirstNames.json').read())
lNames = json.loads(open('LastNames.json').read())
street = json.loads(open('StreetNames.json').read())
company = json.loads(open('CompanyNames.json').read())
country = json.loads(open('USVariations.json').read())
na = json.loads(open('NAVariations.json').read())

#Track the number of data bombardments done during this script call
dataCount = 1
while True:
	#Generate a random city/state pairing
	state = random.choice(json.loads(open('StateAbbreviations.json').read()))
	city = random.choice(json.loads(open('StateCities\\'+ state + 'Cities.json').read()))
	
	#Person Information
	PName = random.choice(fNames) + ' ' + random.choice(lNames)
	PAppartmentNumber = str(random.randint(1, 999))
	if random.choice([True, False]):
		PAppartmentNumber =  random.choice(na)
	PAddress = str(random.randint(1, 10000)) + ' ' + random.choice(street)
	PCity = city
	PState = state
	PZip = ''.join(random.choice(string.digits) for i in range(5))
	PCountry = random.choice(country)
	PPhoneNumber = '(' + ''.join(random.choice(string.digits) for i in range(3)) + ') ' + ''.join(random.choice(string.digits) for i in range(3)) + '-' + ''.join(random.choice(string.digits) for i in range(4))
	
	#Employer Information
	EName = random.choice(company)
	EEIN = ''.join(random.choice(string.digits) for i in range(2))
	if random.choice([True, False]):
		EEIN = ''.join(random.choice(string.ascii_letters)) + EEIN
	if random.choice([True, False]):
		EEIN = EEIN + '-'
	EEIN = EEIN + ''.join(random.choice(string.digits) for i in range(7))
	if random.choice([True, False]):
		EEIN = EEIN + ''.join(random.choice(string.digits))
	EAddress = ''.join(random.choice(string.digits) for i in range(4)) + ' ' + random.choice(street)
	ECity = city
	EState = state
	EZip = PZip[:3] + ''.join(random.choice(string.digits) for i in range(2))
	ECountry = random.choice(country)
	EPhoneNumber = '(' + ''.join(random.choice(string.digits) for i in range(3)) + ') ' + ''.join(random.choice(string.digits) for i in range(3)) + '-' + ''.join(random.choice(string.digits) for i in range(4))

	#Government/Financial Information
	EDOB = str_time_prop('01/01/1970', '12/31/2011', '%m/%d/%Y', random.random())
	ESSN = ''.join(random.choice(string.digits) for i in range(3)) + '-' + ''.join(random.choice(string.digits) for i in range(2)) + '-' +''.join(random.choice(string.digits) for i in range(4))
	EDLNumber = 'D' + ''.join(random.choice(string.digits) for i in range(8))
	EState = state
	EDLIssueDate = str_time_prop('01/01/1970', '12/31/1970', '%m/%d/%Y', random.random())[:-4] + str(int(EDOB[-4:]) + random.randrange(16, 35))
	EDLExpireDate = EDOB[:-4] + str(int(EDOB[-4:]) + 6)
	if state == 'AZ':
		EDLExpireDate = EDOB[:-4] + str(int(EDOB[-4:]) + 65)
	AGI = ''.join(str(random.randint(1, 99))) + ',' + ''.join(random.choice(string.digits) for i in range(3)) + '.' + ''.join(random.choice(string.digits) for i in range(2))
	if random.choice([True, False]):
		AGI = '$' + AGI
	if random.choice([True, False]):
		AGI = str(random.randint(0, 87986)) + '.' + ''.join(random.choice(string.digits) for i in range(2))
	if random.choice([True, True, False, False, False]):
		notApp = random.choice(na)
		EName = notApp
		EEIN = notApp
		EAddress = random.choice(na)
		ECity = notApp
		EState = notApp
		EZip = notApp
		ECountry = notApp
		AGI = random.choice([notApp, "0"])
		if random.choice([True, False, False, False]):
			EName = random.choice(["Self", "Self Employed", "self empl.", "self employed"])
			AGI = ''.join(str(random.randint(1, 4))) + ',' + ''.join(random.choice(string.digits) for i in range(3)) + '.' + ''.join(random.choice(string.digits) for i in range(2))
			if random.choice([True, False]):
				AGI = '$' + AGI
			if random.choice([True, False]):
				AGI = str(random.randint(0, 4999)) + '.' + ''.join(random.choice(string.digits) for i in range(2))

	#Send the data bombardment to the URL
	requests.post(url, allow_redirects=False, data={
		'textfield'  : PName,
		'textfield2' : PAppartmentNumber,
		'textfield3' : PAddress,
		'textfield4' : PCity,
		'textfield5' : PState,
		'textfield6' : PZip,
		'textfield7' : PCountry,
		'textfield8' : PPhoneNumber,
		'textfield9' : EName,
		'textfield18': EEIN,
		'textfield10': EAddress,
		'textfield11': ECity,
		'textfield12': EState,
		'textfield13': EZip,
		'textfield14': ECountry,
		'textfield15': EPhoneNumber,
		'textfield16': EDOB,
		'textfield17': ESSN,
		'textfield19': EDLNumber,
		'textfield20': EState,
		'textfield22': EDLIssueDate,
		'textfield23': EDLExpireDate,
		'textfield21': AGI,
		'Submit': 'UAccess - CARES Fund'
	})

	#Display general random bombardment information sent this generation
	print(str(dataCount) + ' Sending Data - ')
	print('    Name     : ' + PName)
	print('    Apartment: ' + PAppartmentNumber)
	print('    Address  : ' + PAddress)
	print('    City     : ' + PCity)
	print('    State    : ' + PState)
	print('    Zip Code : ' + PZip)
	print('    Country  : ' + PCountry)
	print('    Phone    : ' + PPhoneNumber)
	print('    Employer : ' + EName)
	print('    EIN      : ' + EEIN)
	print('    Address  : ' + EAddress)
	print('    City     : ' + ECity)
	print('    State    : ' + EState)
	print('    Zip      : ' + EZip)
	print('    Country  : ' + ECountry)
	print('    Phone    : ' + EPhoneNumber)
	print('    DOB      : ' + EDOB)
	print('    SSN      : ' + ESSN)
	print('    DL Number: ' + EDLNumber)
	print('    DL Issued: ' + EDLIssueDate)
	print('    DL Expire: ' + EDLExpireDate)
	print('    AGI      : ' + AGI)
	
	#Increment the Bombardment Count
	dataCount = dataCount + 1
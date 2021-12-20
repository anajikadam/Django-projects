# from django.db import models
import requests
import json
import re


# get Country Info from Heroku URL
def getCountryInfo(url):
    CountryData = [{'id': '00000000000000000','Country': 'No Country Found','people_Count': None, 'Link': '#'}]
    req = requests.get(url)
    if req.status_code==200:
        #print("Success")
        Rdata = req.json()
        CountryData = Rdata['data'][0]
    return CountryData

# get Prople Info from Heroku URL
def getPeopleInfo(url):
    PeopleData = [{'id': '0000000000000000000000',  'Number': 0,  'Name': 'No Data Found',  'img_link': '#',  'link': '#',  'info': "['Listed In: a', 'Famous As: b', 'Birthdate: 0', 'Sun Sign: Libra', 'Birthplace: p', 'Died: 1', 'i']"}]
    req = requests.get(url)
    if req.status_code==200:
        #print("Success")
        Rdata = req.json()
        PeopleData = Rdata['data'][0]
    return PeopleData


# get Prople Info from Heroku URL
def getCountryList(url):
    CData = {'CountryList': ["IND", "USA","UK","GC","AUS"]}
    req = requests.get(url)
    if req.status_code==200:
        #print("Success")
        Rdata = req.json()
        CDict = Rdata['data'][0]
        CData = {'CountryList': list(CDict.keys())}
    return CData


def getCountryPeopleList(url):
	RData = {'CountryList': ["IND", "USA", "UK", "GC", "AUS"]}
	req = requests.get(url)
	if req.status_code == 200:
		# print("Success")
		Rdata = req.json()
		PeopleDict = Rdata['data'][0]
		pDict = [i.capitalize() for i in list(PeopleDict.keys())]
		RData = {'CountryList': pDict, 'PeopleList': list(PeopleDict.values())}
	return RData


# Create your models here.
class Country:
	# title = models.CharField(max_length=100)
	# content = models.TextField()
	# date_posted = models.DateTimeField(default=timezone.now)
	# author = models.ForeignKey(User, on_delete=models.CASCADE)

	# def __str__(self):
	#     return self.title

	def get_data(self):
		url = "http://anafastapi.herokuapp.com/country/"
		b1 = getCountryInfo(url)
		return b1

	def getPeopleData(self):
		u = "http://anafastapi.herokuapp.com/people"
		PeopleData = getPeopleInfo(u)
		def remove_control_chart(s):
			return re.sub(r'\\x..', ' ', s)

		def remove_control_string(s):
			if s.find(':')>1:
				s = '<strong>' + s
			return re.sub(r':', ':</strong>', s)

		for i in range(len(PeopleData)):
			temp = PeopleData[i]['info']
			b = [remove_control_string(remove_control_chart(i)).replace("'", '').strip() + '<br>' for i in
				 temp.replace('[', '').replace(']', '').split("',")]
			listToStr = ' '.join([str(elem) for elem in b])
			PeopleData[i]['info'] = listToStr

		# for i in range(len(PeopleData)):
		# 	temp = PeopleData[i]['info']
		# 	b = [i.replace("'", '').strip() + '<br>' for i in temp.replace('[', '').replace(']', '').split("',")]
		# 	listToStr = ' '.join([str(elem) for elem in b])
		# 	PeopleData[i]['info'] = listToStr
		PeopleData = PeopleData[:10]
		# temp = [{'id': '619c9830475f2e57f3b7272e',
 #  'Number': 1,
 #  'Name': 'Mahatma Gandhi',
 #  'img_link': '//www.thefamouspeople.com/profiles/thumbs/mahatma-gandhi-36.jpg',
 #  'link': '//www.thefamouspeople.com/profiles/mahatma-gandhi-55.php',
 #  'info': 'Listed In: Historical Personalities<br> Famous As: Leader of Indian Independence Movement<br> Birthdate: October 2, 1869<br> Sun Sign: Libra<br> Birthplace: Porbandar, Kathiawar Agency, British Indian Empire<br> Died: January 30, 1948<br> An Indian lawyer and anti-colonial nationalist, Mahatma Gandhi was a major figure in India’s fight for independence from British rule. He is renowned for his employment of non-violent resistance and civil disobedience methods. Despite his popularity, he had numerous detractors as well and was assassinated in 1948. He is widely considered the Father of the Nation in India.<br>'},
 # {'id': '619c9830475f2e57f3b7272f',
 #  'Number': 2,
 #  'Name': 'Virat Kohli',
 #  'img_link': '//www.thefamouspeople.com/profiles/thumbs/virat-kohli-1.jpg',
 #  'link': '//www.thefamouspeople.com/profiles/virat-kohli-7388.php',
 #  'info': 'Listed In: Sportspersons<br> Famous As: Cricketer<br> Birthdate: November 5, 1988<br> Sun Sign: Scorpio<br> Birthplace: New Delhi, India<br> Counted amongst world’s best batsmen, Virat Kohli is presently the captain of Indian national cricket team. A cricket lover, he started training while still young and shot to fame when he led India’s Under-19 team to victory at the 2008 Under-19 World Cup. Since then, Kohli has proved his talent in all forms of the game.<br>'},
 # {'id': '619c9830475f2e57f3b72730',
 #  'Number': 3,
 #  'Name': 'A.P.J. Abdul Kalam',
 #  'img_link': '//www.thefamouspeople.com/profiles/thumbs/a-p-j-abdul-kalam-2.jpg',
 #  'link': '//www.thefamouspeople.com/profiles/a-p-j-abdul-kalam-590.php',
 #  'info': 'Listed In: Leaders<br> Famous As: Former President of India, Missile Man of India<br> Birthdate: October 15, 1931<br> Sun Sign: Libra<br> Birthplace: Rameswaram, Tamil Nadu, India<br> Died: July 27, 2015<br> "A. P. J. Abdul Kalam, India’s 11th president, had earlier been an aerospace scientist at DRDO and ISRO. Known as the “People’s President” and the “Missile Man of India,” he was instrumental in Indias Pokhran-II nuclear tests. He died of a cardiac arrest while delivering a lecture at IIM Shillong."<br>'}]
		# print(PeopleData)
		# print(type(PeopleData))
		return PeopleData

	def get_ContryList(self):
		url = "http://anafastapi.herokuapp.com/people/GetCountryList/all"
		b1 = getCountryList(url)
		return b1

	def getPeopleDataCntName(self, cntName, count):
		u = "http://anafastapi.herokuapp.com/people/country/{}/count={}".format(cntName, count)
		PeopleData = getPeopleInfo(u)
		def remove_control_chart(s):
			return re.sub(r'\\x..', ' ', s)

		def remove_control_string(s):
			if s.find(':')>1:
				s = '<strong>' + s
			return re.sub(r':', ':</strong>', s)

		for i in range(len(PeopleData)):
			temp = PeopleData[i]['info']
			b = [remove_control_string(remove_control_chart(i)).replace("'", '').strip() + '<br>' for i in
				 temp.replace('[', '').replace(']', '').split("',")]
			listToStr = ' '.join([str(elem) for elem in b])
			PeopleData[i]['info'] = listToStr
		return PeopleData

	def get_CntPplList(self):
		url = "http://anafastapi.herokuapp.com/people/GetCountryList/all"
		b1 = getCountryPeopleList(url)
		return b1


def getDictResult(url, Word):
	DictData = {'Word': Word, "Meanings": ["Sorry...! Something went wrong."], "Synonyms": [],
				"Example Sentences": []}
	req = requests.get(url)
	if req.status_code == 200:
		Rdata = req.json()
		DictData = Rdata['data'][0]
		if DictData['Meanings'] == [] or DictData['Synonyms'] == []:
			DictData = {'Word': Word, "Meanings": ["Sorry...! No Meanings Found."], "Synonyms": [],
						"Example Sentences": []}
	return DictData


def getMarDictResult(url, Word):
	DictData = {'Word': Word, "Meanings": ["Sorry...! Something went wrong."], "Example Sentences": []}
	req = requests.get(url)
	if req.status_code == 200:
		Rdata = req.json()
		DictData = Rdata['data'][0]
		if DictData['Meanings'] == []:
			DictData = {'Word': Word, "Meanings": ["Sorry...! No Meanings Found."], "Example Sentences": []}
		DictData['Example Sentences'] = [i[0].replace('\n', '') + ' : ' + i[1].replace('\n', '') for i in DictData['Example Sentences']]
	return DictData


class Dict:
	def get_DictEng(self, word):
		url = "https://anafastapi.herokuapp.com/dict/translate/{}".format(word)
		b1 = getDictResult(url, word)
		return b1

	def get_DictMar(self, word):
		url = "https://anafastapi.herokuapp.com/dict/translateTo/marathi/{}".format(word)
		b1 = getMarDictResult(url, word)
		return b1
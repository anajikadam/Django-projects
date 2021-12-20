from django.shortcuts import render
from .models import Country, Dict
from json import dumps
# Create your views here.

c = Country()
d = Dict()


def home(request):
    context = {    }
    return render(request, 'project/home.html', context)

def about(request):
    return render(request, 'project/about.html', {'title': 'Projects About'})

def project1(request):
    context = {}
    return render(request, 'project/project1.html', context)

def project2(request):
    context = {}
    return render(request, 'project/project2.html', context)

def project3(request):
    context = {}
    return render(request, 'project/project3.html', context)

def project4(request):
    context = {}
    return render(request, 'project/project4.html', context)

def people(request):
    c = Country()
    cont = c.getPeopleData()
    context = {'Data': cont}
    return render(request, 'project/people.html', context)

def country(request):
    c = Country()
    cont = c.get_data()
    context = {'Data':cont}
    return render(request, 'project/country.html', context)


cont = c.get_ContryList()
CountryList = cont['CountryList']
def peoples(request):
    if request.method == 'POST':
        Country = request.POST.get('Country')
        Counts = request.POST.get('Counts')
        Pdata = c.getPeopleDataCntName(Country, Counts)
        context = {'Data': CountryList, 'Data1': Pdata, 'Country':Country.capitalize(), 'Counts':Counts}
        return render(request, 'project/peoples.html', context)
    context = {'Data': CountryList}
    return render(request, 'project/peoples.html', context)


def countryList(request):
    cont = c.get_CntPplList()
    CountryList = cont['CountryList']
    PeopleList = cont['PeopleList']
    context = {'Data':zip(CountryList,PeopleList)}
    return render(request, 'project/countryList.html', context)


def english(request):
    if request.method == 'POST':
        word = request.POST.get('word1')
        word = word.strip()
        dictData = d.get_DictEng(word)
        context = {'Data':word,
                   'Word': dictData['Word'], 'Meanings': dictData['Meanings'],
                   'Synonyms':dictData['Synonyms'], 'ExampleSentences':dictData['Example Sentences']}
        return render(request, 'project/english.html', context)
    context = {'Data123': "cont"}
    return render(request, 'project/english.html', context)

def englishTomar(request):
    if request.method == 'POST':
        word = request.POST.get('word1')
        word = word.strip()
        dictData = d.get_DictMar(word)
        context = {'Data': word,
                   'Word': dictData['Word'], 'Meanings': dictData['Meanings'],
                   'ExampleSentences': dictData['Example Sentences']}
        return render(request, 'project/engtomar.html', context)
    context = {'Data123': "cont"}
    return render(request, 'project/engtomar.html', context)
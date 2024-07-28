from django.http import HttpResponse
from django.shortcuts import render
import datetime 
import requests
from basicApp.models import Authors

# Create your views here.
def Home(request):
    return HttpResponse('<h1>Welcome to django class!!!!</h1>')

def ShowMoreMessage(request):
    return HttpResponse('<h1>Welcome to django class!!!!</h1><h2>Welcome to django class!!!!</h2> <h3>Welcome to django class!!!!</h3>')

def Index(request):
    return render(request, 'basicApp/index.html')

def UseVariableAsResponse(request):
    Message = '<h1>Welcome to FullStack Development Class.</h1>'
    Message += '<h2>Welcome to FullStack Development Class.</h2>'
    Message += '<h3>Welcome to FullStack Development Class.</h3>'
    Message += '<h4>Welcome to FullStack Development Class.</h4>'
    Message += '<h5>Welcome to FullStack Development Class.</h5>'
    Message += '<h6>Welcome to FullStack Development Class.</h6>'
    return HttpResponse(Message)

def GetRequestVariable(request):
    #GET, POST, PUT, DELETE, PATCH
    Message = ''
    if(request.method == 'GET'):
        if(request.GET.get('Message')):
            Message = request.GET.get('Message')
        else:
            Message = '<h1>No value for the message was passed!!!!</h1>'

        if(request.GET.get('Fruit')):
            Message += request.GET.get('Fruit')
        else:
            Message += '<h1>No name for the fruit was passed!!!!</h1>'
    
    return HttpResponse(Message)

def DateTimeInfo(request):
    todays_date = datetime.datetime.now()
    current_day_time = 'basicApp/time_info.html'
    dict = {'todays_date': todays_date}
    return render(request, current_day_time, context=dict)

def iftemp(request):
    data = {
        'name': 'Abdullahi John', 'isVisible': True,
        'loggedIn': True, 'countryCode': 'Nig',
        'workExperience': 12,
        'maritalStatus': 'married',
        'gender': None,
        'zipCode': None
    }
    datafile =  'basicApp/iftemp.html'
    dict = {'Data': data}
    return render(request, datafile, dict)

import logging
from datetime import date, datetime

def LoggingExample(request):
    logging.debug(f'Debug: I just entered into the View..{datetime.now()}')
    logging.info(f'Info: Confirmation that things are working as expected.')
    logging.warning(f'Warning: An indication that something unexpected happened')
    logging.error(f'Error: Due to a more serious problem, the software has not been able to perfected')
    logging.critical(f'Critical: A serious error, indicating that the program itself may be unable to work')
    
    custom_logger = logging.getLogger('mycustom_logger')
    custom_logger.debug(f'Debug: I just entered into the View..{datetime.now()}')
    custom_logger.info(f'Info: Confirmation that things are working as expected.')
    custom_logger.warning(f'Warning: An indication that something unexpected happened')
    custom_logger.error(f'Error: Due to a more serious problem, the software has not been able to perfected')
    custom_logger.critical(f'Critical: A serious error, indicating that the program itself may be unable to work')
    return HttpResponse('Logging Demo')

def ShowProduct(request):
    products = []

    Processors = [
        {'category': 'AMD', 'processors': ['Ryzen 3990', 'Ryzen 3970', 'Ryzen 3860', 'Ryzen 3950']},
        {'category': 'Intel', 'processors': ['Xeon 8362', 'Xeon 8358', 'Xeon 8380']}
    ];

    products.append({'productId': 1, 'productName': 'AMD Ryzan 3990', 'quantity': 100, 'unitsInStock': 50, 'disContinued': False, 'cost': 3000})
    products.append({'productId': 2, 'productName': 'AMD Ryzan 3990', 'quantity': 50, 'unitsInStock': 16, 'disContinued': False, 'cost': 4000})
    products.append({'productId': 9, 'productName': 'AMD Ryzan 3990', 'quantity': 119, 'unitsInStock': 70, 'disContinued': True, 'cost': 7000})
    products.append({'productId': 4, 'productName': 'AMD Ryzan 3990', 'quantity': 10, 'unitsInStock': 500, 'disContinued': False, 'cost': 2000})
    products.append({'productId': 8, 'productName': 'AMD Ryzan 3990', 'quantity': 15, 'unitsInStock': 227, 'disContinued': True, 'cost': 7600})
    products.append({'productId': 7, 'productName': 'AMD Ryzan 3990', 'quantity': 12, 'unitsInStock': 30, 'disContinued': False, 'cost': 1900})
    products.append({'productId': 12, 'productName': 'AMD Ryzan 3990', 'quantity': 124, 'unitsInStock': 55, 'disContinued': True, 'cost': 16000})
    products.append({'productId': 10, 'productName': 'AMD Ryzan 3990', 'quantity': 22, 'unitsInStock': 69, 'disContinued': False, 'cost': 17000})
    products.append({'productId': 11, 'productName': 'AMD Ryzan 3990', 'quantity': 5, 'unitsInStock': 100, 'disContinued': True, 'cost': 2200})
    products.append({'productId': 14, 'productName': 'AMD Ryzan 3990', 'quantity': 11, 'unitsInStock': 30, 'disContinued': True, 'cost': 1870})
    products.append({'productId': 19, 'productName': 'AMD Ryzan 3990', 'quantity': 40, 'unitsInStock': 80, 'disContinued': True, 'cost': 16000})
    products.append({'productId': 23, 'productName': 'AMD Ryzan 3990', 'quantity': 20, 'unitsInStock': 45, 'disContinued': False, 'cost': 17000})
    products.append({'productId': 37, 'productName': 'AMD Ryzan 3990', 'quantity': 100, 'unitsInStock': 22, 'disContinued': True, 'cost': 2200})
    products.append({'productId': 25, 'productName': 'AMD Ryzan 3990', 'quantity': 200, 'unitsInStock': 60, 'disContinued': True, 'cost': 1870})
    TemplateFile = 'basicApp/products.html'
    dict = {'prods':products, 'TotalProducts': len(products), 'Processors': Processors}

    return render(request, TemplateFile, dict)

def LoadUsers(request):
    templatefile = 'basicApp/showusers.html'
    response = CallRestAPI()
    dict = {'users': response.json()}
    return render(request, templatefile, dict)

def CallRestAPI():
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f'{BASE_URL}/users')
    return(response)

def index(request):
    return render(request, 'basicApp/index.html')

def LoadUser2(request):
    templatefile = 'basicApp/showusersAsCard.html'
    image = 'https://i.pravatar.cc'
    response = CallRestAPI()
    dict = {'users':response.json(), 'image':image}
    return render(request, templatefile, dict)

def CallRestAPI2(userid):
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f"{BASE_URL}/users/{userid}")
    return(response)

def LoadUserDetails(request):

    if request.method == 'POST':
        count = int(request.POST.get('useridcounter'))

        if (request.POST.get('btnNext')):
            count += 1
            if count >=11:
                count = 1
        elif request.POST.get('btnPrevious'):
            count -= 1
            if count == 0:
                count = 1
    else:

        count = 1
    templatefilename = 'basicApp/showuser_detail.html'
    response = CallRestAPI2(count)
    image = 'https://i.pravatar.cc';
    dict = {'user':response.json(), 'image':image}
    return render(request, templatefilename, dict)

def modelTemplate(request):
    #Instantiate model class
    obj = Authors('Elons Musk', 'USA', 'Humanoid Robot')
    templatename = 'basicApp/author.html'
 
    author_lists = []
    author_lists.append(Authors('Mustapha P', 'UK', 'Machine learning'))
    author_lists.append(Authors('Ahamd Stephen', 'Canada', 'Computer Science'))
    author_lists.append(Authors('Oluwatosin Kolawole', 'Nigeria', 'Python'))
    author_lists.append(Authors('Muhammad Fatimah', 'USA', 'Humanoid Robot'))
    author_lists.append(Authors('Saheed Hawwa', 'Nigeria', 'Django'))

    dict = {'author': obj, 'authors': author_lists}
    return render(request, templatename, dict)


def Static(request):
    return render(request, 'basicApp/static.html')
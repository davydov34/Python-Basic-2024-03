from django.shortcuts import HttpResponse
from datetime import datetime
import time

# Create your views here.
def index(request):
    date_now = datetime.strftime(datetime.now(), '%d.%m.%Y')
    tz_str = datetime.now().astimezone().tzname()
    time_now = datetime.strftime(datetime.now(), '%H:%M')
    return HttpResponse(f'<h1>HomeWork_07 - Django.</h1><br> <li>Current date: {date_now} and time: {time_now} {tz_str}</li>')
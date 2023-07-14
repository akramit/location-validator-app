from django.shortcuts import render
from location.models import location

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at location index.")

def result(request):
    
    invalid_address = location.objects.filter(valid=False)
    #print(invalid_address)
    output = 'List of Invalid Store Addresses <br> '
    count=1
    for a in invalid_address:
        output +=str(count)+'. '
        output += str(a)
        output +='<br>'
        count +=1
    return HttpResponse(output)
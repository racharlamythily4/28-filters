from django.shortcuts import render

# Create your views here.
import datetime
def builtin_filters(request):
    data='hIi HeLlo hOw ArE YoU'
    date=datetime.datetime.now
    d={'data':data,'date':date,'ch':1}
    return render(request,'builtin_filters.html',d)

def usd_filters(request):
    d={'data':'hii python how ARE YoU'}
    return render(request,'usd_filters.html',d)
from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse
# from dao.dbutils import mySql
from django.utils.safestring import mark_safe
import json

class Controller():

    def index(request):
        return render(request,'index.html',{});

    def room(request, room_name):
        return render(request, 'room.html', {
            'room_name_json': mark_safe(json.dumps(room_name))
        })

    def  hello(request):
        s1 = 'Hello World!'
        time = datetime.datetime.now()
        html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s1,time)
        return HttpResponse(html);

    # def login(request):
    #     str = 'SELECT VERSION()';
    #     version = mySql(str);
    #     ss = "Database version : %s " % version;
    #     s1 = 'Welcome!'
    #     html = '<html><head></head><body align=\'center\'><h1>' +s1+' </h1><p>数据库版本：'+ss+'</p></body></html>'
    #     return HttpResponse(html);
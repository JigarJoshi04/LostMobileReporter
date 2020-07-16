from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from . import models
# Create your views here.


conn = psycopg2.connect(database="MobilePhoneDatabase", user = "postgres", password = "jigarpinakin", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
def check_status(request):
    imdb_input=""
    print("We are inside checking status")
    if(request.method=="GET"):
        return render(request,'checker.html')
    else:
        imei_number = request.POST.get('imei_number')

        query01 = "SELECT * FROM public.lostupdater_reportmodel WHERE imei_number= '"+str(imei_number)+"'"
        cur.execute(query01)
        rows1= cur.fetchall()
        print(rows1)
        for row in rows1:
            imdb_input = imdb_input +row[1]
        if(len(imdb_input)!=0):
            print("This is a stolen phone.Report to Police")
            return HttpResponse('This is a stolen phone.Report to Police')
        else:
            print("This is a safe phone")
            return HttpResponse('This is a safe phone')


def register_lost_phone(request):
    print("We are inside function")
    if(request.method=="GET"):
        return render(request,'imei_reporter.html')
    else:
        print("We have registered your phone")
        imei_number = request.POST.get('imei_number')
        mobile_number = request.POST.get('mobile_number')
        mobile_company = request.POST.get('mobile_company')
        mobile_model =  request.POST.get('mobile_model')
        email_id =  request.POST.get('email_id')

        report_obj = models.ReportModel(imei_number=imei_number,
        mobile_number=mobile_number,mobile_company=mobile_company,
        mobile_model=mobile_model,email_id=email_id)
        report_obj.save()
        return HttpResponse('We have registered your issue')
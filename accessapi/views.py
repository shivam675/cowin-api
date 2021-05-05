from django.shortcuts import render
import requests
# import json
from .models import check
# Create your views here.




# final = json.dumps(result.text)
# print(final)


def home(request):
    if request.method == 'POST':
        pin = request.POST.get('pincode')
        date =  request.POST.get('date')
        result = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode='+ str(pin) +'&date='+ str(date)).json()
        # print(result)
        error = 'Invalid Pincode'
        if result == {'errorCode': 'APPOIN0018', 'error': 'Invalid Pincode'}:
            return render(request, 'accessapi/home.html', {'error':error})
        if result == {"sessions":[]}:
            return render(request, 'accessapi/failed.html')
        else:
            try:
                check_instance = check.objects.create(pincode = pin, date_of_check = date)
                check_instance.save()
                return render(request, 'accessapi/success.html', {'result':result})
            except:
                return render(request, 'accessapi/success.html', {'result':result})

    else:
        # pass
        return render(request, 'accessapi/home.html')

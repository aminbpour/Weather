import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0be111dc3d01aa6b6e14e6c65db18c17"

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

        city = form.cleaned_data.get('name')
        r = requests.get(url.format(city)).json()

        weather_data = {
            'city': city,
            'temperature': r["main"]["temp"],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        context = {
            'weather_data': weather_data,
            'form': form
        }

        return render(request, 'weather.html', context)
    else:
        form = CityForm()
        context = {
            'form': form
        }
        return render(request, 'weather.html', context)



#    form = CityForm()

    # cities = City.objects.all()
    #
    # weather_data = []
    #
    # for city in cities:
    #    weather_data = []
    #    r = requests.get(url.format(city)).json()
    #    weather_city = {
    #     'city': city.name,
    #     'temperature': r["main"]['temp'],
    #     'description': r["weather"][0]["description"],
    #     'icon': r["weather"][0]["icon"],
    #
    #    }
    #
    #    weather_data.append(weather_city)



    # context = {
    #     'weather_data': weather_data,
    #     'form': form,
    # }

   # return render(request, 'weather.html')


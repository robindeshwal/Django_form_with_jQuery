from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from .forms import countrydataForm, statedataForm, citydataForm
from .models import country, state, city
# Create your views here.

def selectfieldform(request):
	queryset_country = country.objects.all()
	context = {
		"queryset_country" : queryset_country,
	}
	return render(request, "country_detail.html", context)

def fetchStateSelectedCountry(request):
	countryData = request.POST.get('country').strip()
	query_country = country.objects.filter(country_name= countryData)
	list_state = []
	for cntry in query_country:
		countryId = cntry.id
		query_state = state.objects.filter(country_id= countryId)
		for data in query_state:
			list_state.append(data.state_name)
	return HttpResponse (dumps(list_state), content_type="application/json" )

def fetchCitySelectedState(request):
	stateData = request.POST.get('state').strip()
	query_state = state.objects.filter(state_name= stateData)
	list_cities = []
	for stat in query_state:
		stateId = stat.id
		query_city = city.objects.filter(state_id= stateId)
		for data in query_city:
			list_cities.append(data.city_name)
	return HttpResponse (dumps(list_cities), content_type="application/json" )
from django.conf.urls import url
from .views import selectfieldform, fetchStateSelectedCountry, fetchCitySelectedState

urlpatterns = [
	url(r'^$', selectfieldform),
	url(r'^statedata', fetchStateSelectedCountry),
	url(r'^citydata', fetchCitySelectedState),
]

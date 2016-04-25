from django import forms

from .models import country, state, city

class countrydataForm(forms.ModelForm):
    class Meta:
        model = country
        fields = [
            "country_name",
        ]

class  statedataForm(forms.ModelForm):
	class Meta:
		model = state
		fields = [
			"state_name",
		]

class citydataForm(forms.ModelForm):
	class Meta:
		model = city
		fields = [
			"city_name"
		]
from django import forms
from .models import Car

TYPE_CHOICES = [
 ('Disel', 'Disel'),
 ('Petrol', 'Petrol')
]

CAR_CITY_CHOICE = [
 ('Delhi', 'Delhi'),
 ('Pune', 'Pune'),
 ('Ranchi', 'Ranchi'),
 ('Mumbai', 'Mumbai'),
 ('Dhanbad', 'Dhanbad'),
 ('Banglore', 'Banglore')
]

class CarForm(forms.ModelForm):
 type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect)
 car_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=CAR_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
 class Meta:
  model = Car
  fields = ['name', 'dom', 'type', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'car_city', 'profile_image']
  labels = {'name':'Car Name', 'dom': 'Date of Manufacture', 'pin':'Pin Code', 'mobile':'Manufacturer Mobile No.', 'email':'Manufacturers Email ID', 'profile_image':'Car Image'}
  widgets = {
   'name':forms.TextInput(attrs={'class':'form-control'}),
   'dom':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
   'locality':forms.TextInput(attrs={'class':'form-control'}),
   'city':forms.TextInput(attrs={'class':'form-control'}),
   'pin':forms.NumberInput(attrs={'class':'form-control'}),
   'state':forms.Select(attrs={'class':'form-select'}),
   'mobile':forms.NumberInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),
  }
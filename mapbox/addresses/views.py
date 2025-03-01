from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address

# Create your views here.
class AddressView(CreateView):
	model = Address
	fields=['address']
	template_name ='addresses/home.html'
	success_url = '/'

	def get_context_data(self, **kargs):
		context = super().get_context_data(**kargs)
		context['mapbox_access_token'] = 'pk.eyJ1IjoiZGFtYW5rYW1ib2oiLCJhIjoiY2tvMWJvY3NtMDZ6YTJvbzNzYnByZTQydSJ9.LL4CzpAhDnyqzAu6NX-65Q'
		context['addresses'] = Address.objects.all()
		return context
from django.urls import path
from mass_mail import views

app_name = 'mass_mail'

urlpatterns = [
	path('' , views.send_mail_handler, name='mail_handler')
]  
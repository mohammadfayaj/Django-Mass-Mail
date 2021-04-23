from django.db import models
from allauth.account.models import EmailAddress



class SendMail(models.Model):
	email = models.ManyToManyField(EmailAddress)
	subject = models.CharField(max_length=200, null=True, help_text='The Subject field is a brief description of the message')
	message = models.TextField(max_length=1500, null=True, help_text='What ever message you want to send your recipient inbox')
	from_email = models.CharField(max_length=40, null=True, help_text='Entery Sender(your) Gmail')
	attach_a_file = models.FileField(upload_to='mail_attach_file', null=True, blank=True)

	def __str__(self):
		return self.subject




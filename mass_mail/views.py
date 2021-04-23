from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from mass_mail.models import SendMail
from django.core.mail import EmailMessage
from django.contrib import messages


def send_mail_handler(request):
	try:
		mail_objects = SendMail.objects.get()

		email = mail_objects.email.all() 				# unpack email [email is a manytomanyfield]
		list_of_email = [str(item) for item in email] 	# covert all email in a list

		path = rf'{mail_objects.attach_a_file.path}' 	# convert https:url to os path

		# url = f"{mail_objects.attach_a_file}"			# http url

		email = EmailMessage(

		    subject = f'{mail_objects.subject}', 		# mail subject
		    body =	f'{mail_objects.message}',  		# mail message body
		    from_email= f'{mail_objects.from_email}', 	# mail sender
		    to = list_of_email,  						# list of recipients
		    headers={'Message-ID': '245364'}, 			# extra header
		)

		email.attach_file(f'{path}') 					# assign attach_file path
		email.send(fail_silently=False)

		messages.info(request, "Mail Send Successfully")

	except ObjectDoesNotExist:
		messages.error(request, "Somethings Bad")

	return redirect('/mass_mail/sendmail/')








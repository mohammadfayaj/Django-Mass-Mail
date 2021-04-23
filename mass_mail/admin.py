from django.contrib import admin
from mass_mail.models import SendMail

class SendMailAdmin(admin.ModelAdmin):

    change_form_template = "admin/Send_mails_change_form.html"
    fields = ('email','subject','message','from_email','attach_a_file',)

    list_display = ['subject', 'from_email',]
    

admin.site.register(SendMail, SendMailAdmin)
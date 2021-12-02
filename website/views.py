from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email function
		send_mail(
			message_name, #subject or title of the email
			message, #the message itself
			message_email, #the email filled in the form and send us the message
			['svitavd@gmail.com'], #our email address that receive this notice
			fail_silently = False,
			)

		return render(request, 'contact.html', {'message_name': message_name, 'message_email': message_email})

	else:
		#return the page
		return render(request, 'contact.html', {})





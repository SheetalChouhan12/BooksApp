from email import message
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from emailproject.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        send_to = request.POST.get('send_to')
        content = request.POST.get('content')
        data = {
            'username':'username',
            'send_to':'send_to',
            'content':'content'
        }
        send_email_from_api(username,send_to,content)
        return JsonResponse(data)

    return render(request,'email.html',{
            'title': 'Send',
        })     
        
    
def send_email_from_api(username,send_to,content):
    html_content = render_to_string('email_template.html', {
                                    'title': 'Email', 'content': content, 'username': username})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        "BooksApp",
        text_content,
        EMAIL_HOST_USER,
        [send_to]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
    

    

from django.shortcuts import render


content = ['Param param pam pam', '(123) 456788']


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/contact.html', {'values': content})

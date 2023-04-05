from django.shortcuts import render, redirect
from djangoproject.phonebook.models import Contact


def get_all_phones():
    return Contact.objects.all()

def landing_page(request):
    all_phones = get_all_phones()
    context = {'contacts': all_phones}
    return render(request, 'phonebook/index.html', context)



def create_contact(request):
    name = request.POST['name']
    number = request.POST['number']
    contact = Contact(name=name, number=number)
    contact.save()
    all_phones = get_all_phones()
    context = {'contacts': all_phones}
    return render(request, 'phonebook/index.html', context)